import librosa.display
import numpy as np
from pydub import AudioSegment
import traceback
import sys


def extract_features(file_name):
    print(f'extracting features for file: {file_name}')
    sys.stdout.flush()
    try:
        audio_data, sample_rate = librosa.load(file_name)
        stft = np.abs(librosa.stft(audio_data))

        mfccs = np.mean(librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=110).T, axis=0)
        chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
        mel = np.mean(librosa.feature.melspectrogram(audio_data, sr=sample_rate).T, axis=0)
        contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T, axis=0)
        tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(audio_data), sr=sample_rate).T, axis=0)

        features = np.concatenate([mfccs, chroma, mel, contrast, tonnetz])

        return features
    except Exception as e:
        traceback.print_exc()
        print(e)


def cut_wav_last_secs(file, secs):
    audio = AudioSegment.from_wav(file)
    duration = audio.duration_seconds
    frame_length = audio.duration_seconds / audio.frame_count()
    t1 = 0
    t2 = (duration - secs) / frame_length

    new_audio = audio.get_sample_slice(int(t1), int(t2))
    new_audio.export(file, format="wav")
