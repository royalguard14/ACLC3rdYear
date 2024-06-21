import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import os
from sklearn.mixture import GaussianMixture
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch

os.environ['NUMBA_DISABLE_INTEL_SVML'] = '1'

# Load and resample WAV file to 16 kHz
def load_and_resample_wav(file_path, target_sr=16000):
    signal, orig_sr = torchaudio.load(file_path)
    resampler = torchaudio.transforms.Resample(orig_sr, target_sr)
    signal = resampler(signal).squeeze().numpy()
    return target_sr, signal

# Load pre-trained Wav2Vec2 model and processor for Arabic
def load_model():
    processor = Wav2Vec2Processor.from_pretrained("mohammed/wav2vec2-large-xlsr-arabic")
    model = Wav2Vec2ForCTC.from_pretrained("mohammed/wav2vec2-large-xlsr-arabic")
    return processor, model

# Speech-to-Text Decoding
def speech_to_text(processor, model, signal, sample_rate):
    input_values = processor(signal, return_tensors="pt", sampling_rate=sample_rate).input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)
    return transcription

# Main function to process and convert WAV to text
def process_wav_to_text(file_path):
    sample_rate, signal = load_and_resample_wav(file_path)
    signal = (signal - np.mean(signal)) / np.std(signal)  # Normalization
    processor, model = load_model()
    transcription = speech_to_text(processor, model, signal, sample_rate)
    return transcription

# Load the audio file
file_path = 'pogi.wav'
signal, sr = librosa.load(file_path, sr=None)

# Normalize signal to [-1, 1]
signal = signal / np.max(np.abs(signal))

# Define signal processing functions
def noise_reduction(signal, sr):
    noise = signal[:sr]
    noise_reduced_signal = signal - noise.mean()
    return noise_reduced_signal

def pre_emphasis(signal, alpha=0.97):
    return np.append(signal[0], signal[1:] - alpha * signal[:-1])

def framing(signal, frame_size=0.025, frame_stride=0.01, sr=16000):
    frame_length, frame_step = frame_size * sr, frame_stride * sr
    frame_length, frame_step = int(round(frame_length)), int(round(frame_step))
    signal_length = len(signal)
    num_frames = 1 + int(np.ceil((1.0 * signal_length - frame_length) / frame_step))
    pad_signal_length = int((num_frames - 1) * frame_step + frame_length)
    z = np.zeros((pad_signal_length - signal_length))
    pad_signal = np.append(signal, z)
    indices = np.tile(np.arange(0, frame_length), (num_frames, 1)) + \
              np.tile(np.arange(0, num_frames * frame_step, frame_step), (frame_length, 1)).T
    frames = pad_signal[indices.astype(np.int32, copy=False)]
    return frames

def windowing(frames):
    frame_length = frames.shape[1]
    hamming_window = np.hamming(frame_length)
    return frames * hamming_window[None, :]


def voice_activity_detection(frames, threshold=0.01):
    frame_energy = np.sum(frames**2, axis=1)
    vad_frames = frame_energy > threshold
    return vad_frames

def mfcc_extraction(signal, sr, n_mfcc=13):
    mfcc_features = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=n_mfcc)
    return mfcc_features

def train_gmm(features, num_components):
    gmm = GaussianMixture(n_components=num_components)
    gmm.fit(features.T)
    return gmm

def classify_gmm(gmm, features):
    return gmm.predict(features.T)

# Apply signal processing steps
clean_signal = noise_reduction(signal, sr)
emphasized_signal = pre_emphasis(clean_signal)
frames = framing(emphasized_signal, sr=sr)
windowed_frames = windowing(frames)
vad_frames = voice_activity_detection(windowed_frames)
normalized_signal = (emphasized_signal - np.mean(emphasized_signal)) / np.std(emphasized_signal)
mfcc_features = mfcc_extraction(normalized_signal, sr)
num_components = 3
gmm = train_gmm(mfcc_features, num_components)
class_labels = classify_gmm(gmm, mfcc_features)

# Plot the signals and features
plt.figure(figsize=(20, 18))
plt.subplot(9, 1, 1)
plt.plot(signal)
plt.title('Original Signal')

plt.subplot(9, 1, 2)
plt.plot(clean_signal)
plt.title('Noise Reduced Signal')

plt.subplot(9, 1, 3)
plt.plot(emphasized_signal)
plt.title('Pre-emphasized Signal')

plt.subplot(9, 1, 4)
plt.imshow(frames.T, aspect='auto', origin='lower')
plt.title('Framed Signal')

plt.subplot(9, 1, 5)
plt.imshow(windowed_frames.T, aspect='auto', origin='lower')
plt.title('Windowed Signal')

plt.subplot(9, 1, 6)
plt.plot(vad_frames.astype(int))
plt.title('Voice Activity Detection (VAD) Result')

plt.subplot(9, 1, 7)
plt.plot(normalized_signal)
plt.title('Normalized Signal')

plt.subplot(9, 1, 8)
librosa.display.specshow(mfcc_features, sr=sr, x_axis='time')
plt.colorbar()
plt.title('MFCC Features')

plt.subplot(9, 1, 9)
plt.plot(class_labels)
plt.title('GMM Classification Result')

plt.tight_layout()
plt.savefig('Signal_Preprocessing_and_MFCC_with_GMM.png')
plt.show()

# Get transcription
transcription = process_wav_to_text(file_path)
print(transcription)
