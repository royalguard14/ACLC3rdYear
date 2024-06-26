import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import soundfile as sf
import os
from sklearn.mixture import GaussianMixture
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch

os.environ['NUMBA_DISABLE_INTEL_SVML'] = '1'

# Load and resample WAV file to 16 kHz
def load_and_resample_wav(file_path, target_sr=16000):
    signal, orig_sr = torchaudio.load(file_path)  # Load with original sampling rate
    resampler = torchaudio.transforms.Resample(orig_sr, target_sr)  # Define resampler
    signal = resampler(signal).squeeze().numpy()  # Resample to target sampling rate
    return target_sr, signal

# Load pre-trained Wav2Vec2 model and processor for Arabic
def load_model():
    processor = Wav2Vec2Processor.from_pretrained("mohammed/wav2vec2-large-xlsr-arabic")
    model = Wav2Vec2ForCTC.from_pretrained("mohammed/wav2vec2-large-xlsr-arabic")
    return processor, model

# Speech-to-Text Decoding
def speech_to_text(processor, model, signal, sample_rate):
    # Process the signal and convert it to input values for the model
    input_values = processor(signal, return_tensors="pt", sampling_rate=sample_rate).input_values
    logits = model(input_values).logits  # Get the logits (predictions) from the model
    predicted_ids = torch.argmax(logits, dim=-1)  # Get the predicted IDs (best predictions)
    transcription = processor.batch_decode(predicted_ids)  # Decode the IDs to text
    return transcription

# Main function to process and convert WAV to text
def process_wav_to_text(file_path):
    sample_rate, signal = load_and_resample_wav(file_path)  # Load and resample the audio file
    
    # Normalize the signal
    signal = (signal - np.mean(signal)) / np.std(signal)
    
    # Load the pre-trained model and processor
    processor, model = load_model()
    
    # Perform speech-to-text decoding
    transcription = speech_to_text(processor, model, signal, sample_rate)
    
    return transcription

# Load the audio file
file_path = 'pogi.wav'
signal, sr = librosa.load(file_path, sr=None)

# Normalize signal to [-1, 1]
signal = signal / np.max(np.abs(signal))

# Step 1: Noise Reduction (simple spectral subtraction)
def noise_reduction(signal, sr):
    noise = signal[:sr]  # Assume first second is noise
    noise_reduced_signal = signal - noise.mean()
    return noise_reduced_signal

# Step 2: Pre-emphasis
def pre_emphasis(signal, alpha=0.97):
    return np.append(signal[0], signal[1:] - alpha * signal[:-1])

# Step 3: Framing
def framing(signal, frame_size=0.025, frame_stride=0.01, sr=16000):
    frame_length, frame_step = frame_size * sr, frame_stride * sr
    signal_length = len(signal)
    frame_length = int(round(frame_length))
    frame_step = int(round(frame_step))
    num_frames = int(np.ceil(float(np.abs(signal_length - frame_length)) / frame_step)) + 1
    pad_signal_length = num_frames * frame_step + frame_length
    z = np.zeros((pad_signal_length - signal_length))
    pad_signal = np.append(signal, z)
    indices = np.tile(np.arange(0, frame_length), (num_frames, 1)) + np.tile(np.arange(0, num_frames * frame_step, frame_step), (frame_length, 1)).T
    frames = pad_signal[indices.astype(np.int32, copy=False)]
    return frames

# Step 4: Windowing using Hamming window
def windowing(frames):
    hamming_window = np.hamming(frames.shape[1])
    return frames * hamming_window

# Step 5: Voice Activity Detection (VAD)
def voice_activity_detection(frames, threshold=0.01):
    frame_energy = np.sum(frames**2, axis=1)
    vad_frames = frame_energy > threshold
    return vad_frames

# Step 6: Normalization
def normalization(signal):
    return signal / np.max(np.abs(signal))

# Step 7: Feature Extraction using MFCC
def mfcc_extraction(signal, sr, n_mfcc=13):
    mfcc_features = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=n_mfcc)
    return mfcc_features

# Step 8: Train Gaussian Mixture Model (GMM)
def train_gmm(features, num_components):
    gmm = GaussianMixture(n_components=num_components)
    gmm.fit(features.T)
    return gmm

# Step 9: Classify using trained GMM
def classify_gmm(gmm, features):
    return gmm.predict(features.T)

# Apply each step and visualize the results

# Step 1: Noise Reduction
clean_signal = noise_reduction(signal, sr)

# Step 2: Pre-emphasis
emphasized_signal = pre_emphasis(clean_signal)

# Step 3: Framing
frames = framing(emphasized_signal, sr=sr)

# Step 4: Windowing
windowed_frames = windowing(frames)

# Step 5: Voice Activity Detection (VAD)
vad_frames = voice_activity_detection(windowed_frames)

# Step 6: Normalization
normalized_signal = normalization(emphasized_signal)

# Step 7: MFCC Extraction
mfcc_features = mfcc_extraction(normalized_signal, sr)

# Step 8: Train Gaussian Mixture Model (GMM)
num_components = 3  # Number of components for each GMM
gmm = train_gmm(mfcc_features, num_components)

# Step 9: Classify using trained GMM
class_labels = classify_gmm(gmm, mfcc_features)

# Plot the original and processed signals
plt.figure(figsize=(20, 18))

# Original signal
plt.subplot(9, 1, 1)
plt.plot(signal)
plt.title('Original Signal')

# Noise Reduced signal
plt.subplot(9, 1, 2)
plt.plot(clean_signal)
plt.title('Noise Reduced Signal')

# Pre-emphasized signal
plt.subplot(9, 1, 3)
plt.plot(emphasized_signal)
plt.title('Pre-emphasized Signal')

# Framed signal
plt.subplot(9, 1, 4)
plt.imshow(frames.T, aspect='auto', origin='lower')
plt.title('Framed Signal')

# Windowed signal
plt.subplot(9, 1, 5)
plt.imshow(windowed_frames.T, aspect='auto', origin='lower')
plt.title('Windowed Signal')

# Voice Activity Detection (VAD) result
plt.subplot(9, 1, 6)
plt.plot(vad_frames.astype(int))
plt.title('Voice Activity Detection (VAD) Result')


#Normalized signal
plt.subplot(9, 1, 7)
plt.plot(normalized_signal)
plt.title('Normalized Signal')

#MFCC Features
plt.subplot(9, 1, 8)
librosa.display.specshow(mfcc_features, sr=sr, x_axis='time')
plt.colorbar()
plt.title('MFCC Features')

#GMM classification result
plt.subplot(9, 1, 9)
plt.plot(class_labels)
plt.title('GMM Classification Result')

plt.tight_layout()
plt.savefig('Signal_Preprocessing_and_MFCC_with_GMM.png')
plt.show()

#Example usage
file_path = 'pogi.wav' # Path to the input audio file
transcription = process_wav_to_text(file_path) # Get the transcription
print(transcription) # Print the transcription

