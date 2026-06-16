# 🤖 AGENTS.md - 프로젝트 정책 및 에이전트 관리

> EcoMind 프로젝트의 개발 정책, AI 에이전트 활용 규칙, 그리고 Claude Code를 통한 자동화 정책을 정의합니다.

---

## 1️⃣ 프로젝트 정책

### 개발 정책
- **언어**: Python (Backend), HTML5/CSS3/JavaScript (Frontend)
- **버전 관리**: Git 기반, Semantic Versioning 준수
- **커밋 메시지**: 한글 + 영문 병행, 명확한 변경사항 명시
- **코드 스타일**: PEP 8 (Python), ESLint (JavaScript)

### 문서화 정책
- **README.md**: 프로젝트 개요, 설치, 실행 방법
- **DEPLOY.md**: 배포 가이드
- **docs/index.html**: 프레젠테이션 슬라이드 (슬라이더 형식)
- **AGENTS.md**: 이 파일 (정책 및 에이전트 정의)
- **각 폴더 README**: 모듈별 상세 문서

### 품질 정책
- **테스트**: 단위 테스트 (85%+), 통합 테스트 (100%)
- **성능**: 동시 사용자 15명 이상 지원
- **보안**: HTTPS 전송, API 인증 (JWT), MQTT QoS 1

---

## 2️⃣ AI 에이전트 활용

### Claude Code 활용 방식

#### A. 코드 작성 및 수정
- **Backend**: Python Flask 서비스 개발, MQTT 통신, 데이터 처리
- **Frontend**: HTML/CSS/JavaScript 대시보드, MediaPipe 통합
- **Deployment**: GitHub Pages, 슬라이더 형식 프레젠테이션

#### B. 문서화 자동화
- **명령어**: 
  ```bash
  claude code: <작업 요청>
  ```
- **예시**:
  - "README.md에 API 엔드포인트 추가"
  - "docs/index.html을 슬라이더 형식으로 변환"
  - "기술 스택 문서 보충"

#### C. 검증 및 리뷰
- **코드 리뷰**: `claude /code-review <file>`
- **테스트**: 신규 기능 추가 시 테스트 케이스 작성 확인
- **성능**: 배포 전 성능 테스트 검증

---

## 3️⃣ 에이전트 지침

### 작업 분류

#### 📝 문서 작업
```
범위: README, DEPLOY, 설정 가이드
도구: Read, Write, Edit
검증: 키워드 포함 여부, 형식 검증
```

#### 💻 코드 작업
```
범위: Backend (Python), Frontend (JS)
도구: Read, Edit, Bash
검증: 구문 검사, 테스트 실행
```

#### 🚀 배포 작업
```
범위: GitHub Pages, 슬라이더 형식 전환
도구: Edit, Bash, Git
검증: 브라우저 렌더링 확인
```

### 에이전트 선택 기준

| 작업 | 권장 에이전트 | 이유 |
|------|-------------|------|
| 기획/요구사항 | 일반 (General) | 복잡한 분석 필요 |
| 코드 리뷰 | code-reviewer | 전문 리뷰 |
| 문서 작성 | 일반 (General) | 명확한 요구사항 |
| 성능 최적화 | 일반 (General) | 트레이드오프 분석 |
| 보안 검토 | security-reviewer | 보안 특화 |

---

## 4️⃣ 슬래시 커맨드 정책

### 활용 중인 커맨드

```bash
# 코드 리뷰
/code-review ultra          # 다중 에이전트 클라우드 리뷰

# 설정 관리
/config                     # 기본 설정 변경
/update-config              # 고급 설정 (hooks, permissions)

# 프로젝트 관리
/init                       # 새 CLAUDE.md 초기화
```

### 호출 가이드
- **간단한 수정**: 직접 Edit/Write (에이전트 불필요)
- **복잡한 작업**: 에이전트 활용
- **병렬 작업**: 여러 에이전트 동시 실행 가능

---

## 5️⃣ 암묵지 관리 전략

### 프로젝트별 학습 내용

#### 📌 기술 결정 기록 (ADR)
- **ADR-001**: MQTT 센서 브로커 (Mosquitto)
- **ADR-002**: Flask REST API 서버
- **ADR-003**: MediaPipe 자세/얼굴 인식

#### 🔧 시행착오 기록
1. **Arduino 통신 불안정** → 연결 지연 + 재시도 로직
2. **MQTT 메시지 손실** → QoS 1 + 영속성 활성화
3. **MediaPipe 웹캠 권한** → HTTPS 인증서 + manifest.json
4. **성능 저하** → 해상도 조정 + 프레임 스킵
5. **센서 노이즈** → 이동 평균 필터 + 범위 검증

#### 📚 재사용 가능한 패턴
- **MQTT 통신 패턴**: paho-mqtt + QoS 1 + 재연결 정책
- **Flask API 패턴**: Blueprint + Service 레이어 분리
- **MediaPipe 통합**: CDN 로드 + 프레임 스킵 + 캐싱

---

## 6️⃣ 잔디 심기 전략

### 일정
- **매주 월요일**: 주간 리뷰 및 문서 보충
- **매월 첫 주**: 성능 최적화 및 기술 블로그 작성
- **스프린트 종료**: 전체 문서 갱신

### 커밋 메시지 규칙
```
<type>: <subject>

<body>

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

### 커밋 유형
- `docs`: 문서 추가/수정
- `feat`: 새 기능
- `fix`: 버그 수정
- `refactor`: 리팩토링
- `style`: 스타일 (글씨, UI)
- `perf`: 성능 최적화
- `test`: 테스트 추가

---

## 7️⃣ 체크리스트

### 신규 기능 추가 시
- [ ] 기능 구현 완료
- [ ] 테스트 작성 및 통과
- [ ] README/문서 업데이트
- [ ] docs/index.html 내용 반영
- [ ] Git 커밋 (명확한 메시지)

### 배포 전
- [ ] 모든 테스트 통과 (85% 이상)
- [ ] 성능 테스트 (15명 이상)
- [ ] 보안 검리 (HTTPS, JWT, MQTT QoS)
- [ ] 문서 최신화
- [ ] GitHub Pages 배포 확인

### 월간 리뷰
- [ ] 시행착오 기록 정리
- [ ] 아키텍처 결정 (ADR) 업데이트
- [ ] 성능 지표 검토
- [ ] 다음 월 계획 수립

---

## 📌 참고 자료

| 항목 | 위치 | 설명 |
|------|------|------|
| 프로젝트 개요 | README.md | 설치, 실행, API |
| 배포 가이드 | DEPLOY.md | 개발/프로덕션 배포 |
| 프레젠테이션 | docs/index.html | 슬라이더 형식 18개 슬라이드 |
| 기술 상세 | docs/presentation/ | 세부 기술 설명 |
| 아키텍처 | ARCHITECTURE.md | 시스템 설계 |

---

**Last Updated**: 2026-06-16  
**Version**: 1.0  
**Maintainer**: HyeRyeong125
