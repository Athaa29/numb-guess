import tkinter as tk
import customtkinter as ctk
import random

ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("green") 

def start_game():
    global target_number, attempts
    target_number = random.randint(1, 100)
    attempts = 0
    guess_entry.configure(state="normal")
    guess_button.configure(state="normal")
    guess_entry.delete(0, tk.END)
    update_status("Permainan dimulai! Masukkan angka 1-100", "gray")
    attempts_label.configure(text="🎯 Percobaan: 0")

def check_guess():
    global attempts
    guess = guess_entry.get()
    if not guess.isdigit():
        update_status("⚠️ Masukkan angka valid!", "red")
        return

    guess = int(guess)
    if guess < 1 or guess > 100:
        update_status("⚠️ Angka harus antara 1 dan 100!", "red")
        return

    attempts += 1
    attempts_label.configure(text=f"🎯 Percobaan: {attempts}")

    if guess < target_number:
        update_status("🔽 Terlalu rendah!", "orange")
    elif guess > target_number:
        update_status("🔼 Terlalu tinggi!", "orange")
    else:
        update_status(f"✅ Tepat! Lu menang dalam {attempts} percobaan!", "green")
        guess_entry.configure(state="disabled")
        guess_button.configure(state="disabled")

def update_status(message, color):
    result_label.configure(text=message, text_color=color)

def toggle_mode(choice):
    ctk.set_appearance_mode(choice)

app = ctk.CTk()
app.title("🎮 Game Tebak Angka")
app.geometry("480x500")
app.resizable(False, False)

main_frame = ctk.CTkFrame(app, corner_radius=20)
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

title = ctk.CTkLabel(main_frame, text="Tebak Angka 1 - 100", font=("Segoe UI", 26, "bold"))
title.pack(pady=(20, 10))

result_label = ctk.CTkLabel(main_frame, text="Klik 'Mulai' untuk bermain", font=("Segoe UI", 16))
result_label.pack(pady=10)

attempts_label = ctk.CTkLabel(main_frame, text="🎯 Percobaan: 0", font=("Segoe UI", 14))
attempts_label.pack(pady=5)

guess_entry = ctk.CTkEntry(main_frame, placeholder_text="Masukkan tebakan Anda", font=("Segoe UI", 16), width=220)
guess_entry.pack(pady=15)

guess_button = ctk.CTkButton(main_frame, text="🚀 Tebak!", font=("Segoe UI", 16), command=check_guess, state="disabled", fg_color="#22bb33", hover_color="#1a9940")
guess_button.pack(pady=10)

start_button = ctk.CTkButton(main_frame, text="🔄 Mulai Permainan", font=("Segoe UI", 16), command=start_game)
start_button.pack(pady=10)

mode_label = ctk.CTkLabel(main_frame, text="🌙 Mode Tampilan:", font=("Segoe UI", 13))
mode_label.pack(pady=(20, 5))

appearance_mode = ctk.StringVar(value="System")
mode_menu = ctk.CTkOptionMenu(main_frame, variable=appearance_mode, values=["System", "Light", "Dark"], command=toggle_mode)
mode_menu.pack()

target_number = 0
attempts = 0

app.mainloop()
