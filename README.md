# 🌿 EcoMind: AI 기반 스마트 학습 환경 최적화 시스템
> **Arduino + FastAPI + EXAONE AI + Flutter**를 활용한 Full-Stack IoT 프로젝트입니다.

[![Platform](https://img.shields.io/badge/Platform-Flutter%20%7C%20Android%20%7C%20iOS-blue)](https://flutter.dev)
[![Backend](https://img.shields.io/badge/Backend-FastAPI-green)](https://fastapi.tiangolo.com)
[![AI](https://img.shields.io/badge/AI-LG%20EXAONE-orange)](https://www.lgresearch.ai/)

---

## 🎬 📊 라이브 프레젠테이션

**[GitHub Pages에서 인터랙티브 프레젠테이션 보기 →](https://HyeRyeong125.github.io/Study-environment-checking-ystem/presentation/)**

프로젝트의 비전, 시스템 아키텍처, WBS(Work Breakdown Structure)를 포함한 완전한 프레젠테이션입니다.

**키보드 단축키:** Space/→(다음) ← (이전) | F(전체화면) | S(발표자 모드) | Esc(맵) | ?(도움말)

---

## 📝 Project Overview
단순히 공부 시간을 기록하는 것을 넘어, 하드웨어 센서를 통해 자세, 소음, 활동량 등 실제 학습 환경을 이해하고 EXAONE AI가 이를 분석하여 학생이 가장 몰입할 수 있는 환경으로 스스로 조정해 나가도록 돕는 지능형 학습 동반자입니다.

## ✨ Key Features
- **Real-time Monitoring:** 초음파/조도/진동 센서를 통한 학습 환경 데이터 수집
- **AI Focus Guide:** EXAONE 기반의 맞춤형 자연어 피드백 제공 (자세 교정, 조명 권장 등)
- **Focus Score:** 4가지 센서 데이터를 종합한 '집중 환경 점수(100pt)' 산출
- **Pomodoro Mode:** 물리 버튼과 연동되는 스마트 뽀모도로 타이머 및 통계
- **Posture Analysis:** 초음파 센서 거리 측정을 통한 거북목 방지 알림

## ⚙️ 설치 및 셋업

### Arduino 센서 연결 및 설정

#### 1. 하드웨어 연결
```
HC-SR04 (초음파 센서):
  TRIG → Digital Pin 7
  ECHO → Digital Pin 8
  VCC  → 5V
  GND  → GND

PWD-LED (조도 센서):
  Signal → Analog Pin A0
  VCC    → 5V
  GND    → GND

HW-072 (진동 센서):
  Signal → Analog Pin A1
  VCC    → 5V
  GND    → GND

Microphone (HW):
  Signal → Analog Pin A2
  +      → 5V
  G      → GND
```

#### 2. Arduino IDE 설정
1. Arduino IDE 다운로드: [arduino.cc](https://www.arduino.cc/en/software)
2. 보드 선택: Tools → Board → Arduino Uno
3. 포트 선택: Tools → Port → `/dev/cu.usbserial-140` (Mac)
4. `arduino/sensor_sketch.ino` 파일 열기
5. Upload 버튼 클릭 (또는 Ctrl+U)

#### 3. Python Gateway 실행
```bash
# 1. 환경 변수 설정
cp .env.example .env
# .env 파일에서 ARDUINO_SERIAL_PORT 확인

# 2. 의존성 설치
pip install -r backend/requirements.txt

# 3. MQTT 브로커 실행 (Docker)
docker run -it --rm --name mosquitto -p 1883:1883 eclipse-mosquitto

# 4. 다른 터미널에서 Gateway 실행
python backend/arduino_gateway.py
```

#### 4. 데이터 흐름
```
Arduino (Sensors) 
    ↓ (USB Serial)
Python Gateway
    ↓ (MQTT)
MQTT Broker
    ↓ (MQTT Subscribe)
Backend Flask/FastAPI
    ↓ (REST API)
Flutter Mobile App
```

---

## 🛠 Tech Stack
### Hardware
- **Controller:** Arduino Uno
- **Sensors:** Ultrasonic(HC-SR04), Photoresistor(PWD-LED), Vibration(HW-072), Microphone(HW)

### Backend & AI
- **Language:** Python 3.10+
- **Framework:** FastAPI
- **AI Model:** LG EXAONE (via API/Local)
- **Database:** PostgreSQL (Log Data), Redis (Real-time State)

### Mobile
- **Framework:** Flutter
- **State Management:** GetX
- **Communication:** MQTT / REST API

## 🏗 System Architecture
```mermaid
graph TD
    A[Arduino Sensors] -->|Serial/MQTT| B[Python Gateway]
    B --> C[FastAPI Server]
    C --> D[(PostgreSQL)]
    C --> E[EXAONE AI Model]
    E -->|Analysis| C
    C --> F[Flutter Mobile App]
    F -->|Control| C
    C -->|Command| A
