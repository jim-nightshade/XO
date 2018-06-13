from tkinter import *
from tkinter import messagebox

import random


w = Tk()
w.title('CLICK')

x = -1

def o_move(index):
    
    o_moves.append(index)
    buttons[index].config(state = 'disabled', text = 'O')
    win(o_moves)
    
    x_move()
    win(x_moves)
    
def x_move():
    global x
    moves = x_moves + o_moves
    while x in moves or x == -1:
        x = random.randint(0,8)
    x_moves.append(x)
    buttons[x].config(state = 'disabled', text = 'X')

def win(player_moves):
    win_moves = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for test in win_moves:
        win_temp = [i for i in player_moves if i in test]
        print(i,test,win_temp)
        if sorted(win_temp) in win_moves:
            if player_moves == x_moves:
                messagebox.showinfo('GAME OVER', 'CONGRATULATIONS COMPUTER!')
                
            else:
                messagebox.showinfo('GAME OVER', 'CONGRATULATIONS!')
            w.quit()


    
        

buttons = []
x_moves = []
o_moves = []


for i in range(9):
    buttons.append(Button(w, text = ' '))
    buttons[i].config(command = lambda index = i: o_move(index))
    buttons[i].config(relief = 'flat', width = 6, pady = 2, font = ('Arial', '10', 'bold'))
    buttons[i].grid(column = i%3 , row = i//3, sticky = W+E+N+S)
    
x_move()


w.mainloop()




# button['command'] = lambda arg1 = local_var1, arg2 = local_var2 : function(arg1, arg2)
# arg1 = local_var1 przypisuje argumentowi funkcji wartosc lokalna w momencie tworzenia lambda, wywoluje callback z zapamietana lokalnie wartoscia
# command = lambda index = 5: disable(5) // dla 6 przycisku przykladowo
