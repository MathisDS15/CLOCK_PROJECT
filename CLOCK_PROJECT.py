# Mathis DA SILVA
# Clock Project

import tkinter as tk
from math import cos, sin, pi

# Constants
r, r1, r2, r3 = 5, 150, 140, 130
Black, Grey, White, Blue = 'black', 'grey', 'white', 'blue'
AngleH, AngleM = 2 * pi / 12, 2 * pi / 60
Hour, Minute = 9, 37
nb_minute = Hour * 60 + Minute

# Function to draw the clock face
def draw_clock():
    cnv1.delete('all')
    cnv1.create_oval(x - r1, y - r1, x + r1, y + r1, fill=Blue)
    cnv1.create_oval(x - r2, y - r2, x + r2, y + r2, fill=White)
    cnv1.create_oval(x - r3, y - r3, x + r3, y + r3, fill=White, outline=Grey)
    cnv1.create_oval(x - r, y - r, x + r, y + r, fill=Grey)
    for i in range(0, 60):
        angle = 2 * pi * i / 60  # Calculate angle for each minute
        x1 = x + r2 * cos(angle)
        y1 = y + r2 * sin(angle)
        x2 = x + r3 * cos(angle)
        y2 = y + r3 * sin(angle)

        if i % 5 == 0:  # Markers for every 5 minutes
            cnv1.create_line(x1, y1, x2, y2, fill='black', width=5)
        else:  # Markers for every minute (thinner)
            cnv1.create_line(x1, y1, x2, y2, fill='grey', width=2)

# Function to set the clock to a specific time
def set_time():
    global nb_minute
    Hour, Minute = 9, 37
    nb_minute = Hour * 60 + Minute
    cnv1.delete('all')
    draw_clock()
    # Draw the hour hand in black
    cnv1.create_line(x, y, x + (r2 / 3) * cos(AngleH * (nb_minute / 60 - 3)),
                     y + (r2 / 3) * sin(AngleH * (nb_minute / 60 - 3)),
                     fill=Black, width=7, arrow='last')
    # Draw the minute hand in grey
    cnv1.create_line(x, y, x + (r2 / 2) * cos(AngleM * -15 + AngleM * Minute),
                     y + (r2 / 2) * sin(AngleM * -15 + AngleM * Minute),
                     fill=Grey, width=3, arrow='last')

# Function to update the clock center based on a mouse click
def update_position(event):
    global x, y
    x, y = event.x, event.y
    draw_clock()

# Function to advance the clock by a given number of minutes
def advance_minutes(minutes):
    global nb_minute
    nb_minute += minutes
    cnv1.delete('minutes')  # Remove the old minute hand
    draw_clock()
    # Draw the minute hand in grey
    cnv1.create_line(x, y, x + (r2 / 2) * cos(AngleM * -15 + AngleM * (nb_minute % 60)),
                     y + (r2 / 2) * sin(AngleM * -15 + AngleM * (nb_minute % 60)),
                     fill=Grey, width=3, arrow='last', tags='minutes')
    # Draw the hour hand in black
    cnv1.create_line(x, y, x + (r2 / 3) * cos(AngleH * (nb_minute / 60 - 3)),
                     y + (r2 / 3) * sin(AngleH * (nb_minute / 60 - 3)),
                     fill=Black, width=7, arrow='last')

# Functions for specific time increments
def add_1_minute():
    advance_minutes(1)

def add_5_minutes():
    advance_minutes(5)

def add_30_minutes():
    advance_minutes(30)

# Function for automatic clock advancement
def automatic():
    advance_minutes(1)
    wnd.after(1000, automatic)

# Main window setup
wnd = tk.Tk()
wnd.title('Clock / Step 4')

# Label with author name
label = tk.Label(wnd, text='DA SILVA', font=('Helvetica', 36), background='yellow')
label.pack()

# Canvas for the clock
cnv1 = tk.Canvas(wnd, width=400, height=400, background='white')
cnv1.pack()
cnv1.bind('<Button-1>', update_position)

# Buttons
tk.Button(wnd, text='9:37', command=set_time).pack(side='left')
tk.Button(wnd, text='Quit', command=wnd.destroy).pack(side='right')
tk.Button(wnd, text='+ 1 minute', command=add_1_minute).pack(side='left')
tk.Button(wnd, text='+ 5 minutes', command=add_5_minutes).pack(side='left')
tk.Button(wnd, text='+ 30 minutes', command=add_30_minutes).pack(side='left')
tk.Button(wnd, text='Automatic', command=automatic).pack(side='left')

# Initialize clock position
x, y = 200, 200
draw_clock()

# Start the main loop
wnd.mainloop()
