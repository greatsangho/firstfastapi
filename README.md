# FirstFastAPI 🚀

FastAPI를 활용한 백엔드 프로그래밍 학습 및 클린 아키텍처 구현 프로젝트입니다.

## 프로젝트 소개 📝

이 프로젝트는 Python 기반의 FastAPI 웹 프레임워크를 학습하고, 클린 아키텍처 원칙을 적용하여 확장 가능하고 유지보수가 용이한 백엔드 시스템을 구현한 것입니다. FastAPI는 플라스크보다 API 생성이 쉽고, 장고보다 가볍다는 장점이 있어 최근 많은 주목을 받고 있는 프레임워크입니다.

## 기술 스택 💻

- Python
- FastAPI
- SQLAlchemy
- Alembic (데이터베이스 마이그레이션)
- Pydantic (데이터 유효성 검사)
- JWT (인증/인가)

## 프로젝트 구조 🏗️

```
firstfastapi/
├── common/         # 공통 모듈
├── migrations/     # 데이터베이스 마이그레이션 파일
├── note/           # 노트 관련 기능
├── user/           # 사용자 관련 기능
├── utils/          # 유틸리티 함수
├── .env            # 환경 변수 설정
├── config.py       # 설정 파일
├── containers.py   # 의존성 주입 컨테이너
├── context_vars.py # 컨텍스트 변수
├── database.py     # 데이터베이스 연결 설정
├── database_models.py # 데이터베이스 모델
├── main.py         # 애플리케이션 진입점
├── middlewares.py  # 미들웨어 설정
```

## 주요 기능 ✨

- **클린 아키텍처 적용**: 도메인, 애플리케이션, 인터페이스, 인프라 계층으로 구분하여 의존성 역전 원칙 적용
- **사용자 인증**: JWT를 활용한 로그인 및 인증 시스템
- **CRUD 기능**: 사용자 및 노트 리소스에 대한 완전한 CRUD 기능 구현
- **의존성 주입**: 코드의 결합도를 낮추고 테스트 용이성을 높이기 위한 DI 패턴 적용
- **비동기 처리**: FastAPI의 비동기 기능을 활용한 효율적인 API 호출 구현
- **미들웨어**: 요청/응답 처리를 위한 미들웨어 구현

## 학습 참고 자료 📚

- **도서**: FastAPI로 배우는 백엔드 프로그래밍 with 클린 아키텍처
- **도서**: 처음 시작하는 FastAPI
- **유튜브**: 다양한 FastAPI 튜토리얼 및 강의 영상
- **공식 문서**: FastAPI 공식 문서

## 설치 및 실행 방법 🛠️

1. 저장소 클론
```bash
git clone https://github.com/greatsangho/firstfastapi.git
cd firstfastapi
```

2. 가상환경 설정 및 의존성 설치
```bash
# Poetry를 사용한 의존성 설치
poetry install
```

3. 환경 변수 설정
```bash
# .env 파일 설정
cp .env.example .env
# 필요한 환경 변수 수정
```

4. 애플리케이션 실행
```bash
uvicorn main:app --reload
```

5. API 문서 확인
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 학습 목표 🎯

- FastAPI의 기본 개념 및 사용법 익히기
- 클린 아키텍처 원칙을 실제 프로젝트에 적용해보기
- 비동기 프로그래밍 패턴 이해하기
- 의존성 주입을 통한 코드 구조화 방법 학습
- 효율적인 API 설계 및 구현 방법 익히기
