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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.config(padx=100,pady=50,bg=YELLOW)

#canvas

canvas = Canvas(width=200, height=224, bg=YELLOW,highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)

#label

Timer_word = Label(text="TIMER",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)
Timer_word.grid(column=1,row=0)

check_mark = Label(text= "✔" ,font=(FONT_NAME,30,"bold"),fg=GREEN,bg=YELLOW)
check_mark.grid(column=1,row=3)

#button

start_button = Button(text="START",font=(FONT_NAME,20,"bold"))
start_button.grid(column=0,row=2)

reset_button = Button(text="RESET",font=(FONT_NAME,20,"bold"))
reset_button.grid(column=2,row=2)
window.mainloop()