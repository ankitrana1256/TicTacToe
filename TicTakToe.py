from tkinter import *

#Tic-Tac-Toe class which contains all the mechanism
class Tic_Tac_toe:
    def __init__(self):
        self.root=Tk()
        # Game Label
        self.my_label=Label(self.root,text="Tic-Tac-Toe",pady=20)
        self.my_label.grid(row=0,column=0,columnspan=3)
        # It holds the right turn
        self.current_player="X"
        #It holds the name of the winner
        self.winner=None
        # Displays Whose turn is this
        self.player_label=Label(self.root,text="Whose Turn to Play : "+self.current_player+"'s Turn.",pady=20)
        self.player_label.grid(row=2,column=0,columnspan=3)
        # Displays The winner
        self.winner_label=Label(self.root,text="Winner : None",pady=20)
        self.winner_label.grid(row=4,column=0,columnspan=3)
        # Keeps the account of played blocks
        self.count=int(0)
        # UI buttons
        self.button_1=Button(self.root,text=" ",command=lambda: self.change_text(self.button_1),padx=50,pady=50)
        self.button_2=Button(self.root,text=" ",command=lambda: self.change_text(self.button_2),padx=50,pady=50)
        self.button_3=Button(self.root,text=" ",command=lambda: self.change_text(self.button_3),padx=50,pady=50)
        self.button_4=Button(self.root,text=" ",command=lambda: self.change_text(self.button_4),padx=50,pady=50)
        self.button_5=Button(self.root,text=" ",command=lambda: self.change_text(self.button_5),padx=50,pady=50)
        self.button_6=Button(self.root,text=" ",command=lambda: self.change_text(self.button_6),padx=50,pady=50)
        self.button_7=Button(self.root,text=" ",command=lambda: self.change_text(self.button_7),padx=50,pady=50)
        self.button_8=Button(self.root,text=" ",command=lambda: self.change_text(self.button_8),padx=50,pady=50)
        self.button_9=Button(self.root,text=" ",command=lambda: self.change_text(self.button_9),padx=50,pady=50)
        self.button_1.grid(row=5,column=0)
        self.button_2.grid(row=5,column=1)
        self.button_3.grid(row=5,column=2)
        self.button_4.grid(row=6,column=0)
        self.button_5.grid(row=6,column=1)
        self.button_6.grid(row=6,column=2)
        self.button_7.grid(row=7,column=0)
        self.button_8.grid(row=7,column=1)
        self.button_9.grid(row=7,column=2)
        self.root.mainloop()
    def change_text(self,button):
        button["text"]=self.current_player
        button["state"]=DISABLED
        if self.current_player=='X' :
            button["bg"]="black"
        else :
            button["bg"]="yellow"
        button["fg"]="white"
        self.count+=1
        self.check_if_someone_wins()
        self.check_if_its_tie()
        self.flip_current_player()

    def flip_current_player(self):
        if self.current_player=="X":
            self.current_player="O"
            self.player_label["text"]="Whose Turn to Play : "+self.current_player+"'s Turn."
        elif self.current_player=="O":
            self.current_player="X"
            self.player_label["text"]="Whose Turn to Play : "+self.current_player+"'s Turn."
    def check_if_someone_wins(self):
        self.check_rows()
        self.check_columns()
        self.check_diagonals()
    def check_rows(self):
        row_1=self.button_1["text"]==self.button_2["text"]==self.button_3["text"]==self.current_player
        row_2=self.button_4["text"]==self.button_5["text"]==self.button_6["text"]==self.current_player
        row_3=self.button_7["text"]==self.button_8["text"]==self.button_9["text"]==self.current_player
        if row_1 :
            self.winner_label["text"]=self.current_player+" win's"
            self.winner=self.current_player
            self.disable_all_buttons()
        if row_2 :
            self.winner_label["text"]=self.current_player+" win's"
            self.winner=self.current_player
            self.disable_all_buttons()
        if row_3 :
            self.winner_label["text"]=self.current_player+" win's"
            self.winner=self.current_player
            self.disable_all_buttons()
    def check_columns(self):
        column_1=self.button_1["text"]==self.button_4["text"]==self.button_7["text"]==self.current_player
        column_2=self.button_2["text"]==self.button_5["text"]==self.button_8["text"]==self.current_player
        column_3=self.button_3["text"]==self.button_6["text"]==self.button_9["text"]==self.current_player
        if column_1 :
            self.winner_label["text"]=self.current_player+" win's"
            self.winner=self.current_player
            self.disable_all_buttons()
        if column_2 :
            self.winner_label["text"]=self.current_player+" win's"
            self.winner=self.current_player
            self.disable_all_buttons()
        if column_3 :
            self.winner_label["text"]=self.current_player+" win's"
            self.winner=self.current_player
            self.disable_all_buttons()
    def check_diagonals(self):
        diagonal_1=self.button_1["text"]==self.button_5["text"]==self.button_9["text"]==self.current_player
        diagonal_2=self.button_3["text"]==self.button_5["text"]==self.button_7["text"]==self.current_player
        if diagonal_1 :
            self.winner_label["text"]=self.current_player+" win's"
            self.winner=self.current_player
            self.disable_all_buttons()
        if diagonal_2 :
            self.winner_label["text"]=self.current_player+" win's"
            self.winner=self.current_player
            self.disable_all_buttons()

    def disable_all_buttons(self):
        self.button_1["state"]=DISABLED
        self.button_2["state"]=DISABLED
        self.button_3["state"]=DISABLED
        self.button_4["state"]=DISABLED
        self.button_5["state"]=DISABLED
        self.button_6["state"]=DISABLED
        self.button_7["state"]=DISABLED
        self.button_8["state"]=DISABLED
        self.button_9["state"]=DISABLED
    def check_if_its_tie(self):
        if self.count==9 and self.winner==None:
            self.winner_label["text"]="Oops it's a Tie."
app=Tic_Tac_toe()