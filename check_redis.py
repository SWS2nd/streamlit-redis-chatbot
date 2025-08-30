import os
from dotenv import load_dotenv
from langchain_community.chat_message_histories import RedisChatMessageHistory

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

# 환경 변수에서 REDIS_URL 값을 가져옵니다.
# REDIS_URL이 설정되지 않은 경우 오류를 방지하기 위해 None을 반환합니다.
redis_url = os.getenv("REDIS_URL")

# redis_url이 유효한지 확인합니다.
if not redis_url:
    raise ValueError("환경 변수 'REDIS_URL'이 설정되지 않았습니다.")

# 가져온 URL을 사용하여 RedisChatMessageHistory 인스턴스를 생성합니다.
history = RedisChatMessageHistory(
    session_id="your_session_id",
    url=redis_url
)

print(history)