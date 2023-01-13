import os
import sys
from random import randint
from tkinter import *
# LATEST
root = Tk()
root.title("Memory Game")

start_label = Label(root, text="Ready to start the game?")

global score
score = 0

global colours_clicked
colours_clicked = []

global flashed_list
flashed_list = []


def start():
    start_label.grid(row=1, column=1)
    start_button.grid(row=2, column=1)


def game_start():
    start_label.grid_remove()

    red_button.grid(row=2, column=1)
    blue_button.grid(row=2, column=2)
    yellow_button.grid(row=3, column=1)
    green_button.grid(row=3, column=2)

    # chooses a random button
    rng_list = ['red_button', 'blue_button', 'yellow_button', 'green_button']
    x = randint(0, 3)
    entry_random = rng_list[x]

    # stores flashed square into flashed_list

    flashed_list.append(entry_random)
    print(f"Flashed Colours {flashed_list}")

    # flashes a square
    if entry_random == 'red_button':
        flash_red()
    elif entry_random == 'blue_button':
        flash_blue()
    elif entry_random == 'yellow_button':
        flash_yellow()
    elif entry_random == 'green_button':
        flash_green()


def get_button(colour):
    if colour == 'red':
        colours_clicked.append('red_button')
    elif colour == 'blue':
        colours_clicked.append('blue_button')
    elif colour == 'yellow':
        colours_clicked.append('yellow_button')
    elif colour == 'green':
        colours_clicked.append('green_button')
    print(f"colours clicked: {colours_clicked}")
    if len(colours_clicked) == len(flashed_list):
        check_press()
    else:
        print("passing to check_press")
        individual_check_press()

def individual_check_press():
    global colours_clicked
    global score
    for i in range(len(colours_clicked)):
        if colours_clicked[i] == flashed_list[i]:
            pass
            #print(f"colour clicked: {colours_clicked[i]} & flashedlist: {flashed_list[i]}")
        else:
            print("failed individual check, moving to highscore")
            highscore()

def check_press():
    global colours_clicked
    global score
    # checks if the final 2 arrays match
    if len(colours_clicked) == len(flashed_list) and colours_clicked != flashed_list:
        print("YOU FAILED")
        highscore()

    # checks if the arrays are matched and adds a point to score
    while colours_clicked == flashed_list and len(colours_clicked) <= len(flashed_list):
        if len(colours_clicked) <= len(flashed_list):
            if colours_clicked == flashed_list:
                print('Well done!')
                score += 1
                print(score)
                colours_clicked = []
                game_start()

            else:
                print("out of guesses")
                end()


def flash_red():
    red_button.config(bg='purple')
    root.after(1200, lambda: red_button.config(bg='red'))

def flash_blue():
    blue_button.config(bg='purple')
    root.after(1200, lambda: blue_button.config(bg='blue'))

def flash_yellow():
    yellow_button.config(bg='purple')
    root.after(1200, lambda: yellow_button.config(bg='yellow'))

def flash_green():
    green_button.config(bg='purple')
    root.after(1200, lambda: green_button.config(bg='green'))


def end():
    print("error, end of code")


def highscore():
    global score
    highscore_label.grid(row=1, column=1)
    quit_button.grid(row=2, column=1)
    start_button.grid_remove()
    red_button.grid_remove()
    blue_button.grid_remove()
    yellow_button.grid_remove()
    green_button.grid_remove()
    final = score
    confirm_label = Label(root, text=final, font=('Arial',100))
    confirm_label.grid(row=1, column=2)


def quit():
    root.destroy()



highscore_label = Label(root, text=f"HighScore:", font=('Arial',100))
quit_button = Button(root, text="Quit Game", command=quit)
start_button = Button(root, text="Start", command=game_start)
# start_button.grid(row=2, column=1)
red_button = Button(root, text="Red", bg='red', padx=108, pady=100, command=lambda: get_button('red'))
blue_button = Button(root, text="Blue", bg='blue', padx=108, pady=100, command=lambda: get_button('blue'))
yellow_button = Button(root, text="Yellow", bg='yellow', padx=100, pady=100, command=lambda: get_button('yellow'))
green_button = Button(root, text="Green", bg='green', padx=105, pady=100, command=lambda: get_button('green'))

start()
root.mainloop()
