from tkinter import *
from tkinter import ttk

frames = {}

alunos = [1, 2, 3, 4]

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title = "Controle"
        self.geometry("1080x1080")

        self.startup()
    
    def startup(self):
        self.notebook = ttk.Notebook(self, width="520", height="1080")
        self.notebook.pack()
        self.notebook.pack_propagate(False)

        self.frameAlunos = Frame(self.notebook, width="520", height="1080")
        self.frameAlunos.pack()
        self.frameAlunos.pack_propagate(False)

        self.frameAgenda = Frame(self.notebook, width="520",  height="1080")
        self.frameAgenda.pack()
        self.frameAgenda.pack_propagate(False)

        self.notebook.add(self.frameAlunos, text="Alunos")
        self.notebook.add(self.frameAgenda, text="Agenda")
    
    def newInfoFrame(self):

        self.infoFrame = Frame(self.frameAlunos, width="500", height="100", highlightthickness=1, highlightbackground="black")
        self.infoFrame.pack(anchor=W)
        self.infoFrame.pack_propagate(False)

        self.nomeLabel = Label(self.infoFrame, text="Nome: ")
        self.nomeLabel.pack(anchor=W)

        self.statusLabel = Label(self.infoFrame, text="Status de Pagamento: ")
        self.statusLabel.pack(anchor=W)

        self.nomeLabel = Label(self.infoFrame, text="Data de Vencimento do Pagamento: ")
        self.nomeLabel.pack(anchor=W)
    
if __name__ == "__main__":
    root = App()
    root.mainloop()