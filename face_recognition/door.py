import cv2
import numpy as np
from deepface import DeepFace
import os
import json
from datetime import datetime
import time

class FaceRecognitionSystem:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        self.db_path = "face_db"
        self.registered_faces = {}
        
        if not os.path.exists(self.db_path):
            os.makedirs(self.db_path)
        
        self.load_registered_faces()
    
    def initialize_camera(self):
        """카메라 초기화 및 연결 확인"""
        max_attempts = 3
        for attempt in range(max_attempts):
            cap = cv2.VideoCapture(0)
            if cap.isOpened():
                # 카메라 설정
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                # 테스트 프레임 읽기
                ret, frame = cap.read()
                if ret:
                    return cap
            cap.release()
            time.sleep(1)
        raise Exception("카메라를 초기화할 수 없습니다.")

    def load_registered_faces(self):
        info_file = os.path.join(self.db_path, "face_info.json")
        if os.path.exists(info_file):
            with open(info_file, 'r') as f:
                self.registered_faces = json.load(f)
    
    def save_registered_faces(self):
        info_file = os.path.join(self.db_path, "face_info.json")
        with open(info_file, 'w') as f:
            json.dump(self.registered_faces, f)
    
    def register_new_face(self, name):
        """새로운 얼굴 등록"""
        try:
            cap = self.initialize_camera()
            frame_count = 0
            
            while True:
                try:
                    ret, frame = cap.read()
                    if not ret:
                        print("프레임을 읽을 수 없습니다. 카메라를 다시 초기화합니다.")
                        cap.release()
                        cap = self.initialize_camera()
                        continue
                    
                    # 프레임 카운터 증가
                    frame_count += 1
                    if frame_count % 2 != 0:  # 프레임 건너뛰기
                        continue
                    
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = self.face_cascade.detectMultiScale(gray, 1.1, 5)
                    
                    for (x, y, w, h) in faces:
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    
                    cv2.imshow('Register New Face (Press s to save)', frame)
                    
                    key = cv2.waitKey(1)
                    if key & 0xFF == ord('s'):
                        if len(faces) == 1:
                            face_path = os.path.join(self.db_path, f"{name}.jpg")
                            cv2.imwrite(face_path, frame)
                            self.registered_faces[name] = {
                                "path": face_path,
                                "register_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            }
                            self.save_registered_faces()
                            print(f"{name}의 얼굴이 성공적으로 등록되었습니다.")
                            break
                        else:
                            print("얼굴이 하나만 보이도록 해주세요.")
                    elif key & 0xFF == ord('q'):
                        break
                        
                except Exception as e:
                    print(f"프레임 처리 중 오류 발생: {e}")
                    time.sleep(0.5)
                    
        except Exception as e:
            print(f"카메라 초기화 중 오류 발생: {e}")
        finally:
            if 'cap' in locals():
                cap.release()
            cv2.destroyAllWindows()
    
    def recognize_faces(self, frame):
        """프레임에서 얼굴 인식"""
        results = []
        
        try:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 5)
            
            for (x, y, w, h) in faces:
                face_img = frame[y:y+h, x:x+w]
                
                try:
                    for name, info in self.registered_faces.items():
                        if os.path.exists(info["path"]):
                            result = DeepFace.verify(
                                face_img,
                                info["path"],
                                model_name="VGG-Face",
                                enforce_detection=False
                            )
                            
                            if result["verified"]:
                                results.append({
                                    "bbox": (x, y, w, h),
                                    "name": name,
                                    "confidence": result["distance"]
                                })
                                break
                    else:
                        results.append({
                            "bbox": (x, y, w, h),
                            "name": "Unknown",
                            "confidence": 0
                        })
                except Exception as e:
                    print(f"얼굴 비교 중 오류 발생: {e}")
                    results.append({
                        "bbox": (x, y, w, h),
                        "name": "Error",
                        "confidence": 0
                    })
                    
        except Exception as e:
            print(f"얼굴 감지 중 오류 발생: {e}")
        
        return results

def main():
    face_system = FaceRecognitionSystem()
    
    try:
        cap = face_system.initialize_camera()
        print("카메라가 성공적으로 초기화되었습니다.")
        print("'r': 새 얼굴 등록, 'q': 종료")
        
        while True:
            try:
                ret, frame = cap.read()
                if not ret:
                    print("프레임을 읽을 수 없습니다. 재시도 중...")
                    time.sleep(0.5)
                    continue
                
                results = face_system.recognize_faces(frame)
                
                for result in results:
                    x, y, w, h = result["bbox"]
                    name = result["name"]
                    color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
                    
                    cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
                    cv2.putText(frame, name, (x, y-10),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
                
                cv2.imshow('Face Recognition', frame)
                
                key = cv2.waitKey(1)
                if key & 0xFF == ord('q'):
                    break
                elif key & 0xFF == ord('r'):
                    name = input("등록할 이름을 입력하세요: ")
                    face_system.register_new_face(name)
                    
            except Exception as e:
                print(f"메인 루프 오류: {e}")
                time.sleep(0.5)
                
    except Exception as e:
        print(f"프로그램 실행 중 오류 발생: {e}")
        
    finally:
        if 'cap' in locals():
            cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()