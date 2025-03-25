from stt import speech_to_text
from emotion import analyze_emotion
from chatbot import chatbot_response

# 음성 파일 입력
audio_file = "recorded.wav"

# 1️⃣ STT 실행
text = speech_to_text(audio_file)

# 2️⃣ 감정 분석 실행
emotion_label = analyze_emotion(text)

# 3️⃣ 감정 분석 결과에 따른 챗봇 응답 출력
response = chatbot_response(emotion_label)
print("🤖 챗봇 응답:", response)