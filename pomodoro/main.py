from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_obj = None

# ---------------------------- TIMER RESET ------------------------------- # 

def time_reset():
    global reps
    global timer_obj
    win.after_cancel(id=timer_obj)
    reps = 0
    canvas.itemconfig(tagOrId=text_canvas, text= "00:00")
    timer.config(text="Timer",fg=GREEN)
    tickM.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    tick = "✔"
    print = ""
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer.config(text="Long Break!!",fg=RED)
        count_down(long_sec)
    elif reps % 2 == 0:
        timer.config(text="Short Break!!",fg=PINK)
        count_down(short_sec)
    else:
        timer.config(text= "Time to work!!",fg=GREEN)
        count_down(work_sec)
    for _ in range(reps//2):
        print += tick
    tickM.config(text=print)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(tagOrId= text_canvas,text=f"{count_min}:{count_sec}")
    if(count>0):
        global timer_obj
        timer_obj = win.after(1000,count_down,count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

win = Tk()
win.title("Pomodora")
win.config(padx=180,pady=50,bg=YELLOW)



canvas = Canvas(width=288,height=224,bg= YELLOW,highlightthickness=0)#widget to draw over
tom_png = PhotoImage(file="pomodoro/tomato.png")#reads the file
canvas.create_image(144,110,image=tom_png)
text_canvas = canvas.create_text(144,120,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))




timer = Label(text="Timer",font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)

timer.grid(column=1,row=0)
canvas.grid(column=1,row=1)

start = Button(text="Start", highlightthickness=0,width=10)
start.grid(column=0,row=2)
start.config(command=start_timer)


tick = "✔"
tickM = Label(font=(FONT_NAME,20,"bold"),fg=GREEN,bg=YELLOW)
tickM.grid(column=1,row=3)


reset = Button(text="Reset", highlightthickness=0,width=10)
reset.grid(column=2,row=2)
reset.config(command=time_reset)


win.mainloop()

