from tkinter import *
from tkinter import messagebox
import random


w = Tk()
w.title('XO.')

buttons = []
x_moves = []
o_moves = []
x_wins = 0
o_wins = 0

r = -1




class Player:
    def __init__(self, name, wins):
        self.name = name
        self.wins = wins
    def move(self):
        raise NotImplemented()
    
    def win(self, player_moves):
        win_moves = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        if any(all(i in player_moves for i in test) for test in win_moves):
            return True
        else:
            return False

    def win_msg(self):
        if messagebox.askyesno('GAME OVER', 'CONGRATULATIONS ' + self.name + ' ! Another game ?'):
            board.generate()
        else:
            w.destroy()

    def draw_msg(self):
        if messagebox.askyesno('GAME OVER', 'IT IS A DRAW ! Another game ?'):
            board.generate()
        else:
            w.destroy()

class Player_Human(Player):
    def __init__(self, name, wins):
        super().__init__(name, wins)

    def move(self, index):
        o_moves.append(index)
        buttons[index].config(state = 'disabled', text = 'O')
        if self.win(o_moves):
            self.wins += 1
            w.title('XO. CPU:' + str(x.wins) + ' HUM:' + str(o.wins))
            self.win_msg()
        else:
            x.move()
    
class Player_CPU(Player):
    def __init__(self, name, wins):
        super().__init__(name, wins)

    def move(self):
        global r
        moves = x_moves + o_moves
        while r in moves or r == -1:
            r = random.randint(0,8)
            
        x_moves.append(r)
        buttons[r].after(1000, lambda r = r: buttons[r].config(highlightbackground = 'azure')) # function, eg. lambda is added to the queue with a timestamp. When it is ready to be processed, tkinter will call the function and pass in the arguments. Otherwise puts GUI to sleep, eq. to time.sleep() and slows down. AVOID !!  
        buttons[r].after(500, lambda r = r: buttons[r].config(state = 'disabled', text = 'X'))
        if self.win(x_moves):
            self.wins += 1
            w.title('XO. CPU:' + str(x.wins) + ' HUM:' + str(o.wins))
            self.win_msg()
        elif len(x_moves + o_moves) == 9:
            self.draw_msg()

class Board:
    
    def generate(self):
        global buttons, x_moves, o_moves
        buttons = []
        x_moves = []
        o_moves = []
        x_wins = 0
        o_wins = 0

        for i in range(9):
            buttons.append(Button(w, text = ''))
            buttons[i].config(command = lambda index = i: o.move(index))
            buttons[i].config(relief = 'flat', width = 7, pady = 2, font = ('Arial', '10', 'bold'))
            buttons[i].grid(column = i%3 , row = i//3, sticky = W+E+N+S)
    
        x.move()


o = Player_Human('HUMAN', o_wins)
x = Player_CPU('CPU', x_wins)

board = Board()
board.generate()

w.mainloop()




# button['command'] = lambda arg1 = local_var1, arg2 = local_var2 : function(arg1, arg2)
# arg1 = local_var1 przypisuje argumentowi funkcji wartosc lokalna w momencie tworzenia lambda, wywoluje callback z zapamietana lokalnie wartoscia
# command = lambda index = 5: disable(5) // dla 6 przycisku przykladowo
