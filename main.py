from tkinter import *
from tkinter import ttk

frames = {}

alunos = {0: {"Nome": "Kaique", "Status do Pagamento": "Pago", "Data de Vencimento": '06/08/2024', "Idade":16}, 1: {"Nome": "Bruna"}}

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title = "Controle"
        self.geometry("1080x1080")

        self.infoLabels = ["Nome", "Status do Pagamento", "Data de Vencimento", "Idade"]
        self.FramesDict = {}
        self.labelsDict = {}
        self.labelsValue = {}

        self.startup()
    
    def clear(self):
        for i in self.winfo_children():
            i.destroy()
    
    def startup(self):
        self.notebook = ttk.Notebook(self, width="1080", height="1080")
        self.notebook.pack()
        self.notebook.pack_propagate(False)

        self.frameAlunos = Frame(self.notebook, width="1080", height="1080")
        self.frameAlunos.pack()
        self.frameAlunos.pack_propagate(False)

        self.frameAgenda = Frame(self.notebook, width="1080",  height="1080")
        self.frameAgenda.pack()
        self.frameAgenda.pack_propagate(False)

        self.notebook.add(self.frameAlunos, text="Alunos")
        self.notebook.add(self.frameAgenda, text="Agenda")
    
        self.newInfoFrame(0)
    
    def newInfoFrame(self, page):
        
        for num in range(0 + (9*page), 9 + (9*page)):  
                self.FramesDict[num] = Frame(self.frameAlunos, width="1080", height="100", highlightthickness=1, highlightbackground="black")
                self.FramesDict[num].pack(anchor=W, pady=1)
                self.FramesDict[num].pack_propagate(False)
                try:
                    placeholder = alunos[num]
                    self.FramesDict[num].bind("<Button-1>", lambda e, a=num: self.openInfo(a))
                    print(num)
                except:
                    pass
                
                for i in self.infoLabels:
                    try:
                        self.labelsDict[i] = Label(self.FramesDict[num], text=f'{i}: {alunos[num][i]}')
                        self.labelsDict[i].pack(anchor=W)
                    except:
                        self.labelsDict[i] = Label(self.FramesDict[num], text=f'{i}:')
                        self.labelsDict[i].pack(anchor=W)
        
        
    def openInfo(self, aluno):
        self.clear()
        
        for i in self.infoLabels:
                self.labelsDict[i] = Label(self, text=f'{i}: {alunos[aluno][i]}', font=("Helvetica", "48"))
                self.labelsDict[i].pack(anchor=W)
        
        
    
if __name__ == "__main__":
    root = App()
    root.mainloop()