import requests
import tkinter as tk
from tkinter import ttk, messagebox

def fetch_prayer_times(city, country):
    response = requests.get(f'http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2')
    data = response.json()
    return data['data']['timings']

def gui_fetch_prayer_times():
    city = city_entery.get()
    country = country_entery.get()

    if city and country:
        prayer_timings = fetch_prayer_times(city, country)
        for name, time in prayer_timings.items():
            results.insert(tk.END, f'{name}: {time}')
    else:
        messagebox.showerror("Error","Unable to fetch prayer times. Please enter a valid city and country name.")

app = tk.Tk()
app.title("Prayer times")
frame = ttk.Frame(app, padding="20")
frame.grid(row=0, column=0)

city_label = ttk.Label(frame, text="City:")
city_label.grid(row=0, column=0, pady=5)
city_entery = ttk.Entry(frame, width=20)
city_entery.grid(row=0, column=1, pady=5)

country_label = ttk.Label(frame, text="Country:")
country_label.grid(row=1, column=0, pady=5)
country_entery = ttk.Entry(frame, width=20)
country_entery.grid(row=1, column=1, pady=5)

fetch_button = ttk.Button(frame, text="Fetch prayer times", command=gui_fetch_prayer_times)
fetch_button.grid(row=2, column=0, columnspan=2, pady=10)

results = tk.Listbox(frame, height=11, width = 30)
results.grid(row=3, column=0,columnspan=2,pady=5)

app.mainloop()
