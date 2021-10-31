from tkinter import *
from PIL import ImageTk, Image
import random

# ======================== Setting ===========================

# root

root = Tk()
root.title('rock,paper,Scissors')
root.geometry('600x400')
root.resizable(0, 0)
root.configure(background='gray')


# ====================== variable ============================
player_name = ''
player_move = ''
num1 = StringVar()
num2 = StringVar()
num3 = StringVar()
L_score = 0
Kira_score = 0
move = ['Rock', 'Paper', 'Scissors']
bot_move = random.randint(0, 2)
# ====================== function ============================


def name(N):
    global player_name
    if player_name == '':
        player_name += N
    num3.set(f'you are {player_name}....')
    num3.set('Enter your move....')


def player(m):
    
    if player_name != '':
        global player_move
        global L_score
        global Kira_score
        global bot_move
    
        player_move = m
        

        if player_name == 'L':
            num2.set(L_score)
            num1.set(Kira_score)   
             

            if player_move == move[bot_move]:
                num3.set('equal moves, choose your other move')
                num2.set(L_score)
                bot_move = random.randint(0, 2)
                if L_score >=10:
                    num3.set('DEATH NOTE : KIRA DEAD.......')
                elif Kira_score >=10:
                    num3.set('DEATH NOTE : L DEAD.......')

            elif player_move == 'Paper' and move[bot_move] == 'Rock':
                L_score += 1
                num3.set('you win , choose your other move')
                num2.set(L_score)
                bot_move = random.randint(0, 2)
                if L_score >=10:
                    num3.set('DEATH NOTE : KIRA DEAD.......')
                elif Kira_score >=10:
                    num3.set('DEATH NOTE : L DEAD.......')

            elif player_move == 'Rock' and move[bot_move] == 'Scissors':
                L_score += 1
                num3.set('you win, choose your other move')
                num2.set(L_score)
                bot_move = random.randint(0, 2)
                if L_score >=10:
                    num3.set('DEATH NOTE : KIRA DEAD.......')
                elif Kira_score >=10:
                    num3.set('DEATH NOTE : L DEAD.......')

            elif player_move == 'Scissors' and move[bot_move] == 'Paper':
                L_score += 1
                num3.set('you win, choose your other move')
                num2.set(L_score)
                bot_move = random.randint(0, 2)
                if L_score >=10:
                    num3.set('DEATH NOTE : KIRA DEAD.......')
                elif Kira_score >=10:
                    num3.set('DEATH NOTE : L DEAD.......')

            elif player_move == 'Rock' and move[bot_move] == 'Paper':
                Kira_score += 1
                num3.set('you lose, choose your other move')
                num1.set(Kira_score)
                bot_move = random.randint(0, 2)
                if L_score >=10:
                    num3.set('DEATH NOTE : KIRA DEAD.......')
                elif Kira_score >=10:
                    num3.set('DEATH NOTE : L DEAD.......')

            elif player_move == 'Paper' and move[bot_move] == 'Scissors':
                Kira_score += 1
                num3.set('you lose, choose your other move')
                num1.set(Kira_score)
                bot_move = random.randint(0, 2)
                if L_score >=10:
                    num3.set('DEATH NOTE : KIRA DEAD.......')
                elif Kira_score >=10:
                    num3.set('DEATH NOTE : L DEAD.......')

            elif player_move == 'Scissors' and move[bot_move] == 'Rock':
                Kira_score += 1
                num3.set('you lose, choose your other move')
                num1.set(Kira_score)
                bot_move = random.randint(0, 2)
                if L_score >=10:
                    num3.set('DEATH NOTE : KIRA DEAD.......')
                elif Kira_score >=10:
                    num3.set('DEATH NOTE : L DEAD.......')

        else:
            if player_move == move[bot_move]:
                num3.set('equal moves, choose your other move')
                num1.set(Kira_score)
                bot_move = random.randint(0, 2)
                if L_score >=10:
                    num3.set('DEATH NOTE : KIRA DEAD.......')
                elif Kira_score >=10:
                    num3.set('DETH NOTE : L DEAD.......')

            elif player_move == 'Paper' and move[bot_move] == 'Rock':
                Kira_score += 1
                num3.set('you win, choose your other move')
                num1.set(Kira_score)
                bot_move = random.randint(0, 2)
                if L_score >=10:
                    num3.set('DEATH NOTE : KIRA DEAD.......')
                elif Kira_score >=10:
                    num3.set('DEATH NOTE : L DEAD.......')

            elif player_move == 'Rock' and move[bot_move] == 'Scissors':
                Kira_score += 1
                num3.set('you win, choose your other move')
                num1.set(Kira_score)
                bot_move = random.randint(0, 2)
                if L_score >=10:
                    num3.set('DEATH NOTE : KIRA DEAD.......')
                elif Kira_score >=10:
                    num3.set('DEATH NOTE : L DEAD.......')

            elif player_move == 'Scissors' and move[bot_move] == 'Paper':
                Kira_score += 1
                num3.set('you win....')
                num1.set(Kira_score)
                bot_move = random.randint(0, 2)
                if L_score >=10:
                    num3.set('DEATH NOTE : KIRA DEAD.......')
                elif Kira_score >=10:
                    num3.set('DEATH NOTE : L DEAD.......')

            elif player_move == 'Rock' and move[bot_move] == 'Paper':
                L_score += 1
                num3.set('you lose, choose your other move')
                num2.set(L_score)
                bot_move = random.randint(0, 2)
                if L_score >=10:
                    num3.set('DEATH NOTE : KIRA DEAD.......')
                elif Kira_score >=10:
                    num3.set('DEATH NOTE : L DEAD.......')

            elif player_move == 'Paper' and move[bot_move] == 'Scissors':
                L_score += 1
                num3.set('you lose, choose your other move')
                num2.set(L_score)
                bot_move = random.randint(0, 2)
                if L_score >=10:
                    num3.set('DEATH NOTE : KIRA DEAD.......')
                elif Kira_score >=10:
                    num3.set('DEATH NOTE : L DEAD.......')

            elif player_move == 'Scissors' and move[bot_move] == 'Rock':
                L_score += 1
                num3.set('you lose, choose your other move')
                num2.set(L_score)
                bot_move = random.randint(0, 2)
                if L_score >=10:
                    num3.set('DEATH NOTE : KIRA DEAD.......')
                elif Kira_score >=10:
                    num3.set('DEATH NOTE : L DEAD.......')
            

    else:
        num3.set('First choose your character! ')
        



# ======================= Frames =============================

frame_1 = Frame(root, width=600, height=200, bg='black')
frame_1.pack(side=TOP)

frame_2 = Frame(root, width=600, height=200, bg='grey')
frame_2.pack(side=TOP)

frame_3 = Frame(root, width=600, height=200, bg='grey')
frame_3.pack(side=BOTTOM)

frame_4 = Frame(root, width=600, height=200, bg='grey')
frame_4.pack(side=TOP)


# ======================= images ===========================

# paper

canvas = Canvas(frame_1, width=150, height=150, background='red')
canvas.pack(side=LEFT, pady=2, padx=2)
img = Image.open("paper.jpg")

resized_image = img.resize((143, 143), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)

canvas.create_image(5, 5, anchor=NW, image=new_image)

# rock

canvas = Canvas(frame_1, width=150, height=150, background='red')
canvas.pack(side=LEFT, pady=2, padx=2)
img1 = Image.open("rock.jpg")

resized_image1 = img1.resize((143, 143), Image.ANTIALIAS)
new_image1 = ImageTk.PhotoImage(resized_image1)

canvas.create_image(5, 5, anchor=NW, image=new_image1)

# scissors

canvas = Canvas(frame_1, width=150, height=150, background='red')
canvas.pack(side=LEFT, pady=2, padx=2)
img2 = Image.open("scissors.png")

resized_image2 = img2.resize((143, 143), Image.ANTIALIAS)
new_image2 = ImageTk.PhotoImage(resized_image2)

canvas.create_image(5, 5, anchor=NW, image=new_image2)

# L

canvas = Canvas(frame_3, width=140, height=140, background='red')
canvas.pack(side=LEFT, pady=5, padx=5)
img3 = Image.open("L.jpg")

resized_image3 = img3.resize((135, 135), Image.ANTIALIAS)
new_image3 = ImageTk.PhotoImage(resized_image3)

canvas.create_image(5, 5, anchor=NW, image=new_image3)


# Kira

canvas = Canvas(frame_3, width=140, height=140, background='red')
canvas.pack(side=RIGHT, pady=5, padx=5)
img4 = Image.open("Kira.jpg")
resized_image4 = img4.resize((135, 135), Image.ANTIALIAS)
new_image4 = ImageTk.PhotoImage(resized_image4)

canvas.create_image(5, 5, anchor=NW, image=new_image4)

# ======================= buttons ==============================

btn_paper = Button(frame_2, text='Paper', foreground="white", width=15,
                   height=2, background='black', command=lambda: player('Paper'))
btn_paper.pack(side=LEFT, padx=20, pady=5)

btn_rock = Button(frame_2, text='Rock', foreground="white", width=15,
                  height=2, background='black', command=lambda: player('Rock'))
btn_rock.pack(side=LEFT, padx=20, pady=5)

btn_scissor = Button(frame_2, text='Scissors', foreground="white", width=15,
                     height=2, background='black', command=lambda: player('Scissors'))
btn_scissor.pack(side=LEFT, padx=20, pady=5)

btn_L = Button(frame_3, text='L', foreground="white", width=3, height=7, background='black',
               command=lambda: name('L'), font=("Times New Roman (Headings CS)", 10))
btn_L .pack(side=LEFT, pady=5)

btn_Kira = Button(frame_3, text='Kira', foreground="white", width=3, height=7, background='black',
                  command=lambda: name('KIRA'), font=("Times New Roman (Headings CS)", 10))
btn_Kira.pack(side=RIGHT, pady=5)

# ======================= Label ==============================

lab = Label(frame_3, text='choose your character', foreground="black", background='gray',
            width=19, height=2, font=("Times New Roman (Headings CS)", 13))
lab.pack(side=TOP)
lab = Label(frame_3, text='<=======VS=======>', foreground="black", background='gray',
            width=20, height=2, font=("Times New Roman (Headings CS)", 12))
lab.pack(side=TOP)

# ======================= Entry ==============================

ent1 = Entry(frame_3, textvariable=num1,  background='red',
             font=("Bernard MT Condensed", 20))
ent1.pack(side=LEFT, padx=35)
ent1.place(x=510, y=100, width=50, height=50)

ent2 = Entry(frame_3, textvariable=num2,  background='red',
             font=("Bernard MT Condensed", 20))
ent2.pack(side=RIGHT, padx=35)
ent2.place(x=100, y=100, width=50, height=50)

ent3 = Entry(frame_4, textvariable=num3,  background='black',
             foreground="red", font=("Bernard MT Condensed", 15))
ent3.pack(side=BOTTOM, padx=35)
ent3.place(x=150, y=10, width=300, height=30)


root.mainloop()