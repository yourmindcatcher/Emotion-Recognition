import os

# 기존 기능 가져오기
from emotion import analyze_emotion
from chatbot import chatbot_response

# ▶ 텍스트 모드 함수 (직접 입력)
def run_text_mode():
    print("\n✍ 텍스트 입력 모드 선택됨")
    text = input("📝 감정을 분석할 문장을 입력하세요: ").strip()
    if not text:
        print("❌ 입력된 문장이 없습니다. 프로그램을 종료합니다.")
        return
    emotion = analyze_emotion(text)
    response = chatbot_response(emotion)
    print(f"\n🎯 감정 분석 결과: {emotion}")
    print(f"🤖 챗봇 응답: {response}")


# ▶ 음성 분석은 main.py를 subprocess로 실행하도록 처리
import subprocess

def run_audio_mode():
    print("\n🎤 음성 인식 모드 선택됨 (main.py 실행)")
    try:
        subprocess.run(["python", "main.py"], check=True)
    except subprocess.CalledProcessError:
        print("❌ main.py 실행 중 오류가 발생했어요.")


if __name__ == "__main__":
    print("🧠 감정 분석 모드 선택")
    print("1. ✍ 텍스트 입력으로 감정 분석")
    print("2. 🎤 실시간 음성 인식으로 분석")
    choice = input("▶ 분석 방법을 선택하세요 (1 또는 2): ").strip()

    if choice == "1":
        run_text_mode()
    elif choice == "2":
        run_audio_mode()
    else:
        print("❌ 잘못된 선택입니다. 프로그램을 종료합니다.")
