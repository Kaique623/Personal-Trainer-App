from tkinter import *
from tkinter import ttk

frames = {}

alunos = {0: {"Nome": "Kaique Madureira", "Status de Pagamento": "Pago", "Data de Vencimento": '06/08/2024', "Idade":16, "Altura": 162, "Peso": 47, "Gênero": "M"}, 1: {"Nome": "Bruna"}}

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title = "Controle"
        self.geometry("1080x1080")
        
        self.infoLabels = ["Nome", "Status de Pagamento", "Data de Vencimento", "Idade"]
        self.FramesDict = {}
        self.labelsDict = {}
        self.labelsValue = {}
        
        self.infoFrames = {}

        self.curPage = 0
        self.maxPage = (len(alunos)/8)

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
    
        self.newInfoFrame()
    
    def newInfoFrame(self):
        
        self.topFrame = Frame(self.frameAlunos, width="1080", height="180", highlightthickness=1, highlightbackground="black")
        self.topFrame.pack(anchor=N)
        self.topFrame.pack_propagate(False)
        
        self.leftArrowFrame = Frame(self.topFrame, width=100, height=180, highlightthickness=1, highlightbackground="blue")
        self.leftArrowFrame.grid(sticky=W, column=0, row=0)
        self.leftArrowFrame.bind("<Button>", lambda e: self.movePage(-1))
        self.leftArrowLabel = Label(self.leftArrowFrame, text="←", font=("Arial", 40), background="blue", fg="white")
        self.leftArrowLabel.bind("<Button>", lambda e: self.movePage(-1))
        self.leftArrowLabel.grid()
        
        self.pageLabelString = StringVar()
        self.pageLabel = Label(self.topFrame, textvariable=self.pageLabelString, font=("Arial", 14))
        self.pageLabel.grid(sticky=N, column=1, row=0, padx=445)
        self.pageLabelString.set(f"Página\n{self.curPage}/{self.maxPage:,.0f}")
        
        self.RightArrowFrame = Frame(self.topFrame, width=100, height=180, highlightthickness=1, highlightbackground="blue")
        self.RightArrowFrame.grid(sticky=W, column=2, row=0)
        self.RightArrowFrame.bind("<Button>", lambda e: self.movePage(1))
        self.RightArrowLabel = Label(self.RightArrowFrame, text="→", font=("Arial", 40), background="blue", fg="white")
        self.RightArrowLabel.bind("<Button>", lambda e: self.movePage(1))
        self.RightArrowLabel.grid(sticky=N)
        
        for num in range(0 + (9*self.curPage), 8 + (8*self.curPage)):  
            try:
                alunos[num]
                self.FramesDict[num] = Frame(self.frameAlunos, width="1080", height="100", highlightthickness=1, highlightbackground="black")
                self.FramesDict[num].pack(anchor=W, pady=1)
                self.FramesDict[num].pack_propagate(False)
                self.FramesDict[num].bind("<Button-1>", lambda e, a=num: self.openInfo(a))
                
                for i in self.infoLabels:
                    try:
                        self.labelsDict[i] = Label(self.FramesDict[num], text=f'{i}: {alunos[num][i]}')
                        self.labelsDict[i].pack(anchor=W)
                    except:
                        self.labelsDict[i] = Label(self.FramesDict[num], text=f'{i}:')
                        self.labelsDict[i].pack(anchor=W)
            except:
                pass
        
    def refreshMainPage(self):
        self.clear()
        self.startup()
        self.pageLabelString.set(f"Página\n{self.curPage}/{self.maxPage:,.0f}")
        
    def movePage(self, num):
        if self.curPage != 0 and num == -1:
            self.curPage += num
            self.refreshMainPage()
        elif num == 1 and self.curPage < self.maxPage - 1:
            self.curPage += num            
            self.refreshMainPage()
        
    def openInfo(self, aluno):
        self.clear()
          
        self.nameFrame = LabelFrame(self, width=240, height=60, text="Nome", font=("Arial", "12"))
        self.nameFrame.grid(pady=3, sticky=W, padx=3)
        self.nameFrame.grid_propagate(False)
        
        self.nameString = StringVar()
        self.nameLabel = Entry(self.nameFrame, textvariable=self.nameString, font=("Arial", "15"), bg=self.cget("bg"), borderwidth=0)   
        self.nameLabel.grid(column=0, row=0, sticky=W)
        self.nameLabel.grid_propagate(False)
        self.nameString.set(alunos[aluno]['Nome']) 
        
        self.idadeFrame = LabelFrame(self, width=240, height=60, text="Idade", font=("Arial", "12"))
        self.idadeFrame.grid(pady=3, sticky=W, padx=3)
        self.idadeFrame.grid_propagate(False)
        
        self.idadeString = StringVar()
        self.idadeLabel = Entry(self.idadeFrame, textvariable=self.idadeString, font=("Arial", "15"), bg=self.cget("bg"), borderwidth=0)   
        self.idadeLabel.grid(column=0, row=0, sticky=W)
        self.idadeLabel.grid_propagate(False)
        self.idadeString.set(alunos[aluno]['Idade']) 
        
if __name__ == "__main__":
    root = App()
    root.mainloop()