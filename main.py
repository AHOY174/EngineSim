import tkinter as tk
from engine_integration import engine, pedal, gas_pump, gas_tank

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.pressure = 0.0
        self.duration = 0
        self.rpms = 0
        self.running = False
        self.rpms_label = tk.Label(root, text="0")
        self.label = tk.Label(root, text="0")
        self.d_label = tk.Label(root, text="0")
        self.label.pack()
        self.d_label.pack()
        self.rpms_label.pack()

        self.button = tk.Button(root, text="GAS PEDAL", width=20, height=5)
        self.button.pack(pady=20)

        self.button.bind('<ButtonPress-1>', self.press)
        self.button.bind('<ButtonRelease-1>', self.release)

        self.pressure_job = None
        self.duration_job = None

    def press(self, event):
        self.running = True
        self.duration = 0
        self.rpms = 0
        self.update_pressure()
        self.update_duration()
        self.use_gas()

    def release(self, event):
        self.running = False
        if self.pressure_job is not None:
            self.root.after_cancel(self.pressure_job)
            self.pressure_job = None
        if self.duration_job is not None:
            self.root.after_cancel(self.duration_job)
            self.duration_job = None
        self.decrease_pressure()

    def update_pressure(self):
        if self.running:
            if self.pressure < 100:
                self.pressure += 1
                self.label.config(text=str(self.pressure))
                self.root.after(10, self.update_pressure)  # Update every 10 ms
                
    def update_duration(self):
        if self.running:
            self.duration += 1
            self.d_label.config(text=str(self.duration))
            self.duration_job = self.root.after(1000, self.update_duration) # Update every 1s
    
    def decrease_pressure(self):
        if not self.running and self.pressure > 0:
            self.pressure -= 1
            self.label.config(text=str(self.pressure))
            self.pressure_job = self.root.after(10, self.decrease_pressure)   # Update every 10 ms

    def use_gas(self):
        how_hard=0.01*self.pressure
        seconds = self.duration
        gas_portion = pedal.press(how_hard=how_hard, seconds=seconds)
        rotations = gas_pump.apply_gas(gas_portion=gas_portion, seconds=seconds)
        rpms = rotations
        self.rpms_label.config(text=str(rpms))

    
if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()
