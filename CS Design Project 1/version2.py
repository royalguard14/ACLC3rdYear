import numpy as np
import librosa
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch
import os

# Disable Intel SVML to avoid compatibility issues with librosa
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

# Example usage
file_path = 'pogi.wav'  # Path to the input audio file
transcription = process_wav_to_text(file_path)  # Get the transcription
print(transcription)  # Print the transcription
