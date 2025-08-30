import redis
import json
import sys
import os
from urllib.parse import urlparse
from dotenv import load_dotenv


# .env 파일에서 환경 변수 불러오기
load_dotenv()

# 환경 변수에서 Redis URL 불러오기
REDIS_URL = os.environ.get('REDIS_URL')

# REDIS_URL이 설정되지 않았을 경우 오류 메시지 출력
if not REDIS_URL:
    print("오류: 환경 변수 'REDIS_URL'이 설정되지 않았습니다.")
    sys.exit(1)

try:
    # URL을 파싱하여 Redis 접속 정보 추출
    parsed_url = urlparse(REDIS_URL)
    
    # Redis 접속 객체 생성
    r = redis.StrictRedis(
        host=parsed_url.hostname,
        port=parsed_url.port,
        db=int(parsed_url.path.strip('/') or 0),
        password=parsed_url.password,
        decode_responses=False
    )
    
    # 연결 테스트
    r.ping()
    print("Redis에 성공적으로 연결되었습니다!")

except Exception as e:
    print(f"Redis 연결 오류: {e}")
    sys.exit(1)

key = 'message_store:1000'

try:
    # LRANGE 명령어 실행 (바이트 문자열로 반환)
    data = r.lrange(key, 0, -1)

    # 각 항목을 JSON으로 변환하고 유니코드를 디코딩하여 출력
    if data:
        for i, item in enumerate(data):
            # 바이트 문자열을 UTF-8로 디코딩
            decoded_str = item.decode('utf-8')
            # JSON 문자열을 파이썬 딕셔너리로 로드
            json_obj = json.loads(decoded_str)
            # 보기 좋게 JSON 출력
            print(f"--- 항목 {i+1} ---")
            print(json.dumps(json_obj, indent=2, ensure_ascii=False))
    else:
        print(f"키 '{key}'에 데이터가 없습니다.")

except Exception as e:
    print(f"명령어 실행 오류: {e}")
