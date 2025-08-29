import tkinter as tk
from tkinter import ttk, messagebox
import serial
import time

class DoorLock:
    def __init__(self):
        # GUI 설정
        self.window = tk.Tk()
        self.window.title("Door Lock System")
        self.window.geometry("300x400")
        
        # 시스템 변수
        self.password = "3456#"
        self.current_input = ""
        
        # 아두이노 연결
        try:
            self.arduino = serial.Serial('COM10', 9600, timeout=1)
            time.sleep(2)
        except:
            messagebox.showerror("Error", "Arduino 연결 실패!")
            self.arduino = None

        self.create_widgets()

    def create_widgets(self):
        # 입력 디스플레이
        self.display = ttk.Entry(
            self.window, 
            justify='center',
            font=('Arial', 24)
        )
        self.display.pack(pady=20, padx=20, fill='x')

        # 상태 표시
        self.status_label = ttk.Label(
            self.window,
            text="비밀번호를 입력하세요",
            font=('Arial', 14)
        )
        self.status_label.pack(pady=20)

    def check_password(self):
        if self.current_input == self.password:
            self.status_label.config(
                text="비밀번호 일치",
                foreground="green"
            )
        else:
            self.status_label.config(
                text="비밀번호 불일치",
                foreground="red"
            )
        self.window.after(2000, self.reset_input)

    def reset_input(self):
        self.current_input = ""
        self.display.delete(0, tk.END)
        self.status_label.config(
            text="비밀번호를 입력하세요",
            foreground="black"
        )

    def process_serial(self):
        if self.arduino and self.arduino.in_waiting:
            try:
                value = self.arduino.readline().decode().strip()
                if value:
                    self.current_input += value
                    self.display.delete(0, tk.END)
                    self.display.insert(0, self.current_input)
                    
                    if value == '#':
                        self.check_password()
                    elif len(self.current_input) > 8:
                        self.reset_input()
            except:
                pass
        self.window.after(100, self.process_serial)

    def run(self):
        self.process_serial()
        self.window.mainloop()

    def __del__(self):
        if self.arduino:
            self.arduino.close()

if __name__ == "__main__":
    app = DoorLock()
    app.run()