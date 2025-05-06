# 🎯 GestureToColorSerial

**GestureToColorSerial** — Python-приложение для управления цветом (RGB) через жесты руки. Использует компьютерное зрение (MediaPipe) и передачу данных по последовательному порту (Serial), чтобы взаимодействовать, в моем случае, с Arduino.

## 📷 Как это работает

На изображении с веб-камеры отображаются три зоны:

- 🔴 Левая верхняя — **RED**
- 🟢 Правая верхняя — **GREEN**
- 🔵 Левая нижняя — **BLUE**

Когда указательный палец попадает в одну из зон, соответствующий RGB-сигнал (например, `255,0,0`) отправляется через COM-порт на внешнее устройство.

## 🧠 Используемые технологии

- [OpenCV](https://opencv.org/) — захват и обработка видео
- [MediaPipe](https://mediapipe.dev/) — распознавание руки
- [PySerial](https://pythonhosted.org/pyserial/) — работа с COM-портом
- Python 3

## 🛠️ Установка

```bash
pip install opencv-python mediapipe pyserial
```

🔌 Подключение к Arduino (опционально)
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

📄 Лицензия
MIT — свободно используйте и модифицируйте.
