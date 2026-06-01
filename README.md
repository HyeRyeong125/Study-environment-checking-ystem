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
단순히 공부 시간을 기록하는 것을 넘어, **하드웨어 센서**로 실제 학습 환경(조도, 자세, 소음, 활동량)을 측정하고 **EXAONE AI**가 이를 분석하여 최적의 집중 환경을 가이드하는 지능형 학습 도우미입니다.

## ✨ Key Features
- **Real-time Monitoring:** 초음파/조도/진동 센서를 통한 학습 환경 데이터 수집
- **AI Focus Guide:** EXAONE 기반의 맞춤형 자연어 피드백 제공 (자세 교정, 조명 권장 등)
- **Focus Score:** 4가지 센서 데이터를 종합한 '집중 환경 점수(100pt)' 산출
- **Pomodoro Mode:** 물리 버튼과 연동되는 스마트 뽀모도로 타이머 및 통계
- **Posture Analysis:** 초음파 센서 거리 측정을 통한 거북목 방지 알림

## 🛠 Tech Stack
### Hardware
- **Controller:** Arduino Uno / ESP32
- **Sensors:** Ultrasonic(HC-SR04), Photoresistor(LDR), Vibration(SW-420)

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
