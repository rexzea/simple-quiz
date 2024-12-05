import tkinter as tk
from tkinter import messagebox, ttk  # Pastikan ttk diimpor dari tkinter
import random

# Data soal
questions = [
    {"category": "Sejarah", "question": "Siapa presiden pertama Indonesia?", 
     "options": ["Sukarno", "Hatta", "Megawati", "Prabowo"], "answer": "Sukarno"},
    {"category": "Sains", "question": "Apa simbol kimia untuk air?", 
     "options": ["H2O", "O2", "H2", "CO2"], "answer": "H2O"},
    {"category": "Matematika", "question": "Berapa hasil dari 6 x 5?", 
     "options": ["65", "30", "70", "40"], "answer": "30"},
    {"category": "Sains", "question": "Planet yang memiliki cincin di tata surya?", 
     "options": ["Bumi", "Jupiter", "Mars", "Saturnus"], "answer": "Saturnus"},
    {"category": "Sejarah", "question": "Kapan Indonesia merdeka?", 
     "options": ["1945", "1940", "1950", "1965"], "answer": "1945"},
]

# mengacak soal
random.shuffle(questions)

# variable global
current_question = 0
score = 0

# memproses jawaban
def check_answer(selected_option):
    global current_question, score
    
    correct_answer = questions[current_question]["answer"]
    if selected_option == correct_answer:
        messagebox.showinfo("Hasil", "Benar!")
        score += 1
    else:
        messagebox.showinfo("Hasil", f"Salah! Jawaban yang benar adalah {correct_answer}.")
    
    current_question += 1
    if current_question < len(questions):
        load_question()
    else:
        save_score()
        show_results()

# memuat soal berikutnya
def load_question():
    global current_question
    
    question_data = questions[current_question]
    question_label.config(text=f"{current_question + 1}. {question_data['question']}")
    option1_button.config(text=question_data["options"][0], command=lambda: check_answer(question_data["options"][0]))
    option2_button.config(text=question_data["options"][1], command=lambda: check_answer(question_data["options"][1]))
    option3_button.config(text=question_data["options"][2], command=lambda: check_answer(question_data["options"][2]))
    option4_button.config(text=question_data["options"][3], command=lambda: check_answer(question_data["options"][3]))
    progress_var.set((current_question + 1) / len(questions) * 100)

# menyimpan skor ke file leaderboard
def save_score():
    with open("leaderboard.txt", "a") as file:
        file.write(f"Skor: {score}/{len(questions)}\n")

# menampilkan hasil akhir
def show_results():
    messagebox.showinfo("Hasil Akhir", f"Skor Anda: {score}/{len(questions)}")
    root.destroy()

# melihat leaderboard
def view_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            leaderboard = file.read()
    except FileNotFoundError:
        leaderboard = "Maaf yaa, Belum ada skor yang disimpan."
    
    messagebox.showinfo("Leaderboard", leaderboard)

# GUI
root = tk.Tk()
root.title("Kuis Rexzea")

# soal
question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, justify="center")
question_label.pack(pady=20)

# tombol opsi
option1_button = tk.Button(root, text="", font=("Arial", 12), width=30, command=None)
option1_button.pack(pady=5)
option2_button = tk.Button(root, text="", font=("Arial", 12), width=30, command=None)
option2_button.pack(pady=5)
option3_button = tk.Button(root, text="", font=("Arial", 12), width=30, command=None)
option3_button.pack(pady=5)
option4_button = tk.Button(root, text="", font=("Arial", 12), width=30, command=None)
option4_button.pack(pady=5)

# progres bar
progress_var = tk.DoubleVar()
progress_bar = tk.ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(pady=10, fill="x")

# tombol leaderboard
leaderboard_button = tk.Button(root, text="Lihat riwayat", font=("Arial", 12), command=view_leaderboard)
leaderboard_button.pack(pady=10)

# Memunculkan soal pertama
load_question()

# GUI
root.mainloop()
