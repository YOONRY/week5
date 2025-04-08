---

## 📘 README – LED Domino (Raspberry Pi)

이 Bash 스크립트는 Raspberry Pi의 GPIO 핀 4번부터 7번까지를 이용해, **LED 4개를 도미노처럼 순차적으로 점등**하는 간단한 GPIO 제어 예제입니다.  
각 LED는 1초 간격으로 켜졌다 꺼지며 반복적으로 움직입니다.

유튜브 시연 영상 https://youtu.be/GSWM3ugUTAc


---

### 🔌 GPIO 연결 예시

실물 예시 사진 ![KakaoTalk_20250408_103805833_01](https://github.com/user-attachments/assets/6347278f-6821-464c-bee6-e347d14aa235)


![화면 캡처 2025-04-08 112656](https://github.com/user-attachments/assets/35d7466e-ef95-42b2-84bb-06b0aba9575f)


| GPIO 번호 | 연결된 부품 |
|-----------|--------------|
| GPIO 4    | LED 1        |
| GPIO 5    | LED 2        |
| GPIO 6    | LED 3        |
| GPIO 7    | LED 4        |

※ 해당 핀은 임의로 지정된 것이며 코드를 수정하면 다른 핀을 사용할 수 있습니다.

---

## 💻 코드 설명

### 🔹 핀 초기화
```bash
for a in {4..7}; do
    pinctrl set $a op
    pinctrl set $a dl
done
```
- GPIO 4~7번을 **출력 모드(op)** 로 설정
- 초기값은 **Low(dl)** 로 설정하여 LED를 모두 끔

---

### 🔹 메인 루프 – 도미노 방식 점등
```bash
while true; do
    for p in {4..7}; do
        pinctrl set $p dh
        sleep 1
        pinctrl set $p dl
    done
done
```

- 무한 루프 안에서 4개의 GPIO 핀을 순차적으로 점등
- 각 LED는 1초 동안 켜지고 꺼진 뒤 다음 LED로 넘어감
- 결과적으로 LED가 **도미노처럼 순차적으로 깜빡임**

---
