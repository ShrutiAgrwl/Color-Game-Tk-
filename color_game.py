# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 15:34:22 2019

@author: Shruti
"""

from tkinter import *
import random

color_list=[['RED', 'YELLOW', 'BLUE', 'RED', 'PINK', 'RED'], 
            ['YELLOW', 'BLUE', 'YELLOW', 'GREY', 'GREEN', 'YELLOW'], 
            ['BLUE', 'PINK', 'RED', 'GREEN', 'BLUE', 'BLUE'],
            ['GREEN', 'GREEN', 'RED', 'GREY', 'YELLOW', 'GREEN'],
            ['PINK', 'YELLOW', 'PINK', 'RED', 'PURPLE', 'PINK'],
            ['BLACK', 'PINK', 'BLACK', 'PURPLE', 'BLUE', 'BLACK'],
            ['PURPLE', 'ORANGE', 'RED', 'GREEN', 'PURPLE', 'PURPLE'],
            ['GREY', 'GREY', 'ORANGE', 'BLUE', 'PURPLE', 'GREY'],
            ['VIOLET', 'VIOLET', 'BROWN', 'GREEN', 'BLUE', 'VIOLET'],
            ['BROWN', 'GREY', 'BROWN', 'BLACK', 'PURPLE', 'BROWN']
            ]

count = 0
correct = 0
score = 0

# start the quiz
def start(event):
    global count
    global correct
    global score
    count = 0
    correct = 0
    score = 0
    widget_list = root.winfo_children()
    for item in widget_list:
        item.grid_forget()
    quiz()

# generating the quiz
def quiz():
    r = random.randint(0, 9)
    global count
    global correct
    global score
    global color_list
        
    if count+1 <= len(color_list): 
        ques['text'] = color_list[r][0]
        ques['fg'] = color_list[count][0]
        ques.grid(row=0, column=1)
        btn1 = Button(root, text=color_list[count][1], width=8, height=2, command=lambda: check(color_list[count][1])).grid(row=1, column=0, padx=2, pady=8)
        btn2 = Button(root, text=color_list[count][2], width=8, height=2, command=lambda: check(color_list[count][2])).grid(row=1, column=2, padx=2, pady=8)
        btn3 = Button(root, text=color_list[count][3], width=8, height=2, command=lambda: check(color_list[count][3])).grid(row=2, column=0, padx=2, pady=8)
        btn4 = Button(root, text=color_list[count][4], width=8, height=2, command=lambda: check(color_list[count][4])).grid(row=2, column=2, padx=2, pady=8)
    
        
    else:
        widget_list = root.winfo_children()
        for item in widget_list:
            item.grid_forget()
            
        restart()
    
# check the answers
def check(text):
    global count
    global correct
    global score
    if text == color_list[count][5]:
        correct += 1
        score += 10
     
    count += 1
    quiz()
    
# restart the quiz
def restart():
    global correct
    global score
    
    Label(root, text="Result : " , font=('arial', 18, 'bold'), width=6, height=1).grid(row=0, column=0)
    total = Label(root, text="Total : " + str(10), font=('arial', 18, 'bold'), width=10, height=1, fg='brown').grid(row=0, column=1)
    correct_ques = Label(root, text="Correct : " + str(correct), font=('arial', 18, 'bold'), fg='green', width=10, height=1).grid(row=1, column=1)
    incorrect_ques = Label(root, text="Inorrect : " + str(10-correct), font=('arial', 18, 'bold'), fg='red', width=10, height=1).grid(row=2, column=1)
    t_score = Label(root, text="Score : " + str(score), font=('arial', 18, 'bold'), fg='blue', width=10, height=1).grid(row=3, column=1)
    btn = Button(root, text='Restart', fg='white', bg='blue', font=('arial', 8, 'bold'), width=10, height=2)
    btn.bind('<Button-1>', start)
    btn.grid(row=4, column=1, padx=4, pady=5)
    

root = Tk()
root.geometry('300x200')
l = Label(root, text='Choose the color of \nthe text not the name \nof the text', font=('arial', 20, 'bold'))
l.grid(row=0, column=0)
btn = Button(root, text='Start', fg='white', bg='blue', font=('arial', 8, 'bold'), width=8, height=2)
btn.bind('<Button-1>', start)
btn.grid(row=1, column=0, padx=4, pady=5)
ques = Label(root, text='', font=('arial', 18, 'bold'), width=10, height=2)
root.mainloop()