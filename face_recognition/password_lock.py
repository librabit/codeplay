import tkinter as tk
from tkinter import ttk, messagebox
import serial
import time

class DoorLock:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Door Lock System")
        self.window.geometry("300x400")
        
        # Password settings
        self.password = "1234"
        self.current_input = ""
        
        # Arduino connection
        try:
            self.arduino = serial.Serial('COM5', 9600, timeout=1)
            time.sleep(2)
        except:
            messagebox.showerror("Error", "Arduino 연결 실패!")
            self.arduino = None

        self.create_widgets()

    def create_widgets(self):
        # Password display
        self.display = ttk.Entry(self.window, justify='center', font=('Arial', 20))
        self.display.pack(pady=20, padx=20, fill='x')

        # Status display
        self.status_label = ttk.Label(
            self.window, 
            text="대기중...", 
            font=('Arial', 12),
            justify='center'
        )
        self.status_label.pack(pady=10)

        # Keypad frame
        keypad = ttk.Frame(self.window)
        keypad.pack(pady=20)

        # Keypad buttons
        buttons = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '*', '0', '#'
        ]

        row = 0
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.button_click(x)
            ttk.Button(keypad, text=button, command=cmd, width=8).grid(
                row=row, column=col, padx=5, pady=5
            )
            col += 1
            if col > 2:
                col = 0
                row += 1

    def button_click(self, value):
        if value == '*':  # Clear
            self.current_input = ""
        elif value == '#':  # Enter
            self.check_password()
        else:  # Numbers
            if len(self.current_input) < 8:  # Max 8 digits
                self.current_input += value
        
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_input)

    def check_password(self):
        if len(self.current_input) >= 4 and self.current_input == self.password:
            self.status_label.config(text="비밀번호가 확인되었습니다.")
            self.unlock_door()
        else:
            self.status_label.config(text="잘못된 비밀번호입니다.")
            self.window.after(1000, lambda: self.status_label.config(text="대기중..."))
        
        self.current_input = ""
        self.display.delete(0, tk.END)

    def unlock_door(self):
        if self.arduino:
            self.arduino.write(b'1')  # 180도로 이동
            self.status_label.config(text="문 열림")
            self.window.after(3000, self.lock_door)


    def lock_door(self):
        if self.arduino:
            self.arduino.write(b'0')  # 0도로 복귀
            self.status_label.config(text="문 잠김")
            self.window.after(1000, lambda: self.status_label.config(text="대기중..."))

    def run(self):
        self.window.mainloop()

    def __del__(self):
        if self.arduino:
            self.arduino.close()

if __name__ == "__main__":
    app = DoorLock()
    app.run()