def chatbot_response(emotion):
    """ 감정에 따른 챗봇 응답 """
    responses = {
        "joy": "좋은 일이 있으셨나요? 함께 기뻐해드릴게요!",
        "sadness": "괜찮아요, 무슨 일이 있었나요? 이야기해 주세요.",
        "anger": "화가 나셨군요. 이유를 말해주실 수 있을까요?",
        "fear": "불안한 감정이 드시나요? 제가 도와드릴 수 있을까요?",
    }
    return responses.get(emotion, "어떤 감정이신가요? 말해 주세요!")