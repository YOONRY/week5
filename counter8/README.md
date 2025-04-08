---

## 📘 Bit Counter – Raspberry Pi

이 Bash 스크립트는 라즈베리파이의 GPIO 핀을 사용해 **0부터 7까지 이진수로 카운팅**하며, 각 비트 값을 3개의 LED로 시각적으로 표현합니다.  
LED는 1초 간격으로 ON/OFF되며 이진수 표현을 실시간으로 확인할 수 있습니다.

🎬 **시연 영상**: [YouTube에서 보기](https://youtu.be/aRUmTOn6Csc)

---

## 📌 핀 구성 (Pin Map)

![GPIO 핀맵](https://github.com/user-attachments/assets/00bb9e03-d8e6-4c5c-a78d-e17f3f1330b0)

> 참고: 사진에는 GPIO 7번 핀이 연결되어 있지만, 스크립트에서는 사용되지 않습니다.

---

## 🔌 사용 GPIO 핀 (BCM 번호 기준)

위 핀은 임의적으로 정한것이며 코드 수정에 따라 다른핀을 사용할수도 있습니다

| GPIO 번호 | 역할            | 비트 위치 |
|------------|-----------------|------------|
| GPIO 4     | LSB (2⁰ 자리)   | 오른쪽 비트 |
| GPIO 5     | 중간 비트 (2¹) | 가운데 비트 |
| GPIO 6     | MSB (2² 자리)   | 왼쪽 비트   |

---

## 🧠 코드 구조 및 설명

### 🔹 1. 핀 배열 정의
```bash
PINS=(4 5 6)
```
- 사용할 3개의 GPIO 핀 번호를 배열에 저장합니다.

---

### 🔹 2. 핀 초기 설정 (출력 모드 & OFF)
```bash
pinctrl set $p op
pinctrl set $p dl
```
- 각 핀을 **출력 모드(op)** 로 설정한 후 **Low(dl)** 상태로 초기화합니다 (LED OFF).

---

### 🔹 3. 카운터 루프 시작
```bash
while true; do
```
- 카운터를 무한 반복하는 루프입니다.

---

### 🔹 4. 0~7까지 이진수 카운트
```bash
for ((i=0; i<8; i++)); do
```
- 이진수 표현이 가능한 3비트 범위인 **0부터 7까지** 순차적으로 카운트합니다.

---

### 🔹 5. 현재 숫자의 각 비트를 추출
```bash
bit_val=$(( (i >> bit) & 1 ))
```
- 숫자 `i`의 각 비트를 추출하는 핵심 로직입니다:
  - `i >> bit`: `i`를 오른쪽으로 `bit`만큼 이동
  - `& 1`: 마지막 비트만 추출 → `0` 또는 `1`

---

### 🔹 6. 비트에 따라 LED ON/OFF
```bash
if [ "$bit_val" -eq 1 ]; then
    pinctrl set $gpio_num dh
else
    pinctrl set $gpio_num dl
fi
```
- 추출한 `bit_val`이 1이면 **High(dh)** → LED ON  
- 0이면 **Low(dl)** → LED OFF

---

### 🔹 7. 1초 대기
```bash
sleep 1
```
- LED 상태를 1초 동안 유지하고, 다음 숫자로 넘어갑니다.

---

## 🧪 예시 출력 (i = 5 → 이진수 `101`)

| 비트 위치 | GPIO 핀 | 추출된 값 | LED 상태 |
|------------|----------|------------|-----------|
| 2⁰ (LSB)   | GPIO 4   | 1          | ON        |
| 2¹         | GPIO 5   | 0          | OFF       |
| 2² (MSB)   | GPIO 6   | 1          | ON        |

결과적으로 LED는 **ON - OFF - ON** 패턴으로 점등됩니다.

---
