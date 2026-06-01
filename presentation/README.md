# 프레젠테이션 가이드

## 개요
이 폴더는 집중력 강화 시스템에 대한 프레젠테이션을 포함합니다.

## 파일 구조
```
presentation/
├── index.html          # 메인 프레젠테이션 (Reveal.js 기반)
├── assets/            # 이미지, 자료 등
└── README.md          # 이 파일
```

## 사용 방법

### 로컬에서 보기
```bash
# Python 내장 서버 사용
python -m http.server 8000

# 또는 Node.js http-server 사용
npx http-server
```

브라우저에서 `http://localhost:8000/presentation/` 접속

### 키보드 단축키
- **Space / 화살표** - 슬라이드 이동
- **F** - 전체화면
- **S** - 발표 모드
- **Esc** - 슬라이드 맵 보기

## 프레젠테이션 내용

### 1️⃣ 프로젝트 비전 (Vision & Goals)
- 프로젝트 개요
- 핵심 가치
- 기대 효과

### 2️⃣ 시스템 아키텍처 (Architecture)
- Hardware Layer (Arduino)
  - 센서 구성 (진동, 조도, 초음파)
  - 데이터 송신 (MQTT/Serial)
  
- Backend Layer (Python)
  - API 서버
  - 센서 서비스
  - AI 서비스 (EXAONE)
  - 데이터 서비스
  
- Frontend Layer (Web)
  - 대시보드
  - 통계 분석
  - MediaPipe 포즈 감지
  - Chart.js 시각화
  
- Database Layer
  - 개발 환경 (H2)
  - 프로덕션 (MySQL)

### 3️⃣ WBS (Work Breakdown Structure)
세부 작업 목록:
1. Hardware Development
2. Backend Development
3. Frontend Development
4. Database Design
5. Integration & Testing

### 4️⃣ 기술 스택
- Hardware: Arduino, 센서
- Backend: Python, REST API, EXAONE AI
- Frontend: HTML/CSS/JS, Chart.js, MediaPipe
- Database: H2, MySQL

## GitHub Pages 배포

### 1. 저장소 설정
```bash
# 로컬 저장소 초기화
git init
git add .
git commit -m "Initial commit"
```

### 2. GitHub에 푸시
```bash
# GitHub에서 새 저장소 생성 후
git remote add origin https://github.com/yourusername/concentration-system.git
git branch -M main
git push -u origin main
```

### 3. GitHub Pages 활성화
1. GitHub 저장소 → Settings
2. Pages 섹션에서:
   - Source: Deploy from a branch
   - Branch: main, / (root)
3. Save

### 4. 프레젠테이션 접속
프레젠테이션은 다음 URL에서 접근 가능합니다:
```
https://yourusername.github.io/concentration-system/presentation/
```

## 프레젠테이션 커스터마이징

### CSS 수정
`index.html`의 `<style>` 섹션에서:
- 색상: `#4DB8FF` (주요 파란색)
- 폰트: `Segoe UI`
- 배경: `black` 테마

### 슬라이드 추가
```html
<section>
    <h2>새로운 제목</h2>
    <p>내용</p>
</section>
```

### 테마 변경
```html
<!-- 다른 테마 사용 -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/theme/white.css">
```

## 참고 자료

- [Reveal.js 공식 문서](https://revealjs.com/)
- [GitHub Pages 가이드](https://pages.github.com/)
- [프로젝트 아키텍처](../ARCHITECTURE.md)
- [프로젝트 README](../README.md)

## 라이센스
프로젝트와 동일한 라이센스를 따릅니다.
