from gui import *


def main() -> None:
    """
    Main function. Calls the GUI module.
    :return: This function returns no data.
    """
    window = Tk()
    window.title('Project 1')
    window.geometry('265x200')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
