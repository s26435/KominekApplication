import tkinter as tk
import requests

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Symulacja Kominka")
        self.geometry("800x500")

        self.temperature_label = tk.Label(self, text="Temperature:")
        self.temperature_label.pack()

        self.mode_label = tk.Label(self, text="Mode:")
        self.mode_label.pack()

        self.status_label = tk.Label(self, text="Status:")
        self.status_label.pack()

        self.color_label = tk.Label(self, text="Color:")
        self.color_label.pack()

        self.refresh_data()

    def refresh_data(self):
        try:
            response = requests.get("http://127.0.0.1:5000/info/1")
            data = response.json()

            if "error" in data:
                self.temperature_label.config(text="Kominek nie istnieje")
                self.mode_label.config(text="")
                self.status_label.config(text="")
                self.color_label.config(text="")
            else:
                temperature = data["temperature"]
                mode = data["mode"]
                status = "On" if data["status"] else "Off"
                color = data["color"]

                self.temperature_label.config(text=f"Temperature: {temperature}°C")
                self.mode_label.config(text=f"Mode: {mode}")
                self.status_label.config(text=f"Status: {status}")
                self.color_label.config(text=f"Color: {color}")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

        self.after(3000, self.refresh_data)

if __name__ == "__main__":
    app = App()
    app.mainloop()
