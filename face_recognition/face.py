import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# 얼굴 인식용 Haar Cascade 로드
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 웹캠 초기화
cap = cv2.VideoCapture(0)

def draw_text(img, text, position, font_size=30, font_color=(255, 255, 255)):
    # Convert the image to RGB (OpenCV uses BGR by default)
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)
    # Use a truetype font
    font = ImageFont.truetype("malgun.ttf", font_size)
    draw.text(position, text, font=font, fill=font_color)
    # Convert the image back to BGR
    img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
    return img

while True:
    # 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        break

    # 그레이스케일로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴 검출
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 사람 수 출력
    if len(faces) == 0:
        frame = draw_text(frame, "사람없음", (50, 50), font_size=30, font_color=(255, 255, 255))
    else:
        frame = draw_text(frame, f"{len(faces)}명 있음", (50, 50), font_size=30, font_color=(255, 255, 255))

    # 얼굴에 사각형 그리기
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # 결과 프레임 표시
    cv2.imshow('Face Detection', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 웹캠 해제 및 창 닫기
cap.release()
cv2.destroyAllWindows()