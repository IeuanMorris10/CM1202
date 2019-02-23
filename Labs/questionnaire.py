from tkinter import *
#from Response import Response

class Questionnaire(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        createProgSelect(self)
        createTeamExperience(self)
        createProblems(self)
        createComment(self)
        createButtons(self)
        clearResponse(self)
        self.grid()

def createProgSelect(self):
    # Create widgets to select a degree programme from a list
    lblProg = Label(self, text='Degree Programme:', font=('MS', 8,'bold'))
    lblProg.grid(row=0, column=0, columnspan=2, sticky=W)
    self.listProg = Listbox(self, height= 3)
    scroll = Scrollbar(self, command= self.listProg.yview)
    self.listProg.configure(yscrollcommand=scroll.set)
    self.listProg.grid(row=0, column=2, columnspan=2, sticky=NE)
    scroll.grid(row=0, column=4, sticky=W)
    for item in ["CS", "CS with", "BIS", "SE", "Joints",""]:
        self.listProg.insert(END, item)
    self.listProg.selection_set(END)

def createTeamExperience(self):
    lblTeamExp = Label(self, text="Team Experience:", font=('MS', 8,'bold'))
    lblTeamExp.grid(row=4, column=0, columnspan=2, sticky=W)
    lblExp1 = Label(self, text="1. Our team worked together effectively", font=('MS', 8))
    lblExp1.grid(row=5, column=0, columnspan=4, sticky=W)
    lblExp2 = Label(self, text="2. Our team produced good quality products", font=('MS', 8))
    lblExp2.grid(row=6, column=0, columnspan=4, sticky=W)
    lblExp3 = Label(self, text="3.  I enjoyed working in our team", font=('MS', 8))
    lblExp3.grid(row=7, column=0, columnspan=4, sticky=W)

    self.varQ1 = IntVar()
    self.varQ2 = IntVar()
    self.varQ3 = IntVar()

    lblStrAgr = Label(self, text = 'Strongly \n Disagree', font=('MS', 8,'bold'))
    lblStrAgr.grid(row=3, column= 4, rowspan=2)
    R1Q1 = Radiobutton(self, variable=self.varQ1, value=1)
    R1Q1.grid(row=5, column=4)
    R1Q2 = Radiobutton(self, variable=self.varQ2, value=1)
    R1Q2.grid(row=6, column=4)
    R1Q3 = Radiobutton(self, variable=self.varQ3, value=1)
    R1Q3.grid(row=7, column=4)


    lblStrAgr = Label(self, text = 'Partly \n Agree', font=('MS', 8,'bold'))
    lblStrAgr.grid(row=3, column= 5, rowspan=2)
    R2Q1 = Radiobutton(self, variable=self.varQ1, value=2)
    R2Q1.grid(row=5, column=5)
    R2Q2 = Radiobutton(self, variable=self.varQ2, value=2)
    R2Q2.grid(row=6, column=5)
    R2Q3 = Radiobutton(self, variable=self.varQ3, value=2)
    R2Q3.grid(row=7, column=5)

    lblStrAgr = Label(self, text = 'Partly \n Disagree', font=('MS', 8,'bold'))
    lblStrAgr.grid(row=3, column= 6, rowspan=2)
    R3Q1 = Radiobutton(self, variable=self.varQ1, value=3)
    R3Q1.grid(row=5, column=6)
    R3Q2 = Radiobutton(self, variable=self.varQ2, value=3)
    R3Q2.grid(row=6, column=6)
    R3Q3 = Radiobutton(self, variable=self.varQ3, value=3)
    R3Q3.grid(row=7, column=6)

    lblStrAgr = Label(self, text = 'Strongly \n Disagree', font=('MS', 8,'bold'))
    lblStrAgr.grid(row=3, column= 7, rowspan=2)
    R4Q1 = Radiobutton(self, variable=self.varQ1, value=4)
    R4Q1.grid(row=5, column=7)
    R4Q2 = Radiobutton(self, variable=self.varQ2, value=4)
    R4Q2.grid(row=6, column=7)
    R4Q3 = Radiobutton(self, variable=self.varQ3, value=4)
    R4Q3.grid(row=7, column=7)

def createProblems(self):
    #Create Widgets to show Problems experienced
    lblProb1 = Label(self, text='Problems:', font=('MS', 8,'bold'))
    lblProb1.grid(row=8, column = 0)
    lblProb2 = Label(self, text='Our team often experienced the ' +
    'following problems (choose all that apply):')
    lblProb2.grid(row=8, column = 1, columnspan=6, sticky=W)

    self.varCB1 = IntVar()
    CB1 = Checkbutton(self, text=" Poor Communication", variable=self.varCB1)
    CB1.grid(row=9, column=0, columnspan=4, sticky=W)

    self.varCB2 = IntVar()
    CB1 = Checkbutton(self, text=" Lack of Direction ", variable=self.varCB2)
    CB1.grid(row=10, column=0, columnspan=4, sticky=W)

    self.varCB3 = IntVar()
    CB1 = Checkbutton(self, text=" Disagreements Amongst Team ", variable=self.varCB3)
    CB1.grid(row=11, column=0, columnspan=4, sticky=W)

    self.varCB4 = IntVar()
    CB1 = Checkbutton(self, text=" Members Missing Meetings ", variable=self.varCB4)
    CB1.grid(row=9, column=4, columnspan=4, sticky=W)

    self.varCB5 = IntVar()
    CB1 = Checkbutton(self, text=" Members Not Contributing", variable=self.varCB5)
    CB1.grid(row=10, column=4, columnspan=4, sticky=W)

    self.varCB6 = IntVar()
    CB1 = Checkbutton(self, text=" Members Not Motivated", variable=self.varCB6)
    CB1.grid(row=11, column=4, columnspan=4, sticky=W)

def createComment(self):
    lblComm = Label(self, text='Comments about teamwork:', font=('MS', 8,'bold'))
    lblComm.grid(row=12, column = 0, columnspan=2)
    self.txtComment = Text(self, height=3,width=40)
    scroll = Scrollbar(self, command=self.txtComment.yview)
    self.txtComment.configure(yscrollcommand=scroll.set)
    self.txtComment.grid(row=12, column=0,columnspan=7, sticky=E)
    scroll.grid(row=12, column=7, sticky=W)

    lblName = Label(self, text='Name (optional):', font=('MS', 8,'bold'))
    lblName.grid(row=15, column = 1, columnspan=2)
    self.entName = Entry(self)
    self.entName.grid(row=15, column=3, columnspan=2, sticky=E)

def createButtons(self):
    btnSubmit = Button(self, text='Submit',font=('MS', 8,'bold'))
    #btnClear['command']=self.clearResponse #Note: no () after the method
    btnSubmit.grid(row=16, column=2, columnspan=2)

    btnClear = Button(self, text='Clear',font=('MS', 8,'bold'))
    #btnClear['command']=self.clearResponse #Note: no () after the method
    btnClear.grid(row=16, column=4, columnspan=2, command=clearResponse(self))

def storeResponse(self):
    index = self.listProg.curselection()[0]
    strProg = str(self.listProg.get(index))
    strMsg=""
    if strProg == "":
        strMsg = "You need to select a Degree Programme. "

    if (self.varQ1.get()== 0) or (self.varQ2.get() == 0) or (self.varQ3.get() == 0):
        strMsg = strMsg + "You need to answer all Team Experience Questions"

def clearResponse(self):
    self.listProg.selection_clear(0,END)
    self.listProg.selection_set(END)

    self.varQ1.set(0)
    self.varQ2.set(0)
    self.varQ3.set(0)

    self.varCB1.set(0)
    self.varCB2.set(0)
    self.varCB3.set(0)
    self.varCB4.set(0)
    self.varCB5.set(0)
    self.varCB6.set(0)

    self.entName.delete(0, END)
    self.txtComment.delete(1.0, END)

root = Tk()
root.title("Teamwork Questionnaire")
app = Questionnaire(root)
root.mainloop()


class Response:
    def __init__(self, respNo="", prog="", q1=0, q2=0,q3=0, pr1=0, pr2=0, pr3=0, pr4=0, pr5=0, pr6=0, comment="", name=""):
        self.respNo = respNo
        self.prog = prog
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.pr1 = pr1
        self.pr2 = pr2
        self.pr3 = pr3
        self.pr4 = pr4
        self.pr5 = pr5
        self.pr6 = pr6
        self.comment = comment
        self.name = name
