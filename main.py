#установка библиотек (список в README.md)
import cv2
import mediapipe as mp
import serial
import time

# Инициализация последовательного соединения (настройте CDM-порт и скорость передачи)
ser = serial.Serial('COM№', 9600)  # Замените на ваш порт
time.sleep(2)  # Ожидание инициализации последовательного порта

# Инициализация решения для распознавания рук
handSolution = mp.solutions.hands
hands = handSolution.Hands()
mp_drawing = mp.solutions.drawing_utils


#разрешение 1280x720
desired_width = 1280 
desired_height = 720

# Инициализация камеры
videoCap = cv2.VideoCapture(0)
videoCap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
videoCap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)

actual_width = int(videoCap.get(cv2.CAP_PROP_FRAME_WIDTH))
actual_height = int(videoCap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"Разрешение: {actual_width}x{actual_height}")

# Переменная для хранения текущего цвета
current_color = "NONE"

# Главный цикл обработки
while True:
    # Чтение кадра с камеры и его отражение
    success, img = videoCap.read()
    img = cv2.flip(img, 1)
    if not success:
        break

    h, w, _ = img.shape  # Получение размеров изображения

    # Определение размеров цветных прямоугольников
    rectangle_width = 200
    rectangle_height = 200

    # Отрисовка красного прямоугольника в левом верхнем углу
    cv2.rectangle(img, (0, 0), (rectangle_width, rectangle_height), (0, 0, 255), -1)
    cv2.putText(img, 'RED', (60, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

    # Отрисовка зеленого прямоугольника в правом верхнем углу
    cv2.rectangle(img, (w - rectangle_width, 0), (w, rectangle_height), (0, 255, 0), -1)
    cv2.putText(img, 'GREEN', (w - 130, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

    # Отрисовка синего прямоугольника в левом нижнем углу
    cv2.rectangle(img, (0, h - rectangle_height), (rectangle_width, h), (255, 0, 0), -1)
    cv2.putText(img, 'BLUE', (30, h - 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Обработка ключевых точек руки
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    recHands = hands.process(img_rgb)

    if recHands.multi_hand_landmarks:
        for hand_landmarks in recHands.multi_hand_landmarks:
            # Получение координат кончика указательного пальца (точка 8)
            x = int(hand_landmarks.landmark[8].x * w)
            y = int(hand_landmarks.landmark[8].y * h)

            # Инициализация значений RGB
            red, green, blue = 0, 0, 0

            # Проверка нахождения руки в красной зоне
            if 0 <= x <= rectangle_width and 0 <= y <= rectangle_height:
                red = 255
                current_color = "RED"
                rgb_message = f"{red},{green},{blue}\n"
                ser.write(rgb_message.encode())
                print("Обнаружена красная зона")

            # Проверка нахождения руки в зеленой зоне
            elif (w - rectangle_width) <= x <= w and 0 <= y <= rectangle_height:
                green = 255
                current_color = "GREEN"
                rgb_message = f"{red},{green},{blue}\n"
                ser.write(rgb_message.encode())
                print("Обнаружена зеленая зона")

            # Проверка нахождения руки в синей зоне
            elif 0 <= x <= rectangle_width and (h - rectangle_height) <= y <= h:
                blue = 255
                current_color = "BLUE"
                rgb_message = f"{red},{green},{blue}\n"
                ser.write(rgb_message.encode())
                print("Обнаружена синяя зона")

            # Отрисовка ключевых точек руки
            mp_drawing.draw_landmarks(
                img,
                hand_landmarks,
                handSolution.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=3, circle_radius=0),
                                mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=3)
            )

    # Отображение текста о текущем цвете в центре экрана
    center_x = w // 2
    center_y = h // 2
    cv2.putText(img, f"Detected Color: {current_color}", (center_x - 300, center_y - 300), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3, cv2.LINE_AA)

    # Отображение видеокадра
    cv2.imshow("CamOutput", img)

    # Выход по нажатию 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов камеры и закрытие окон
videoCap.release()
cv2.destroyAllWindows()
ser.close()
