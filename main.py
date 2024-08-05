from tkinter import *
from tkinter import ttk

app = Tk();
app.title = "Controle";
app.geometry("520x1080");

notebook = ttk.Notebook(app, width="520", height="1080");
notebook.grid();

frameAlunos = Frame(notebook, width="260");
frameAlunos.grid();

frameAgenda = Frame(notebook, width="260");
frameAgenda.grid();

notebook.add(frameAlunos, text="Alunos")
notebook.add(frameAgenda, text="Agenda")

app.mainloop();