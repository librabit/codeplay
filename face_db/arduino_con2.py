import tkinter as tk
from tkinter import ttk, messagebox
import serial
import time

class ArduinoControl:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Arduino LED Control")
        self.window.geometry("200x200")
        
        # LED state
        self.is_on = False
        
        # Connect to Arduino
        try:
            self.arduino = serial.Serial('COM6', 9600, timeout=1)
            time.sleep(2)  # Wait for Arduino to reset
        except:
            messagebox.showerror("Error", "Arduino 연결 실패!")
            self.arduino = None

        # Create button that fills window
        self.toggle_btn = ttk.Button(
            self.window,
            text="On/Off",
            command=self.toggle_led,
            style='big.TButton'
        )
        self.toggle_btn.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        # Create custom style for button
        style = ttk.Style()
        style.configure('big.TButton', font=('Arial', 20))

    def toggle_led(self):
        if self.arduino:
            self.is_on = not self.is_on
            if self.is_on:
                self.arduino.write(b'1')
            else:
                self.arduino.write(b'0')

    def run(self):
        self.window.mainloop()

    def __del__(self):
        if self.arduino:
            self.arduino.close()

if __name__ == "__main__":
    app = ArduinoControl()
    app.run()