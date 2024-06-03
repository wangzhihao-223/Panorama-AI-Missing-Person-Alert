import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

class voice():
    def record_environment_sound(duration, filename):
        # 设置录制参数
        sample_rate = 44100  # 采样率（每秒采样数）
        channels = 2  # 声道数（1表示单声道，2表示立体声）
    
        # 开始录制环境音
        print("开始录制环境音...")
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype=np.int16)
        sd.wait()  # 等待录制完成
    
        # 保存录音文件
        write(filename, sample_rate, recording)
    
        print(f"环境音已保存到文件: {filename}")

    # 示例：录制 5 秒钟的环境音，并保存到 "environment_sound.wav" 文件中
    record_environment_sound(5, "environment_sound.wav")
