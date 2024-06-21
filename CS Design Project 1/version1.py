import os
import subprocess
import wave
import numpy as np
import matplotlib.pyplot as plt

# Function to plot audio waveform
def plot_waveform(audio_file):
    with wave.open(audio_file, 'rb') as wave_file:
        # Read audio data
        frame_rate = wave_file.getframerate()
        n_frames = wave_file.getnframes()
        audio_data = np.frombuffer(wave_file.readframes(n_frames), dtype=np.int16)
        
        # Time axis
        time = np.linspace(0, len(audio_data) / frame_rate, num=len(audio_data))

        # Plot waveform
        plt.figure(figsize=(10, 4))
        plt.plot(time, audio_data, color='b')
        plt.title('Audio Waveform')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()

# Function to transcribe audio using Kaldi
def transcribe_audio(audio_file):

    kaldi_command = ['kaldi/egs/mgb2_arabic/s5/steps/online/nnet2/online2-wav-nnet3-latgen-faster', '--options', 'arguments']

    
    # Run Kaldi ASR
    result = subprocess.run(kaldi_command, input=open(audio_file, 'rb'), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Check for errors
    if result.returncode != 0:
        print("Error:", result.stderr)
        return None
    
    # Get recognized text
    recognized_text = result.stdout.strip()
    
    return recognized_text

# Main function
def main(audio_file):
    # Plot audio waveform
    plot_waveform(audio_file)
    
    # Transcribe audio
    recognized_text = transcribe_audio(audio_file)
    if recognized_text:
        print("Recognized Text:", recognized_text)

if __name__ == "__main__":
    # Provide the path to your input audio file
    audio_file_path = "pogi.wav"
    
    # Check if the audio file exists
    if os.path.exists(audio_file_path):
        main(audio_file_path)
    else:
        print("Error: Audio file not found.")
