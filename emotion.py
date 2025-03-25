from transformers import pipeline

# 감정 분석 모델 로드
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/bert-base-go-emotion")

def analyze_emotion(text):
    """ 텍스트에서 감정을 분석 """
    print("🔍 감정 분석 실행...")
    result = emotion_classifier(text)
    print("🎯 감정 분석 결과:", result)
    return result[0]["label"]  # 감정 라벨 반환