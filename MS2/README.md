---

## 📘 Raspberry Pi GPIO 미션

이 미션 라즈베리파이에서 Python과 gpiozero 라이브러리를 활용하여 버튼과 4개의 LED를 제어하는 4가지 미션으로 구성되어 있습니다.  
모든 미션은 동일한 핀 구성을 사용하며, 각 기능은 개별 Python 파일로 구현되어 있습니다.

---

### ✅ 핀 구성 (BCM 기준)

- **LED 핀**: `8`, `7`, `16`, `20` (LSB → MSB 순서)
- **버튼 핀**: `25`

---

### 🚩 Mission 1. 버튼이 눌린 동안만 LED 켜기

- 버튼을 누르고 있는 동안만 모든 LED가 켜지고, 버튼에서 손을 떼면 꺼집니다.
- **파일명**: `ms1.py`  
- [🔗 시연 영상 보기](https://youtube.com/shorts/2vgsYc163AU?si=fvIX7tp278h6Jksi)

---

### 🚩 Mission 2. 버튼이 눌릴 때마다 LED 토글

- 버튼을 누를 때마다 모든 LED의 상태가 반전됩니다.
  - 예: 꺼져 있던 LED가 켜지고, 켜져 있던 LED는 꺼짐
- **파일명**: `ms2.py`  
- [🔗 시연 영상 보기](https://youtube.com/shorts/XZ38Whjfkls?si=hpegGjTa71sIbqJF)

---

### 🚩 Mission 3. 버튼을 누르면 도미노 효과 실행

- 버튼을 누르면 4개의 LED가 순차적으로 켜졌다 꺼지는 **도미노 효과**를 1회 실행합니다.
- **파일명**: `ms3.py`  
- [🔗 시연 영상 보기](https://youtube.com/shorts/dienfzbpus0?si=JuLBU_ZvVTv9o6rl)

---

### 🚩 Mission 4. 버튼을 누를 때마다 4-bit 카운터 증가

- 버튼을 누를 때마다 카운터 값이 1씩 증가하고,
- 4개의 LED가 해당 값을 **이진수 형태로 표현**합니다. (0~15 반복)
- **파일명**: `ms4.py`  
- [🔗 시연 영상 보기](https://youtube.com/shorts/BuNbNGmcyFs?si=ubvBMWLoDZ1Oe17y)

---
