import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
import datetime
import os
import numpy as np
import time

class SelfieApp:
    def __init__(self, window):
        self.window = window
        self.window.title("연속 촬영 셀피 카메라")
        
        # 저장 폴더 생성
        self.save_folder = "face_recognition//my_selfies"
        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)
        
        # 카메라 초기화
        self.camera = cv2.VideoCapture(0)
        
        # 연속 촬영 이미지 저장용 리스트
        self.captured_images = []
        
        # 메인 프레임
        self.main_frame = ttk.Frame(window, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 카메라 미리보기
        self.preview_label = ttk.Label(self.main_frame)
        self.preview_label.grid(row=0, column=0, columnspan=2)
        
        # 버튼들
        self.capture_btn = ttk.Button(self.main_frame, text="연속 촬영 시작!", command=self.take_photo)
        self.capture_btn.grid(row=1, column=0, pady=5)
        
        # 필터 선택
        self.filter_var = tk.StringVar(value="없음")
        self.filter_combo = ttk.Combobox(self.main_frame, 
                                       textvariable=self.filter_var,
                                       values=["None", "B/W", "Sephia", "Sketch"])
        self.filter_combo.grid(row=1, column=1, pady=5)
        
        # 카운트다운 변수
        self.countdown = 0
        self.counting = False
        
        # 촬영 상태
        self.is_capturing = False
        
        # 타이머 시작
        self.update_preview()
    
    def apply_filter(self, frame):
        filter_name = self.filter_var.get()
        
        if filter_name == "B/W":
            return cv2.cvtColor(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 
                              cv2.COLOR_GRAY2BGR)
        
        elif filter_name == "Sephia":
            sepia_matrix = np.array([
                [0.393, 0.769, 0.189],
                [0.349, 0.686, 0.168],
                [0.272, 0.534, 0.131]
            ])
            sepia_frame = cv2.transform(frame, sepia_matrix)
            sepia_frame[sepia_frame > 255] = 255
            return np.array(sepia_frame, dtype=np.uint8)
        
        elif filter_name == "Sketch":
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            inverted = cv2.bitwise_not(gray)
            blur = cv2.GaussianBlur(inverted, (21, 21), 0)
            inverted_blur = cv2.bitwise_not(blur)
            sketch = cv2.divide(gray, inverted_blur, scale=256.0)
            return cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)
            
        return frame

    def update_preview(self):
        ret, frame = self.camera.read()
        if ret:
            frame = cv2.flip(frame, 1)
            frame = self.apply_filter(frame)
            
            if self.counting:
                cv2.putText(frame, str(self.countdown), 
                          (frame.shape[1]//2, frame.shape[0]//2),
                          cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 4)
            
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(rgb_frame)
            img_tk = ImageTk.PhotoImage(image=pil_img)
            
            self.preview_label.img_tk = img_tk
            self.preview_label.configure(image=img_tk)
        
        self.window.after(3, self.update_preview)
    
    def start_countdown(self):
        self.countdown = 3
        self.counting = True
        self.captured_images = []  # 이미지 리스트 초기화
        self.count_down()
    
    def count_down(self):
        if self.countdown > 0:
            self.countdown -= 1
            self.window.after(1000, self.count_down)
        else:
            self.counting = False
            self.capture_sequence()
    
    def capture_sequence(self):
        self.is_capturing = True
        self.capture_frame()
    
    def capture_frame(self):
        if len(self.captured_images) < 4:
            ret, frame = self.camera.read()
            if ret:
                frame = cv2.flip(frame, 1)
                frame = self.apply_filter(frame)
                self.captured_images.append(frame)
                
                # 촬영 효과음 재생하거나 플래시 효과를 넣을 수 있습니다
                
                if len(self.captured_images) < 4:
                    # 0.2초 후 다음 촬영
                    self.window.after(200, self.capture_frame)
                else:
                    self.create_collage()
        
    def create_collage(self):
        if len(self.captured_images) == 4:
            # 각 이미지 크기 계산
            h, w = self.captured_images[0].shape[:2]
            target_size = (w//2, h//2)
            
            # 2x2 캔버스 생성
            collage = np.zeros((h, w, 3), dtype=np.uint8)
            
            # 이미지 리사이징 및 배치
            positions = [(0,0), (target_size[0],0), 
                        (0,target_size[1]), (target_size[0],target_size[1])]
            
            for img, pos in zip(self.captured_images, positions):
                resized = cv2.resize(img, target_size)
                collage[pos[1]:pos[1]+target_size[1], 
                       pos[0]:pos[0]+target_size[0]] = resized
            
            # 이미지 저장
            filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_collage.jpg")
            filepath = os.path.join(self.save_folder, filename)
            cv2.imwrite(filepath, collage)
            
            # 저장 완료 메시지
            saved_label = ttk.Label(self.main_frame, 
                                  text=f"연속 촬영 완료!\n{filepath}")
            saved_label.grid(row=2, column=0, columnspan=2, pady=5)
            self.window.after(2000, saved_label.destroy)
            
            # 상태 초기화
            self.is_capturing = False
            self.captured_images = []
    
    def take_photo(self):
        if not self.is_capturing:
            self.start_countdown()
    
    def __del__(self):
        self.camera.release()

if __name__ == "__main__":
    root = tk.Tk()
    app = SelfieApp(root)
    root.mainloop()