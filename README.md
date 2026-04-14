# 🎯 GestureToColorSerial

**GestureToColorSerial** is a Python application that lets you control RGB color output using hand gestures. It utilizes computer vision (MediaPipe) for hand tracking and sends color data over a serial connection — for example, to an Arduino.

## 📷 How It Works

The screen displays three colored zones:

- 🔴 Top-left corner — **RED**
- 🟢 Top-right corner — **GREEN**
- 🔵 Bottom-left corner — **BLUE**
 
When your index finger enters one of these zones, the program sends a corresponding RGB signal (e.g., `255,0,0`) via the serial port to an external device.

## 🧠 Technologies Used

- [OpenCV](https://opencv.org/) — video capture and image processing
- [MediaPipe](https://mediapipe.dev/) — real-time hand tracking
- [PySerial](https://pythonhosted.org/pyserial/) — serial communication
- Python 3

## 🛠️ Installation

```bash
pip install opencv-python mediapipe pyserial
```
🔌 Optional: Arduino Connection
```
// Определение пинов, к которым подключены выводы RGB-светодиода
const int redPin = 9;   // Красный канал подключен к пину 9
const int greenPin = 10;  // Зеленый канал подключен к пину 10
const int bluePin = 12;  // Синий канал подключен к пину 12

void setup() {
  // Установка пинов как выходов
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop() {
  // Пример: плавное изменение цвета от красного к зеленому к синему
  for (int i = 0; i < 256; i++) {
    setColor(i, 255 - i, 0);  // Красный -> Желтый
    delay(5);
  }

  for (int i = 0; i < 256; i++) {
    setColor(0, i, 255 - i);  // Зеленый -> Голубой
    delay(5);
  }

  for (int i = 0; i < 256; i++) {
    setColor(255 - i, 0, i);  // Синий -> Пурпурный
    delay(5);
  }
}

// Функция для установки цвета RGB-светодиода
void setColor(int red, int green, int blue) {
  // Отправка значений PWM на соответствующие пины
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
}
```

📄 License
MIT — free to use and modify.


Co-authored-by: SdvSeven <ssdvseven@gmail.com>
