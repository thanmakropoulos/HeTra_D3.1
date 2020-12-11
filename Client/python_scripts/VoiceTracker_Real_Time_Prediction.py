import pyaudio
import math
import struct
import wave
import time
import os
import file_prediction
import threading
from datetime import datetime as dt
import time
#import paramiko
import os
import sys
import random
import string
import time
import json
import pathlib



Threshold = 20

SHORT_NORMALIZE = 1.0 / 32768.0
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
swidth = 2
RECORD_CHANNEL = 0
RECORD_SECONDS = 3
TIMEOUT_LENGTH = 1
DEVICE_INDEX = 2

f_name_directory = './python_scripts/audio'



class Recorder:
   
    
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, output=True, frames_per_buffer=chunk)

    def listen(self):
        print('Listening beginning')
        sys.stdout.flush()
        while True:
            input = self.stream.read(chunk, exception_on_overflow=False)
            rms_val = self.rms(input)
            if rms_val > Threshold:
                self.record()

    def record(self):
        print('Noise detected, recording beginning')
        sys.stdout.flush()
        rec = []
        current = time.time()
        end = time.time() + TIMEOUT_LENGTH
        max = time.time() + RECORD_SECONDS

        while current <= end and current <= max:
            data = self.stream.read(chunk)
            if self.rms(data) >= Threshold:
                end = time.time() + TIMEOUT_LENGTH
            current = time.time()
            # rec.append(np.fromstring(data, dtype=np.int16)[RECORD_CHANNEL::6].tobytes())
            rec.append(data)
        self.write(b''.join(rec))

    @staticmethod
    def rms(frame):
        count = len(frame) / swidth
        format = "%dh" % count
        shorts = struct.unpack(format, frame)

        sum_squares = 0.0
        for sample in shorts:
            n = sample * SHORT_NORMALIZE
            sum_squares += n * n
        rms = math.pow(sum_squares / count, 0.5)
        rms = rms * 1000
        return rms

    def write(self, recording):
        n_files = len(os.listdir(f_name_directory))

        filename = os.path.join(f_name_directory, '{}.wav'.format(n_files))

        wf = wave.open(filename, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(recording)
        wf.close()
        # utils.cut_wav_last_secs(filename, TIMEOUT_LENGTH)

        print('saved to file: {}'.format(filename))
        sys.stdout.flush()
        print('Returning to listening')
        sys.stdout.flush()

        thread = threading.Thread(target=file_prediction.print_prediction(filename))
        thread.start()
        
        


a = Recorder()
a.listen()