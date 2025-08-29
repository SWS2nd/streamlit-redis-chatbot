# Redis 연동 챗봇 프로젝트

이 프로젝트는 Streamlit과 **도커 컨테이너에서 실행되는 Redis**(벡터 저장소로 사용)를 활용한 간단한 챗봇 프로젝트입니다. 

---

## 📂 프로젝트 구조
```
streamlit-redis-chatbot/
│── app_redis.py          # Streamlit 메인 앱
│── utils_redis.py        # Redis 유틸 함수 모음
│── test_redis.py         # Redis 연동 테스트 코드
│── requirements.txt      # Python 의존성 목록
│── .env.example          # 환경 변수 예시 파일
└── README.md
```

## ⚙️ 주요 기능
- Streamlit UI: 간단한 웹 챗봇 인터페이스 제공
- Redis 연동: 도커 컨테이너의 Redis 서버를 백엔드 스토리지로 사용
- 멀티 세션 / 멀티 유저 지원: 세션별로 대화 기록을 안전하게 관리
- 테스트 코드 포함: pytest로 Redis 연결 정상 동작 확인 가능

## 💡 Redis를 Docker 컨테이너와 연동하는 의미
- 대화 기록 안정화: 앱을 종료하거나 새로고침해도 대화 내용 유지
- 환경 격리: 로컬에 직접 Redis를 설치하지 않고 Docker로 독립 실행
- 멀티 세션 / 멀티 유저 지원: 각 세션별로 데이터를 안전하게 관리
- 운영 환경과 유사한 테스트: 클라우드/서버 배포 환경에서 Redis를 사용할 때와 동일하게 개발 가능
- 확장성: 나중에 Redis를 클라우드 서비스나 다른 서버로 이전하더라도 코드 수정 최소화

## 🚀 실행 방법
### 1. 레포지토리 클론
```bash
git clone https://github.com/<your-username>/streamlit-redis-chatbot.git
cd streamlit-redis-chatbot
```

### 2. 가상환경 생성, 활성화 및 pip 업그레이드 및 의존성 설치
```bash
python -m venv <your venv>
source <your venv>/bin/activate   # macOS/Linux
<your venv>\Scripts\activate      # Windows

python -m pip install --upgrade pip

pip install -r requirements.txt
```

### 3. 환경 변수 설정
`.env` 파일을 프로젝트 루트에 생성하고 다음과 같이 작성하세요:
> 참고: .env.example 파일이 제공되므로 복사해서 수정하면 됩니다.
```bash
UPSTAGE_API_KEY=your-upstage-key
REDIS_URL=redis://:yourpassword@localhost:6379/0
```
- REDIS_URL : Redis 접속 URL
- yourpassword : Redis 컨테이너 실행 시 설정한 비밀번호
- localhost : Redis 호스트 (Docker 컨테이너가 로컬에서 실행 중일 경우 localhost)
- 6379 : Redis 기본 포트
- /0 : Redis DB 인덱스 (기본값 0)

### 4. Docker 컨테이너에서 Redis 실행 (비밀번호 지정 꼭!)
```bash
docker run -d \
  --name my-redis \
  -p 6379:6379 \
  -e REDIS_PASSWORD=yourpassword \
  redis:7 redis-server --requirepass yourpassword
```

### 5. Redis 연결 테스트(선택)
Redis 컨테이너를 실행한 뒤 테스트를 실행합니다:
```bash
pytest test_redis.py
```

### 6. Streamlit 앱 실행
```bash
streamlit run app_redis.py
```

## 📜 라이선스
이 프로젝트는 Apache License 2.0 을 따릅니다.