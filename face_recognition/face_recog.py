import cv2
from deepface import DeepFace
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

class FamilyFaceRecognition:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.known_faces = {}
        self.save_folder = "family_faces"
        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)
        self.load_known_faces()

    def load_known_faces(self):
        for filename in os.listdir(self.save_folder):
            if filename.endswith(".jpg"):
                name = os.path.splitext(filename)[0]
                img_path = os.path.join(self.save_folder, filename)
                self.known_faces[name] = DeepFace.represent(img_path, model_name='VGG-Face', enforce_detection=False)

    def draw_text(self, frame, text, position):
        img_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img_pil)
        
        try:
            font = ImageFont.truetype("malgun.ttf", 30)
        except:
            font = ImageFont.load_default()
            
        draw.text(position, text, font=font, fill=(255, 255, 255))
        return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

    def recognize_faces(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            try:
                result = DeepFace.find(frame, db_path=self.save_folder, enforce_detection=False)
                if result:
                    name = result[0]['identity'].split('/')[-1].split('.')[0]
                    text = f"인식된 사람: {name}"
                else:
                    text = "인식되지 않은 사람"
                frame = self.draw_text(frame, text, (10, 50))
                
            except Exception as e:
                print(f"Error: {str(e)}")
                pass

            cv2.imshow('Face Recognition', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def save_face(self, name):
        ret, frame = self.cap.read()
        if ret:
            filename = os.path.join(self.save_folder, f"{name}.jpg")
            cv2.imwrite(filename, frame)
            print(f"Saved {name}'s face to {filename}")
            self.known_faces[name] = DeepFace.represent(filename, model_name='VGG-Face', enforce_detection=False)

    def run(self):
        while True:
            print("모드를 선택하세요: 1 - 얼굴 인식 모드, 2 - 얼굴 저장 모드")
            mode = input("모드 선택: ")

            if mode == '1':
                print("얼굴 인식 모드")
                self.recognize_faces()
            elif mode == '2':
                name = input("이름을 입력하세요: ")
                print(f"{name}의 얼굴 저장 모드")
                self.save_face(name)
            elif mode == 'q':
                break
            else:
                print("잘못된 입력입니다. 다시 시도하세요.")

if __name__ == "__main__":
    app = FamilyFaceRecognition()
    app.run()