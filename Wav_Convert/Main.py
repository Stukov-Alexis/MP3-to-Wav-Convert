from pydub import AudioSegment
import os

# Set input and output folders
input_folder = "MP3"
output_folder = "WAV"
os.makedirs(output_folder, exist_ok=True)

# Loop through all mp3 files
for filename in os.listdir(input_folder):
    if filename.endswith(".mp3"):
        mp3_path = os.path.join(input_folder, filename)
        wav_path = os.path.join(output_folder, filename.replace(".mp3", ".wav"))
        
        sound = AudioSegment.from_mp3(mp3_path)
        sound.export(wav_path, format="wav")
        print(f"Converted: {filename} → {wav_path}")
