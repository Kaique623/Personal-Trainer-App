from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

alunos = []

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Controle")
        self.geometry("1080x1080")
        
        self.infoLabels = ['Nome', 'Idade', 'Altura (cm)', 'Peso (Kg)']
        self.FramesDict = {}
        self.labelsDict = {}
        self.labelsValue = {}
        
        self.infoFrames = {}

        self.curPage = 0
        self.maxPage = (len(alunos)/8)
        if len(alunos)%8 == 0 and not self.maxPage == 0:
            self.maxPage = (len(alunos)/8) - 1

        self.startup()
    
    def clear(self):
        for i in self.winfo_children():
            i.destroy()
    
    def startup(self):
        
        self.notebook = ttk.Notebook(self, width="1080", height="1080")
        self.notebook.pack(expand=True, fill='both')
        
        self.frameAlunos = Frame(self.notebook, width="1080", height="1080")
        self.frameAlunos.pack(expand=True, fill='both')
        self.frameAlunos.pack_propagate(False)

        self.frameAgenda = Frame(self.notebook, width="1080", height="1080")
        self.frameAgenda.pack(expand=True, fill='both')
        self.frameAgenda.pack_propagate(False)

        self.notebook.add(self.frameAlunos, text="Alunos")
        self.notebook.add(self.frameAgenda, text="Agenda")
        
        self.newInfoFrame()
        self.setupAgenda()

    def newInfoFrame(self):
        self.topFrame = Frame(self.frameAlunos, width="1080", height="140", highlightthickness=1, highlightbackground="black")
        self.topFrame.pack(anchor=N)
        self.topFrame.pack_propagate(False)
        
        self.leftArrowFrame = Frame(self.topFrame, width=100, height=140, highlightthickness=1, highlightbackground="blue")
        self.leftArrowFrame.grid(sticky=W, column=0, row=0)
        self.leftArrowFrame.bind("<Button>", lambda e: self.movePage(-1))
        self.leftArrowLabel = Label(self.leftArrowFrame, text="←", font=("Arial", 40), background="blue", fg="white")
        self.leftArrowLabel.bind("<Button>", lambda e: self.movePage(-1))
        self.leftArrowLabel.grid()
        
        self.pageLabelString = StringVar()
        self.pageLabel = Label(self.topFrame, textvariable=self.pageLabelString, font=("Arial", 14))
        self.pageLabel.grid(sticky=N, column=1, row=0, padx=445)
        self.pageLabelString.set(f"Página\n{self.curPage}/{self.maxPage:,.0f}")
        
        self.RightArrowFrame = Frame(self.topFrame, width=100, height=140, highlightthickness=1, highlightbackground="blue")
        self.RightArrowFrame.grid(sticky=W, column=2, row=0)
        self.RightArrowFrame.bind("<Button>", lambda e: self.movePage(1))
        self.RightArrowLabel = Label(self.RightArrowFrame, text="→", font=("Arial", 40), background="blue", fg="white")
        self.RightArrowLabel.bind("<Button>", lambda e: self.movePage(1))
        self.RightArrowLabel.grid(sticky=N)
        
        self.addButton = Frame(self.frameAlunos, width="1080", height="50", highlightthickness=1, highlightbackground="black")
        self.addButton.pack(anchor=N, pady=3)
        self.addButton.pack_propagate(False)
        self.addButton.bind('<Button>', lambda e: self.telaDeCadastro())
        
        self.addButtonLabel = Label(self.addButton, text="(+) Adicionar", font=("Arial", 14))
        self.addButtonLabel.pack(anchor=N, pady=5)
        self.addButtonLabel.bind('<Button>', lambda e: self.telaDeCadastro())
        
        for num in range(0 + (8*self.curPage), 8 + (8*self.curPage)):  
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
        self.maxPage = (len(alunos)/8)
        if len(alunos)%8 == 0 and not self.maxPage == 0:
            self.maxPage = (len(alunos)/8) - 1
        self.pageLabelString.set(f"Página\n{self.curPage}/{self.maxPage:,.0f}")
        self.startup()
        
    def movePage(self, num):
        if self.curPage != 0 and num == -1:
            self.curPage += num
            self.refreshMainPage()
        elif num == 1 and self.curPage < self.maxPage - 1:
            self.curPage += num            
            self.refreshMainPage()
        
    def openInfo(self, aluno):
        self.clear()
          
        self.info = ['Nome', 'Idade', 'Altura (cm)', 'Peso (Kg)', 'Gênero']
        self.openInfoFrames = {}
        self.openInfoEntry = {}
        self.openInfoValues = {}
        
        self.counter = 0
        self.column = 0
        
        for i in self.info:
            self.openInfoFrames[i] = LabelFrame(self, width=240, height=60, text=i, font=("Arial", "12"))
            self.openInfoFrames[i].grid(pady=3, sticky=W, padx=3, column=self.column, row=self.counter)
            self.openInfoFrames[i].grid_propagate(False)
            
            self.openInfoValues[i] = StringVar()
            self.openInfoEntry[i] = Entry(self.openInfoFrames[i], textvariable=self.openInfoValues[i], font=("Arial", "15"), bg=self.cget("bg"), borderwidth=0) 
            self.openInfoEntry[i].grid(sticky=W)
            self.openInfoEntry[i].grid_propagate(False)
            self.openInfoValues[i].set(alunos[aluno][i]) 
            
            self.counter += 1
            if self.counter == 2:
                self.column += 1
                self.counter = 0
                
        self.saveButton = Button(self, text="Salvar", width=10, height=2, font=("Arial", "12"), command= lambda a=aluno: self.substituirInfo(a))
        self.saveButton.grid(column=3, row=0, pady=5)
        
        self.closeButton = Button(self, text="Cancelar", width=10, height=2, font=("Arial", "12"), command=self.refreshMainPage)
        self.closeButton.grid(column=4, row=0, pady=5)
    
    def substituirInfo(self, aluno):
        alunos[aluno] = {"Nome": self.openInfoEntry["Nome"].get(),
                        "Idade": self.openInfoEntry["Idade"].get(),
                        "Peso (Kg)": self.openInfoEntry["Peso (Kg)"].get(),
                        "Altura (cm)": self.openInfoEntry["Altura (cm)"].get(),
                        "Gênero": self.openInfoEntry["Gênero"].get()}
        
        
    def telaDeCadastro(self):
        self.clear()
        self.infoCadastro = ['Nome', 'Idade', 'Peso (Kg)','Altura (cm)', 'Gênero']
        self.cadastroLabel = {}
        self.cadastroEntry = {}
        
        self.cadastroFrame = Frame(self, width=300, height=520, highlightthickness=1, highlightbackground="black")
        self.cadastroFrame.pack(anchor=CENTER, pady=100)
        self.cadastroFrame.pack_propagate(False)
        
        for i in self.infoCadastro:
            self.cadastroLabel[i] = Label(self.cadastroFrame, text=i, font=("Arial", '16'))
            self.cadastroLabel[i].pack(anchor=W, padx=25)
            
            self.cadastroEntry[i] = Entry(self.cadastroFrame, font=("Arial", '16'))
            self.cadastroEntry[i].pack()
            
        self.errorLabel = Label(self.cadastroFrame, text="Preencha Todos os Campos!", fg=self.cget("bg"), font=("Arial", '16'))
        self.errorLabel.pack(pady=5)
            
        self.buttonsFrame = Frame(self.cadastroFrame)
        self.buttonsFrame.pack(pady=40)
            
        self.saveButton = Button(self.buttonsFrame, text="Salvar", font=("Arial", '16'), width=10, command=self.salvar)
        self.saveButton.pack(anchor=S, pady=5)
        
        self.cancelButton = Button(self.buttonsFrame, text="Cancelar", font=("Arial", '16'), width=10, command=self.refreshMainPage)
        self.cancelButton.pack(anchor=S, pady=5)
    
    def salvar(self):
        aluno = {"Nome": self.cadastroEntry["Nome"].get(),
                 "Idade": self.cadastroEntry["Idade"].get(),
                 "Peso (Kg)": self.cadastroEntry["Peso (Kg)"].get(),
                 "Altura (cm)": self.cadastroEntry["Altura (cm)"].get(),
                 "Gênero": self.cadastroEntry["Gênero"].get()}
        
        if aluno["Nome"] == "" or aluno["Idade"] == "" or aluno["Peso (Kg)"] == "" or aluno["Altura (cm)"] == "" or aluno["Gênero"] == "":
            self.errorLabel.configure(fg="red")
        else:
            alunos.append(aluno)
            self.refreshMainPage()
    
    def setupAgenda(self):
        agendaFrame = Frame(self.frameAgenda)
        agendaFrame.pack(pady=20)
        
        
        dateLabel = Label(agendaFrame, text="Data", font=("Arial", 12))
        dateLabel.grid(row=0, column=0, padx=10)
        self.dateEntry = DateEntry(agendaFrame, width=12, font=("Arial", 12))
        self.dateEntry.grid(row=0, column=1)
        
        
        taskLabel = Label(agendaFrame, text="Horario", font=("Arial", 12))
        taskLabel.grid(row=0, column=2, padx=10)
        self.taskEntry = Entry(agendaFrame, font=("Arial", 12))
        self.taskEntry.grid(row=0, column=3)
        
        self.labelHora = Label(self.frameAgenda, text="Tarefa", font=("Arial", 16))
        self.labelHora.pack(pady=10)

        self.entryHora = Entry(self.frameAgenda, width=50)
        self.entryHora.pack(pady=10)
        
        addButton = Button(agendaFrame, text="Adicionar", font=("Arial", 12), command=self.addTask)
        addButton.grid(row=0, column=4, padx=10)
        
       
        self.taskList = Listbox(self.frameAgenda, font=("Arial", 12), width=50)
        self.taskList.pack(pady=20)
        

        removeButton = Button(self.frameAgenda, text="Remover Tarefa", font=("Arial", 12), command=self.removeTask)
        removeButton.pack(pady=10)
    
    def addTask(self):
        task = f"{self.dateEntry.get()} - {self.taskEntry.get()} - {self.entryHora.get()}"
        self.taskList.insert(END, task)
    
    def removeTask(self):
        selectedTask = self.taskList.curselection()
        if selectedTask:
            self.taskList.delete(selectedTask)

if __name__ == "__main__":
    app = App()
    app.mainloop()
