# 집중력 강화 시스템 🎯

IoT 센서 기반의 실시간 집중력 모니터링 및 환경 개선 시스템입니다.

> ⚡ **라이브 프레젠테이션**: [GitHub Pages에서 보기](#github-pages-배포)

## 🎯 프로젝트 비전

사용자의 집중력 상태를 실시간으로 모니터링하고, AI 기반 자동 조언을 통해 최적의 작업 환경을 제공합니다.

## 📁 프로젝트 구조

```
project-root/
├── presentation/          # 🎬 프레젠테이션 (GitHub Pages)
│   ├── index.html        # Reveal.js 기반 인터랙티브 프레젠테이션
│   └── README.md         # 프레젠테이션 가이드
│
├── hardware/              # 🔧 Arduino 펌웨어 및 센서
│   ├── firmware/         # 메인 스케치
│   ├── libraries/        # 외부 라이브러리
│   └── docs/            # 하드웨어 문서
│
├── backend/              # ⚙️ Python 백엔드 서버
│   ├── app/
│   │   ├── api/         # API 엔드포인트
│   │   ├── services/    # 비즈니스 로직
│   │   ├── models/      # 데이터 모델
│   │   └── config/      # 설정
│   └── requirements.txt
│
├── frontend/             # 🎨 웹 프론트엔드
│   ├── public/          # 정적 파일
│   ├── src/
│   │   ├── pages/       # HTML 페이지
│   │   ├── css/         # 스타일시트
│   │   └── js/          # JavaScript
│   └── index.html
│
├── database/             # 💾 데이터베이스
│   ├── h2/              # 개발용 (H2)
│   └── mysql/           # 프로덕션 (MySQL)
│
├── docs/                # 📖 프로젝트 문서
├── ARCHITECTURE.md      # 🏗️ 시스템 아키텍처 다이어그램
└── _config.yml         # GitHub Pages 설정
```

## 🛠️ 기술 스택

| 계층 | 기술 |
|------|------|
| **Hardware** | Arduino, 진동/조도/초음파 센서 |
| **Backend** | Python, REST API, EXAONE AI |
| **Frontend** | HTML/CSS/JavaScript, Chart.js, MediaPipe |
| **Database** | H2 (개발), MySQL (프로덕션) |
| **Presentation** | Reveal.js, GitHub Pages |

## 🚀 빠른 시작

### 1. 저장소 클론
```bash
git clone https://github.com/HyeRyeong125/Study-environment-checking-ystem.git
cd Study-environment-checking-ystem
```

### 2. 각 컴포넌트 설정

#### 하드웨어
```bash
# Arduino IDE에서 firmware/main.ino 파일 열기
# 필요한 라이브러리 설치 후 업로드
```

#### 백엔드
```bash
cd backend
pip install -r requirements.txt
python main.py
```

#### 프론트엔드
```bash
cd frontend
python -m http.server 8000
# 또는
npx http-server
```

#### 프레젠테이션 (로컬)
```bash
cd presentation
python -m http.server 8000
# http://localhost:8000 접속
```

## 📊 GitHub Pages 배포

### 1단계: GitHub 저장소 생성
1. [GitHub](https://github.com/new)에서 새 저장소 생성
2. 저장소 이름: `concentration-system` (또는 원하는 이름)
3. Public으로 설정

### 2단계: GitHub에 푸시 (이미 연결됨)
```bash
# 변경사항이 있으면 추가 커밋 후 푸시
git add .
git commit -m "Add: Project updates"
git push origin main
```

### 3단계: GitHub Pages 활성화
1. GitHub 저장소 → **Settings**
2. 왼쪽 메뉴에서 **Pages** 클릭
3. **Source** 설정:
   - Branch: `main`
   - Folder: `/ (root)`
4. **Save** 클릭

### 4단계: 프레젠테이션 접속 🎉
```
https://HyeRyeong125.github.io/Study-environment-checking-ystem/presentation/
```

## 📋 프레젠테이션 내용

프레젠테이션은 다음 항목들을 포함합니다:

### 1️⃣ 프로젝트 비전 (Vision & Goals)
- 프로젝트 개요
- 핵심 가치
- 기대 효과

### 2️⃣ 시스템 아키텍처 (Architecture)
- Hardware 계층 (Arduino 센서)
- Backend 계층 (Python API)
- Frontend 계층 (Web UI)
- Database 계층 (H2/MySQL)
- 데이터 흐름

### 3️⃣ WBS (Work Breakdown Structure)
- 상세 작업 목록
- 프로젝트 일정
- Phase별 마일스톤

### 4️⃣ 기술 스택 및 배포

## 🎮 프레젠테이션 사용법

### 키보드 단축키
| 키 | 기능 |
|----|------|
| **Space / →** | 다음 슬라이드 |
| **← / ↑** | 이전 슬라이드 |
| **F** | 전체화면 |
| **S** | 발표자 보기 |
| **Esc** | 슬라이드 맵 |
| **?** | 도움말 |

### 프레젠테이션 커스터마이징
`presentation/index.html` 파일을 수정하여:
- 색상 변경 (CSS `<style>` 섹션)
- 슬라이드 추가/수정
- 테마 변경 (Reveal.js 테마)

자세한 내용은 [프레젠테이션 README](./presentation/README.md) 참고

## 📖 추가 문서

- [프로젝트 아키텍처](./ARCHITECTURE.md) - Mermaid 다이어그램 포함
- [하드웨어 설정](./hardware/README.md)
- [백엔드 설정](./backend/README.md)
- [프론트엔드 설정](./frontend/README.md)
- [데이터베이스 구성](./database/README.md)
- [프레젠테이션 가이드](./presentation/README.md)

## 📝 라이센스

이 프로젝트는 MIT 라이센스를 따릅니다.

## 👨‍💻 기여

이 프로젝트에 기여하려면:

1. 저장소를 포크합니다.
2. Feature 브랜치를 생성합니다. (`git checkout -b feature/AmazingFeature`)
3. 변경 사항을 커밋합니다. (`git commit -m 'Add some AmazingFeature'`)
4. 브랜치로 푸시합니다. (`git push origin feature/AmazingFeature`)
5. Pull Request를 생성합니다.

## 📞 연락

- 이메일: cs012_c@ainuri.kr
- GitHub Issues: [프로젝트 이슈](https://github.com/HyeRyeong125/Study-environment-checking-ystem/issues)
- 프레젠테이션: [GitHub Pages](https://HyeRyeong125.github.io/Study-environment-checking-ystem/presentation/)
