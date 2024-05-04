from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_count_down():
    global reps
    reps += 1
    mark = ""

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title.config(text="Long break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title.config(text="Short break", fg=RED)
        mark += "✓"
        check_mark.config(text=mark)
    else:
        count_down(WORK_MIN * 60)
        title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    global timer

    minutes = count // 60
    seconds = count % 60

    if seconds == 0:
        seconds = "00"
    elif 9 >= seconds > 0:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_count_down()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(bg=YELLOW, padx=100, pady=50)
window.tk.call('tk', 'scaling', 1.4)

title = Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
title.grid(column=1, row=0)

canvas = Canvas(width=220, height=230, bg=YELLOW, borderwidth=0, highlightthickness=0)
pic = PhotoImage(file="tomato.png")
canvas.create_image(110, 115, image=pic)
timer_text = canvas.create_text(110, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_count_down)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN)
check_mark.grid(column=1, row=3)


window.mainloop()
