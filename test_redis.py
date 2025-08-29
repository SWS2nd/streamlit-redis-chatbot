import redis
import json
from dotenv import load_dotenv
from urllib.parse import urlparse
import os

# .env 불러오기
load_dotenv()

# URL 파싱
REDIS_URL = os.getenv("REDIS_URL")
redis_url = urlparse(REDIS_URL)

REDIS_HOST = redis_url.hostname
REDIS_PORT = redis_url.port
REDIS_DB = int(redis_url.path.lstrip("/")) if redis_url.path else 0
REDIS_PASSWORD = redis_url.password

# Redis 접속
r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    password=REDIS_PASSWORD,
    decode_responses=True
)

# 사용자 입력
session_id = input("확인하고 싶은 세션 ID를 입력하세요: ")
redis_key = f"message_store:{session_id}"

# Redis에 해당 키가 있는지 확인
if r.exists(redis_key):
    # 리스트 전체 가져오기
    messages = r.lrange(redis_key, 0, -1)
    print(f"세션 '{session_id}' 메시지 기록:")
    
    for i, msg in enumerate(messages, 1):
        try:
            decoded_msg = msg.decode()
            try:
                msg_obj = json.loads(decoded_msg)
                print(f"{i}: {msg_obj}")
            except json.JSONDecodeError:
                print(f"{i}: {decoded_msg}")
        except AttributeError:
            print(f"{i}: {msg}")
else:
    print(f"키 '{redis_key}'는 Redis에 존재하지 않습니다. 새 세션을 생성하지 않았습니다.")
