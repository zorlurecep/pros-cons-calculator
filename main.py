from tkinter import *
from tkinter import messagebox


def createFrames(ws):
    inputFrame = Frame(ws)
    inputFrame.pack(pady=10, padx=10, side=TOP)

    prosFrame = Frame(ws)
    prosFrame.pack(pady=10, padx=10, side=LEFT)

    consFrame = Frame(ws)
    consFrame.pack(pady=10, padx=10, side=RIGHT)

    return (inputFrame, prosFrame, consFrame)


def createListBoxes(prosFrame, consFrame):
    lbPros = Listbox(
        prosFrame,
        width=25,
        height=8,
        font=('Times', 18),
        bd=0,
        fg='#464646',
        highlightthickness=0,
        selectbackground='#a6a6a6',
        activestyle="none"
    )
    lbPros.pack(side=LEFT, fill=BOTH)

    lbCons = Listbox(
        consFrame,
        width=25,
        height=8,
        font=('Times', 18),
        bd=0,
        fg='#464646',
        highlightthickness=0,
        selectbackground='#a6a6a6',
        activestyle="none"
    )
    lbCons.pack(side=LEFT, fill=BOTH)

    return (lbPros, lbCons)

# This is for testing purposes delete it after implementation of actual program


def fill_in_dummy_data(lbPros, lbCons):
    task_list = [
        'Eat apple',
        'drink water',
        'go gym',
        'write software',
        'write documentation',
        'take a nap',
        'Learn something',
        'paint canvas',
        'Eat apple',
        'drink water',
        'go gym',
        'write software',
        'write documentation',
        'take a nap',
        'Learn something',
        'paint canvas'
    ]
    for item in task_list:
        lbPros.insert(END, item)
        lbCons.insert(END, item)


def create_scroll_bars(prosFrame, consFrame):
    sbPros = Scrollbar(prosFrame)
    sbPros.pack(side=RIGHT, fill=BOTH)

    lbPros.config(yscrollcommand=sbPros.set)
    sbPros.config(command=lbPros.yview)

    sbCons = Scrollbar(consFrame)
    sbCons.pack(side=RIGHT, fill=BOTH)

    lbCons.config(yscrollcommand=sbCons.set)
    sbCons.config(command=lbCons.yview)

def show_results():
    messagebox.showinfo("Result", "Result can be shown here.")


if __name__ == '__main__':
    ws = Tk()
    ws.geometry('1000x450+500+200')
    ws.title('ProsCons')
    ws.config(bg='#223441')
    ws.resizable(width=False, height=False)

    inputFrame, prosFrame, consFrame = createFrames(ws)

    lbPros, lbCons = createListBoxes(prosFrame, consFrame)

    fill_in_dummy_data(lbPros, lbCons)

    create_scroll_bars(prosFrame, consFrame)

    user_input = Entry(inputFrame, font=('times', 18))
    user_input.pack(pady=20, padx=10, side=LEFT)

    weight_input = Entry(inputFrame, font=('times', 18))
    weight_input.pack(pady=20, padx=10, side=LEFT)

    add_input = Button(
        inputFrame,
        text='Add Task',
        font=('times 14'),
        bg='#c5f776',
        padx=20,
        pady=10,

        # Below parameter binds the function to the button
        # command=newTask

        command = show_results
    )

    options = ["asdads", "Pro", "Con"]
    type_of_input = OptionMenu(inputFrame, *options)
    type_of_input.pack(side=LEFT)

    add_input.pack(fill=BOTH, expand=True, side=LEFT)


    ws.mainloop()
