---

## 📘 LED Domino – Raspberry Pi

이 Bash 스크립트는 Raspberry Pi의 GPIO 핀 4번부터 7번까지를 사용하여,  
**LED 4개를 도미노처럼 순차적으로 점등**하는 간단한 GPIO 제어 예제입니다.  
각 LED는 1초 간격으로 켜졌다가 꺼지며, 이 동작이 반복되어 시각적으로 흐르는 듯한 LED 효과를 보여줍니다.

🎬 **시연 영상**: [YouTube에서 보기](https://youtu.be/GSWM3ugUTAc)

---

## 🔌 하드웨어 구성 예시

### 📸 실물 연결 사진
![KakaoTalk_20250408_103805833_01](https://github.com/user-attachments/assets/6347278f-6821-464c-bee6-e347d14aa235)

### 🖥️ Fritzing 회로도
![화면 캡처 2025-04-08 112656](https://github.com/user-attachments/assets/35d7466e-ef95-42b2-84bb-06b0aba9575f)

### 📍 GPIO 핀 연결

| GPIO 번호 | 연결된 부품 |
|-----------|--------------|
| GPIO 4    | LED 1        |
| GPIO 5    | LED 2        |
| GPIO 6    | LED 3        |
| GPIO 7    | LED 4        |

> 💡 해당 핀 번호는 코드에서 임의로 지정된 값이며, 필요 시 다른 핀으로 변경 가능합니다.

---

## 💻 코드 설명

### 🔧 핀 초기화

```bash
for a in {4..7}; do
    pinctrl set $a op
    pinctrl set $a dl
done
```

- GPIO 4~7번을 **출력 모드(op)** 로 설정합니다.
- 모든 핀의 초기 출력을 **Low(dl)** 로 설정하여 LED를 꺼둡니다.

---

### 🔁 메인 루프 – 도미노 점등

```bash
while true; do
    for p in {4..7}; do
        pinctrl set $p dh
        sleep 1
        pinctrl set $p dl
    done
done
```

- 무한 루프를 통해 LED 4개를 순차적으로 제어합니다.
- 각 핀에 1초 동안 **High(dh)** 신호를 보내 LED를 점등한 후, 다시 **Low(dl)** 로 꺼줍니다.
- 이 과정을 반복하여 **도미노처럼 흐르는 점등 효과**를 만듭니다.

---

