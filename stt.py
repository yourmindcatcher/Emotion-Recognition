import whisper
import sounddevice as sd
import numpy as np
import wave
import os 

# 모델 로드
model = whisper.load_model("base")

# 오디오 녹음 설정
SAMPLE_RATE = 44100  # 44.1kHz
DURATION = 5  # 녹음 시간 (초)
FILENAME = "C:/Users/je547/Desktop/yourmindcatcher/recorded.wav"

def record_audio(filename, duration, sample_rate):
    print("🎤 녹음 시작...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
    sd.wait()  # 녹음 완료까지 대기
    print("✅ 녹음 완료!")

    # WAV 파일 저장
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit 오디오
        wf.setframerate(sample_rate)
        wf.writeframes(recording.tobytes())
        
    if not os.path.exists(FILENAME):
        print(f"❌ 녹음 파일이 존재하지 않아요: {FILENAME}")
    else:
        print(f"✅ 녹음 파일 확인 완료: {FILENAME}")

def speech_to_text(audio_file):
    # Whisper 모델 로드
    model = whisper.load_model("base")

    print(f"📝 음성 파일 분석 중: {audio_file}")
    result = model.transcribe(audio_file)
    print("📝 변환된 텍스트:", result["text"])
    return result["text"]