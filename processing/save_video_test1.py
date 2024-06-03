import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import time
import threading
from core.camera import camera

def record_environment_sound(duration, filename):
    # 设置录制参数
    sample_rate = 44100  # 采样率（每秒采样数）
    channels = 2  # 声道数（1表示单声道，2表示立体声）
    
    # 开始录制环境音
    print("开始录制音频...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype=np.int16)
    sd.wait()  # 等待录制完成
    
    # 保存录音文件
    write(filename, sample_rate, recording)
    
    print(f"音频已保存到文件: {filename}")

## 使用多线程技术，点击保存视频按钮后，可以录制5秒的视频和音频

class SaveVideoThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.frame_interval = 1 / 24
        self.start_time = time.perf_counter()
        self.success = False
        self.lock = threading.Lock()  # 创建锁对象

    def run(self):
        # 同时开始录制视频和音频
        video_thread = threading.Thread(target=self.record_video)
        audio_thread = threading.Thread(target=self.record_audio)

        video_thread.start()
        audio_thread.start()

        video_thread.join()
        audio_thread.join()

        if self.success:
            print("视频和音频保存成功！")
        else:
            print("视频和音频保存失败！")

    def record_video(self):
        print("现在开始录制视频！")
        frame_time = self.start_time

        while True:
            with self.lock:
                # camera.tmp_im2 是捕获的视频帧
                camera.result.write(camera.tmp_im1)
                
            time.sleep(self.frame_interval)
            frame_time += self.frame_interval
            
            # 检查是否录制结束
            if frame_time >= self.start_time + 10:  # 后5秒
                self.success = True
                camera.result.release()
                break

    def record_audio(self):
        # 同时录制音频
        record_environment_sound(10,"environment_sound.wav")

def video_record():
    # 创建线程并启动
    save_video_thread = SaveVideoThread()
    save_video_thread.start()
