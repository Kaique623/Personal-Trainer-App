from tkinter import *
from tkinter import ttk

frames = {}

alunos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title = "Controle"
        self.geometry("1080x1080")

        self.infoLabels = ["Nome", "Status do Pagamento", "Data de Vencimento", "Idade"]
        self.FramesDict = {}
        self.labelsDict = {}

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
    
        self.newInfoFrame()
    
    def newInfoFrame(self):
        for aluno in alunos:
            self.FramesDict[aluno] = Frame(self.frameAlunos, width="500", height="100", highlightthickness=1, highlightbackground="black")
            self.FramesDict[aluno].pack(anchor=W, pady=1)
            self.FramesDict[aluno].pack_propagate(False)
            
            for i in self.infoLabels:
                self.labelsDict[i] = Label(self.FramesDict[aluno], text=i)
                self.labelsDict[i].pack(anchor=W)
    
if __name__ == "__main__":
    root = App()
    root.mainloop()