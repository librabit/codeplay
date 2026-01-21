import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk, ImageFilter, ImageEnhance
import os

class ImageFilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("이미지 필터 애플리케이션")
        self.root.geometry("1000x700")
        
        self.original_image = None
        self.filtered_image = None
        self.display_image = None
        
        self.setup_ui()
    
    def setup_ui(self):
        # 상단 버튼 프레임
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="이미지 열기", command=self.load_image, 
                 bg="#4CAF50", fg="white", font=("Arial", 10, "bold"),
                 padx=10, pady=5).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="저장하기", command=self.save_image,
                 bg="#2196F3", fg="white", font=("Arial", 10, "bold"),
                 padx=10, pady=5).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="원본으로 복구", command=self.reset_image,
                 bg="#FF9800", fg="white", font=("Arial", 10, "bold"),
                 padx=10, pady=5).pack(side=tk.LEFT, padx=5)
        
        # 이미지 표시 프레임
        self.image_frame = tk.Frame(self.root, bg="gray")
        self.image_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.image_label = tk.Label(self.image_frame, text="이미지를 열어주세요", 
                                   bg="gray", fg="white", font=("Arial", 14))
        self.image_label.pack(expand=True)
        
        # 필터 프레임
        filter_frame = tk.LabelFrame(self.root, text="필터 선택", 
                                    font=("Arial", 11, "bold"), padx=10, pady=10)
        filter_frame.pack(pady=10, fill=tk.X, padx=20)
        
        # 필터 버튼들
        filters = [
            ("흐림 효과", self.apply_blur),
            ("윤곽선", self.apply_contour),
            ("엠보스", self.apply_emboss),
            ("경계선 강조", self.apply_edge_enhance),
            ("선명하게", self.apply_sharpen),
            ("부드럽게", self.apply_smooth),
            ("흑백", self.apply_grayscale),
            ("밝게", self.apply_brighten),
            ("어둡게", self.apply_darken),
            ("대비 증가", self.apply_contrast)
        ]
        
        row = 0
        col = 0
        for text, command in filters:
            btn = tk.Button(filter_frame, text=text, command=command,
                          width=12, height=2, bg="#E1E1E1")
            btn.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 4:
                col = 0
                row += 1
    
    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        if file_path:
            self.original_image = Image.open(file_path)
            self.filtered_image = self.original_image.copy()
            self.display_current_image()
    
    def display_current_image(self):
        if self.filtered_image:
            # 이미지 크기 조정 (화면에 맞게)
            display_img = self.filtered_image.copy()
            display_img.thumbnail((800, 500), Image.Resampling.LANCZOS)
            
            self.display_image = ImageTk.PhotoImage(display_img)
            self.image_label.configure(image=self.display_image, text="")
    
    def save_image(self):
        if self.filtered_image:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), 
                          ("All files", "*.*")]
            )
            if file_path:
                self.filtered_image.save(file_path)
                tk.messagebox.showinfo("저장 완료", "이미지가 저장되었습니다!")
    
    def reset_image(self):
        if self.original_image:
            self.filtered_image = self.original_image.copy()
            self.display_current_image()
    
    def apply_blur(self):
        if self.filtered_image:
            self.filtered_image = self.filtered_image.filter(ImageFilter.BLUR)
            self.display_current_image()
    
    def apply_contour(self):
        if self.filtered_image:
            self.filtered_image = self.filtered_image.filter(ImageFilter.CONTOUR)
            self.display_current_image()
    
    def apply_emboss(self):
        if self.filtered_image:
            self.filtered_image = self.filtered_image.filter(ImageFilter.EMBOSS)
            self.display_current_image()
    
    def apply_edge_enhance(self):
        if self.filtered_image:
            self.filtered_image = self.filtered_image.filter(ImageFilter.EDGE_ENHANCE)
            self.display_current_image()
    
    def apply_sharpen(self):
        if self.filtered_image:
            self.filtered_image = self.filtered_image.filter(ImageFilter.SHARPEN)
            self.display_current_image()
    
    def apply_smooth(self):
        if self.filtered_image:
            self.filtered_image = self.filtered_image.filter(ImageFilter.SMOOTH)
            self.display_current_image()
    
    def apply_grayscale(self):
        if self.filtered_image:
            self.filtered_image = self.filtered_image.convert('L').convert('RGB')
            self.display_current_image()
    
    def apply_brighten(self):
        if self.filtered_image:
            enhancer = ImageEnhance.Brightness(self.filtered_image)
            self.filtered_image = enhancer.enhance(1.3)
            self.display_current_image()
    
    def apply_darken(self):
        if self.filtered_image:
            enhancer = ImageEnhance.Brightness(self.filtered_image)
            self.filtered_image = enhancer.enhance(0.7)
            self.display_current_image()
    
    def apply_contrast(self):
        if self.filtered_image:
            enhancer = ImageEnhance.Contrast(self.filtered_image)
            self.filtered_image = enhancer.enhance(1.5)
            self.display_current_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageFilterApp(root)
    root.mainloop()