import tkinter as tk
from tkinter import ttk, messagebox
import serial
import time

class ArduinoLED:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Arduino LED Control")
        self.window.geometry("400x500")
        
        # System state
        self.is_on = False
        self.blue_value = 0
        self.red_value = 0
        
        try:
            self.arduino = serial.Serial('COM5', 9600, timeout=1)
            time.sleep(2)
        except:
            messagebox.showerror("Error", "Arduino 연결 실패!")
            self.arduino = None

        self.create_widgets()

    def create_widgets(self):
        # Status Label
        self.status_label = ttk.Label(self.window, text="Status: OFF")
        self.status_label.pack(pady=20)

        # ON/OFF Buttons
        button_frame = ttk.Frame(self.window)
        button_frame.pack(pady=20)
        
        self.on_btn = ttk.Button(button_frame, text="ON", command=self.turn_on)
        self.on_btn.pack(side='left', padx=10)
        
        self.off_btn = ttk.Button(button_frame, text="OFF", command=self.turn_off)
        self.off_btn.pack(side='left', padx=10)

        # Blue LED Control
        blue_frame = ttk.Frame(self.window)
        blue_frame.pack(fill='x', padx=20, pady=10)
        ttk.Label(blue_frame, text="Blue LED").pack(side='left')
        self.blue_value_label = ttk.Label(blue_frame, text="0")
        self.blue_value_label.pack(side='right')
        
        self.blue_slider = ttk.Scale(
            self.window,
            from_=0,
            to=100,
            orient='horizontal',
            command=self.update_blue
        )
        self.blue_slider.pack(fill='x', padx=20, pady=5)

        # Red LED Control
        red_frame = ttk.Frame(self.window)
        red_frame.pack(fill='x', padx=20, pady=10)
        ttk.Label(red_frame, text="Red LED").pack(side='left')
        self.red_value_label = ttk.Label(red_frame, text="0")
        self.red_value_label.pack(side='right')
        
        self.red_slider = ttk.Scale(
            self.window,
            from_=0,
            to=100,
            orient='horizontal',
            command=self.update_red
        )
        self.red_slider.pack(fill='x', padx=20, pady=5)

    def turn_on(self):
        self.is_on = True
        self.status_label.config(text="Status: ON")
        # 저장된 값으로 LED 상태 복원
        blue_value = self.blue_slider.get()
        red_value = self.red_slider.get()
        if blue_value > 0:
            self.update_blue(blue_value)
        if red_value > 0:
            self.update_red(red_value)

    def turn_off(self):
        # 현재 값 저장
        self.blue_value = self.blue_slider.get()
        self.red_value = self.red_slider.get()
        self.is_on = False
        self.status_label.config(text="Status: OFF")
        if self.arduino:
            self.arduino.write(b'A0')  # 모든 LED 끄기

    def update_blue(self, value):
        if self.arduino and self.is_on:
            value = int(float(value))
            command = f'B{value:03d}'.encode()
            self.arduino.write(command)
            time.sleep(0.1)  # 통신 안정화를 위한 딜레이 추가
        self.blue_value_label.config(text=f"{int(float(value))}")

    def update_red(self, value):
        if self.arduino and self.is_on:
            value = int(float(value))
            command = f'R{value:03d}'.encode()
            self.arduino.write(command)
            time.sleep(0.1)  # 통신 안정화를 위한 딜레이 추가
        self.red_value_label.config(text=f"{int(float(value))}")

    def run(self):
        self.window.mainloop()

    def __del__(self):
        if self.arduino:
            self.arduino.close()

if __name__ == "__main__":
    app = ArduinoLED()
    app.run()