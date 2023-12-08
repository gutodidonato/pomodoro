from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repeticoes = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def resetar():
    global repeticoes, timer
    repeticoes = 1
    window.after_cancel(timer)
    joinha.config(text="")
    iniciar()


# ---------------------------- TIMER MECHANISM ------------------------------- #


def mostrar_tempo(tempo):
    tempo_minutos = math.floor(tempo / 60)
    tempo_segundos = tempo % 60
    if tempo_segundos < 10:
        tempo_segundos = f"0{tempo_segundos}"
    elif tempo_minutos < 10:
        tempo_minutos = f"0{tempo_minutos}"
    return f"{tempo_minutos}:{tempo_segundos}"


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def iniciar():
    global repeticoes
    text.config(text="TRABALHE")
    contagem(WORK_MIN * 60)
    repeticoes += 1


def verificar_horario():
    if repeticoes % 8 == 1:
        iniciar()
    elif repeticoes % 8 == 0:
        iniciar_descanso_longo()
    else:
        iniciar_descanso_curto()


def iniciar_descanso_curto():
    global repeticoes
    text.config(text="DESCANSO CURTO")
    joinha.config(text=+"✓")
    contagem(SHORT_BREAK_MIN * 60)
    repeticoes += 1


def iniciar_descanso_longo():
    global repeticoes
    joinha.config(text="")
    text.config(text="DESCANSO LONGO")
    contagem(LONG_BREAK_MIN * 60)
    repeticoes += 1


def contagem(count):
    global timer
    if count > 0:
        canvas.itemconfig(time_text, text=mostrar_tempo(count))
        window.update()
        timer = window.after(1000, contagem, count - 1)
    else:
        verificar_horario()


# ---------------------------- UI SETUP ------------------------------- #
"""tela"""
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)
""""""
"""canvas"""
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomate_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomate_img)
time_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.config()
canvas.grid(row=1, column=1)


""""""
text = Label()
text.config(
    fg=GREEN,
    font=(FONT_NAME, 36, "bold"),
    text="Pomodoro",
    highlightthickness=0,
    bg=YELLOW,
)
text.grid(row=0, column=1)
""""""


"""Joinha"""
joinha = Label()
joinha.config(
    fg=GREEN, font=(FONT_NAME, 20, "bold"), text="", highlightthickness=0, bg=YELLOW
)
joinha.grid(row=3, column=1)
""""""


"""Start"""
start = Button()
start.config(text="Start", command=iniciar)
start.grid(row=2, column=0)
""""""


"""Reset"""
reset = Button()
reset.config(text="Reset", command=resetar)
reset.grid(row=2, column=2)
""""""
print("iniciando pomodoro...")
window.mainloop()
""""""
