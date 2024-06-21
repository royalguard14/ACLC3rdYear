import numpy as np
import librosa
import torchaudio
from sklearn.mixture import GaussianMixture
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor, MarianMTModel, MarianTokenizer
import torch, os

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
    return transcription[0]

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
file_path = 'pogi.wav'
signal, sr = librosa.load(file_path, sr=None)
signal = signal / np.max(np.abs(signal))
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

# Transcription
transcription = process_wav_to_text(file_path)
print("Transcription:", transcription)

# Translation
model_name = 'Helsinki-NLP/opus-mt-ar-en'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def preprocess_input(input_text):
    tokenized_text = tokenizer.prepare_seq2seq_batch([input_text], return_tensors='pt')
    return tokenized_text

def encode_input(tokenized_text):
    encoded_states = model.get_encoder()(input_ids=tokenized_text.input_ids, attention_mask=tokenized_text.attention_mask)
    return encoded_states

def decode_states(encoded_states, tokenized_text):
    translated_tokens = model.generate(**tokenized_text)
    translated_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated_tokens]
    return translated_text

def postprocess_output(translated_text):
    final_output = translated_text[0]
    return final_output

input_text = transcription
tokenized_text = preprocess_input(input_text)
encoded_states = encode_input(tokenized_text)
translated_text = decode_states(encoded_states, tokenized_text)
final_output = postprocess_output(translated_text)

print("Translated Output:", final_output)
