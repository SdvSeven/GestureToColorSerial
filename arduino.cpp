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