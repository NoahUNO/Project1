from tkinter import *
import random


class GUI:
    def __init__(self, window: None) -> None:

        """
        This function is used to create the GUI for the rock, paper, scissors game to be played.
        :param window: Used to create the locked dimensions for the GUI.
        """
        self.window = window

        self.frame_game = Frame(self.window)
        self.label_game = Label(self.frame_game, text='Welcome to Rock/Paper/Scissors!')
        self.label_game.pack(padx=5, side='left')
        self.frame_game.pack(anchor='w', pady=5)

        self.frame_game2 = Frame(self.window)
        self.label_game2 = Label(self.frame_game2, text='Select an option to face against the computer!')
        self.label_game2.pack(padx=5, side='left')
        self.frame_game2.pack(anchor='w', pady=5)

        self.frame_status = Frame(self.window)
        self.label_status = Label(self.frame_status, text='Choose:')
        self.radio = IntVar()
        self.radio.set(-1)
        self.radio_paper = Radiobutton(self.frame_status, text='Paper', variable=self.radio, value=0)
        self.radio_rock = Radiobutton(self.frame_status, text='Rock', variable=self.radio, value=1)
        self.radio_scissor = Radiobutton(self.frame_status, text='Scissor', variable=self.radio, value=2)
        self.label_status.pack(padx=5, side='left')
        self.radio_paper.pack(side='left')
        self.radio_rock.pack(side='left')
        self.radio_scissor.pack(side='left')
        self.frame_status.pack()
        self.frame_status.pack(anchor='w', pady=5)

        self.frame_results = Frame(self.window)
        self.label_results = Label(self.frame_results, text='')
        self.label_results.pack(padx=5, side='left')
        self.frame_results.pack(anchor='w', pady=5)

        self.frame_save = Frame(self.window)
        self.button_save = Button(self.frame_save, text='SAVE', command=self.clicked)
        self.button_save.pack()
        self.frame_save.pack(pady=10)

    def clicked(self) -> None:
        """
        This function is utilized when the 'SAVE' button is clicked in the GUI.
        This function gathers necessary information from the user's input, creates a randomized computer choice,
        and calls the game function.
        After this is complete and there are results from the game function, the results are printed on the GUI
        and the interface is cleaned off for the next round.
        :return: This function returns no data.
        """
        status = self.radio.get()
        if status == 0:
            user = 'paper'
        elif status == 1:
            user = 'rock'
        elif status == 2:
            user = 'scissor'
        else:
            self.label_results.destroy()
            self.label_results = Label(self.frame_results, text='Please select a choice before clicking SAVE.')
            self.label_results.pack(padx=5, side='left')

        computer = ['rock', 'paper', 'scissor']
        comp = random.choice(computer)
        results = self.game(user, comp)
        self.label_results.destroy()
        self.label_results = Label(self.frame_results, text='Computer is {}. You are {}. You {}'.format(comp, user, results))
        self.label_results.pack(padx=5, side='left')
        self.radio.set(-1)

    def game(self, user: str, comp: str) -> str:
        """
        This function is for the rock, paper, scissors game.
        It takes the user's input plus the computer's randomized choice and determines the winner.
        Paper beats rock, rock beats scissors, and scissors beats paper.
        :param user: User's input
        :param comp: Computer's randomized choice
        :return: The results of the game in terms of the user, win, tie, or lose
        """
        if comp == 'rock':
            if user == 'rock':
                return 'tie'
            elif user == 'paper':
                return 'win'
            else:
                return 'lose'
        elif comp == 'paper':
            if user == 'rock':
                return 'lose'
            elif user == 'paper':
                return 'tie'
            else:
                return 'win'
        else:
            if user == 'rock':
                return 'win'
            elif user == 'paper':
                return 'lose'
            else:
                return 'tie'
