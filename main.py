from tkinter import *
from tkinter import ttk

app = Tk()
app.title = "Controle"
app.geometry("520x1080")

notebook = ttk.Notebook(app, width="520", height="1080")
notebook.grid()
notebook.grid_propagate(False)

frameAlunos = Frame(notebook, width="260")
frameAlunos.grid()
frameAlunos.grid_propagate(False)

frameAgenda = Frame(notebook, width="260")
frameAgenda.grid()
frameAgenda.grid_propagate(False)

notebook.add(frameAlunos, text="Alunos")
notebook.add(frameAgenda, text="Agenda")

print("teste")

app.mainloop();