from tkinter import *
from tkinter import ttk

app = Tk()
app.title = "Controle"
app.geometry("520x1080")

notebook = ttk.Notebook(app, width="520", height="1080")
notebook.pack()
notebook.pack_propagate(False)

frameAlunos = Frame(notebook, width="260", height="1080")
frameAlunos.pack()
frameAlunos.pack_propagate(False)

frameAgenda = Frame(notebook, width="260",  height="1080")
frameAgenda.pack()
frameAgenda.pack_propagate(False)

notebook.add(frameAlunos, text="Alunos")
notebook.add(frameAgenda, text="Agenda")

app.mainloop()