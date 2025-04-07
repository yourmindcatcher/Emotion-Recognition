import speech_recognition as sr
import time

recognizer = sr.Recognizer()
recognizer.energy_threshold = 150

# ✍ 텍스트 입력용 함수
def get_user_input_text():
    return input("✍ 대화 입력: ")

# 🎙 음성 인식용 함수
def get_user_input_voice():
    print("\n🟢 음성 인식을 시작합니다! 마이크에 대고 자연스럽게 말해주세요.")
    print("💡 말을 멈춘 뒤 5초 이상 조용하면 대화를 종료합니다.\n")

    last_spoken_time = time.time()
    combined_text = ""

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                text = recognizer.recognize_google(audio, language="ko-KR")
                print(f"🗣 {text}")
                combined_text += " " + text
                last_spoken_time = time.time()

            except sr.WaitTimeoutError:
                if time.time() - last_spoken_time > 5:
                    print("⛔ 5초 동안 말이 없어 대화를 종료합니다.")
                    return "종료"
                continue

            except sr.UnknownValueError:
                print("⚠️ 음성을 인식하지 못했어요. 다시 말씀해주세요.")
                if time.time() - last_spoken_time > 5:
                    print("⛔ 5초 동안 말이 없어 대화를 종료합니다.")
                    return "종료"
                continue

            except sr.RequestError:
                print("⚠️ 인식 서버 오류 발생. 텍스트로 입력해주세요.")
                return input("✍ 대화 입력: ")