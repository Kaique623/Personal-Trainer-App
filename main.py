from tkinter import *
from tkinter import ttk
import json

open('data/alunos.json', 'a+').close()
try:
    with open('data/alunos.json', 'r') as data:
        alunos = json.load(data)
except:
    alunos = []
frames = {}

listaTreinos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U']

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
        self.curNotebook = 2
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
        
        self.lastTab = 1
    
        self.newInfoFrame()
    
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
                self.FramesDict[num] = Frame(self.frameAlunos, width="1080", height="100", highlightthickness=2, highlightbackground="black")
                if alunos[num]["Pago"] == True:
                    self.FramesDict[num].config(highlightbackground="green2")
                else:
                    self.FramesDict[num].config(highlightbackground="red")
                    
                self.FramesDict[num].pack(anchor=W, pady=1)
                self.FramesDict[num].pack_propagate(False)
                self.FramesDict[num].bind("<Button-1>", lambda e, a=num: self.openInfo(a, '0'))
                
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
        
    def openInfo(self, aluno, tabaux):
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
                
        self.saveButton = Button(self, text="Salvar", width=10, height=2, font=("Arial", "12"), command= lambda a=aluno: self.substituirInfo(a, True))
        self.saveButton.grid(column=3, row=0, pady=5)
        
        self.closeButton = Button(self, text="Cancelar", width=10, height=2, font=("Arial", "12"), command=self.refreshMainPage)
        self.closeButton.grid(column=4, row=0, pady=5)
        
        self.adicionar = Button(self, text="Adicionar Treino", width=23, height=2, font=("Arial", "12"), command= lambda a=aluno: self.novoTreino(a))
        self.adicionar.grid(column=2, row=1)
    
        self.treinos = {}
    
        self.fichaFrame = ttk.Notebook(self, width=1070, height=600)
        self.fichaFrame.grid(columnspan=10, row=4, padx=5, pady=10)
        
        self.exercicioNovo = Button(self, text="Adicionar Exercicio", width=23, height=2, font=("Arial", "12"), command=lambda a=aluno: self.adicionarExercicio(self.fichaFrame.select(), a))
        self.exercicioNovo.grid(column=3, row=1, columnspan=2)
        
        self.pagamentoBoolean = BooleanVar()
        self.framePagamento = Label(self, text="Status de Pagamento", font=("Arial", "12"))
        self.framePagamento.grid(pady=3, sticky=W, padx=3, column=0, row=2)
        
        self.checkbuttonFrame = Frame(self, width=240, height=60)
        self.checkbuttonFrame.grid(column=0, row=3, sticky=W)
        
        self.checkButton1 = Checkbutton(self.checkbuttonFrame, text="Pago", variable=self.pagamentoBoolean, onvalue=True, offvalue=False, font=("Arial", "12"))
        self.checkButton1.grid(column=0, row=0, sticky=W)
        
        self.checkButton2 = Checkbutton(self.checkbuttonFrame, text="Pendente", variable=self.pagamentoBoolean, onvalue=False, offvalue=True, font=("Arial", "12"))
        self.checkButton2.grid(column=1, row=0, sticky=W)

        self.pagamentoBoolean.set(alunos[aluno]["Pago"])

        self.exercise = {}
        for i in alunos[aluno]["Ficha"].keys():
            self.treinos[i] = Frame(self.fichaFrame, width=1066, height=600, highlightthickness=1, highlightbackground="black")
            self.treinos[i].grid()
            self.fichaFrame.add(self.treinos[i], text=f"Treino {i}")
            
            self.labelFrame = Frame(self.treinos[i], width=1066, height=40, highlightthickness=1, highlightbackground="black")
            self.labelFrame.grid()
            self.labelFrame.grid_propagate(False)
            self.exercise[i] = {}
            self.contador = 0
            self.curRow = 1
            for ex in ['Exercício', 'Série', 'Rep.', 'Carga', 'Intervalo']:
                self.exerciciosFrame = Frame(self.labelFrame, width=213, height=39, highlightthickness=1, highlightbackground="black")
                self.exerciciosFrame.grid(column=self.contador, row=0)
                self.exerciciosFrame.grid_propagate(False)
                Label(self.exerciciosFrame, text=ex, font=("Arial", 16)).grid(row=0, pady=4, sticky=W)
                
                self.contador += 1
            
            for a in alunos[aluno]["Ficha"][i]:
                    self.exercise[i][a] = {}
                    self.exercise[i][a]['Frame'] = Frame(self.treinos[i], width=213*5, height=39, highlightthickness=1, highlightbackground="black")
                    self.exercise[i][a]['Frame'].grid(column=0, row=self.curRow)
                    self.exercise[i][a]['Frame'].grid_propagate(False)
                    
                    self.exercise[i][a]['StringNome'] = StringVar()
                    self.exercise[i][a]['EntryNome'] = Entry(self.exercise[i][a]['Frame'], textvariable=self.exercise[i][a]['StringNome'], width=14, font=('Arial', 20))
                    self.exercise[i][a]['EntryNome'].grid(column=0, row=self.curRow)
                    self.exercise[i][a]['StringNome'].set(a)
                    
                    self.exercise[i][a]['StringSérie'] = StringVar()
                    self.exercise[i][a]['EntrySérie'] = Entry(self.exercise[i][a]['Frame'], textvariable=self.exercise[i][a]['StringSérie'], width=14, font=('Arial', 20))
                    self.exercise[i][a]['EntrySérie'].grid(column=1, row=self.curRow)
                    self.exercise[i][a]['StringSérie'].set(alunos[aluno]["Ficha"][i][a][0])
                    
                    self.exercise[i][a]['StringRep'] = StringVar()
                    self.exercise[i][a]['EntryRep'] = Entry(self.exercise[i][a]['Frame'], textvariable=self.exercise[i][a]['StringRep'], width=14, font=('Arial', 20))
                    self.exercise[i][a]['EntryRep'].grid(column=2, row=self.curRow)
                    self.exercise[i][a]['StringRep'].set(alunos[aluno]["Ficha"][i][a][1])
                    
                    self.exercise[i][a]['StringCarga'] = StringVar()
                    self.exercise[i][a]['EntryCarga'] = Entry(self.exercise[i][a]['Frame'], textvariable=self.exercise[i][a]['StringCarga'], width=14, font=('Arial', 20))
                    self.exercise[i][a]['EntryCarga'].grid(column=3, row=self.curRow)
                    self.exercise[i][a]['StringCarga'].set(alunos[aluno]["Ficha"][i][a][2])
                    
                    self.exercise[i][a]['StringIntervalo'] = StringVar()
                    self.exercise[i][a]['EntryIntervalo'] = Entry(self.exercise[i][a]['Frame'], textvariable=self.exercise[i][a]['StringIntervalo'], width=7, font=('Arial', 20))
                    self.exercise[i][a]['EntryIntervalo'].grid(column=4, row=self.curRow)
                    self.exercise[i][a]['StringIntervalo'].set(alunos[aluno]["Ficha"][i][a][3])
                    
                    self.removeButton = Button(self.exercise[i][a]['Frame'], text="Remover", width=8, font=("Arial", 14), command= lambda i =i, a=a, tabaux=tabaux, aluno=aluno: self.delete(i, a, tabaux, aluno))
                    self.removeButton.grid(column=5, row=self.curRow)
                    self.contador = 0
                    
                    self.contador += 1
                    self.curRow += 1
            try:
                self.fichaFrame.select(tabaux)
            except:
                pass
    def delete(self, i, a, tab, aluno):
        self.substituirInfo(aluno, False)        
        del alunos[aluno]["Ficha"][i][self.exercise[i][a]['StringNome'].get()]
        self.clear()
        tab = tab.replace(f'.!notebook{str(self.curNotebook)}.!frame', '')
        self.curNotebook += 1  
        if tab == '':
            tab = 1
        tab = int(tab) 
        self.openInfo(aluno, f'.!notebook{str(self.curNotebook)}.!frame{tab}')
    
    
    def adicionarExercicio(self, tab, aluno):
        try:
            self.substituirInfo(aluno, False)
            tab = tab.replace(f'.!notebook{str(self.curNotebook)}.!frame', '')
            self.curNotebook += 1  
            if tab == '':
                tab = 1
            tab = int(tab) 
            tab = tab-1 
            alunos[aluno]["Ficha"][listaTreinos[tab]]['NovoExercicio'] = [0, 0, 0, 0]
            self.clear()
            self.openInfo(aluno, f'.!notebook{str(self.curNotebook)}.!frame{tab + 1}')
        except:
            self.adicionarExercicio(tab, aluno)   
                 
    def substituirInfo(self, aluno, sair):
        fichasaux = {}
        for i in alunos[aluno]["Ficha"].keys():
            fichasaux[i] = {}
            for a in alunos[aluno]["Ficha"][i]:
                fichasaux[i][self.exercise[i][a]['StringNome'].get()] = [self.exercise[i][a]['StringSérie'].get(), self.exercise[i][a]['StringRep'].get(), self.exercise[i][a]['StringCarga'].get(), self.exercise[i][a]['StringIntervalo'].get()]
        
        alunos[aluno] = {"Nome": self.openInfoEntry["Nome"].get(),
                        "Idade": self.openInfoEntry["Idade"].get(),
                        "Peso (Kg)": self.openInfoEntry["Peso (Kg)"].get(),
                        "Altura (cm)": self.openInfoEntry["Altura (cm)"].get(),
                        "Gênero": self.openInfoEntry["Gênero"].get(),
                        "Pago": self.pagamentoBoolean.get(),
                        "Ficha": []
                        }
        
        alunos[aluno]["Ficha"] = fichasaux
        
        with open('data/alunos.json', 'w') as data:
            json.dump(alunos, data)

        print("Informação Salva!")
        if sair:
            self.refreshMainPage()
    
    def novoTreino(self, aluno):     
        self.substituirInfo(aluno, False) 
        aux = len(alunos[aluno]["Ficha"])
        alunos[aluno]["Ficha"][listaTreinos[aux]] = {'Exercício 1': [0, 0, 0, 0]}
        self.clear()
        self.openInfo(aluno, '0')
        
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
        self.canSave = True
        
        for i in self.cadastroEntry:
            if self.cadastroEntry[i].get() == '':
                self.canSave = False
        if self.canSave:
            alunos.append({"Nome": self.cadastroEntry["Nome"].get(),
                        "Idade": self.cadastroEntry["Idade"].get(),
                        "Peso (Kg)": self.cadastroEntry["Peso (Kg)"].get(),
                        "Altura (cm)": self.cadastroEntry["Altura (cm)"].get(),
                        "Gênero": self.cadastroEntry["Gênero"].get(),
                        "Pago": False,
                        "Ficha": {"A": {"Exercicio1": [0, 0, 0, 0]}}})
            self.refreshMainPage()
        else:
            self.errorLabel.config(fg="red")
        
if __name__ == "__main__":
    root = App()
    root.mainloop()