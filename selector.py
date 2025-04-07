from stt import get_user_input_text, get_user_input_voice

def choose_character():
    print("🎭 상담 캐릭터를 선택해주세요:")
    print("1. 마루")
    print("2. 아라")

    while True:
        char_choice = input("번호 입력 (1 또는 2): ").strip()
        if char_choice == "1":
            return "마루"
        elif char_choice == "2":
            return "아라"
        else:
            print("❌ 올바른 번호를 입력해주세요 (1 또는 2).")


def main():
    print("🎈 Emotion Catcher에 오신 걸 환영합니다!")

    character_name = choose_character()
    print(f"\n🤖 선택된 상담 캐릭터: {character_name}\n")

    print("🧩 사용할 입력 방식을 선택해주세요:")
    print("1. 텍스트 입력")
    print("2. 음성 인식")

    choice = input("번호 입력 (1 또는 2): ").strip()

    if choice == "1":
        text = get_user_input_text()
    elif choice == "2":
        text = get_user_input_voice()
    else:
        print("❌ 잘못된 입력입니다. 프로그램을 종료합니다.")
        return

    if text.lower() == "종료":
        print("👋 대화를 종료합니다. 다음에 또 만나요!")
        return

    # 🔗 이후 처리 로직
    print(f"📝 입력된 내용: {text}")
    print(f"🤖 ({character_name})의 상담이 이어집니다...")

if __name__ == "__main__":
    main()
