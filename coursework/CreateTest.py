from tkinter import *
from tkinter import messagebox
import csv
import datetime
from datetime import timedelta


class CreateTest(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        FOS_Choice(self)
        Date_Choice(self)
        Question_Choice(self)
        Create_Buttons(self)
        self.grid()


def FOS_Choice(self):
    lblChoice = Label(self, text="Choose the type of test:", font=('MS', 15,'bold'))
    lblChoice.grid(row=0, column=0, columnspan=2, sticky=W)
    lblFormative = Label(self, text="Formative", font=('MS', 15))
    lblFormative.grid(row=1, column=0, columnspan=2)
    lblSummative = Label(self, text="Summative", font=('MS', 15))
    lblSummative.grid(row=1, column=6, columnspan=3, sticky=W)

    self.varChoice = IntVar()

    rbFormative = Radiobutton(self, variable=self.varChoice, value=1)
    rbFormative.grid(row=1, column=2, sticky=W)
    rbSummative = Radiobutton(self, variable=self.varChoice, value=2)
    rbSummative.grid(row=1, column=9, sticky=W)

def Date_Choice(self):
    lblChoice = Label(self, text="Choose the start / end dates:", font=('MS', 15,'bold'))
    lblChoice.grid(row=2, column=0, columnspan=2, sticky=W)

    lblStart = Label(self, text="Start Date:", font=('MS', 15))
    lblStart.grid(row=3, column=0, columnspan=4)
    lblEnd = Label(self, text="Due Date:", font=('MS', 15))
    lblEnd.grid(row=3, column=6, columnspan=4, sticky=W)

    now = datetime.datetime.now()

    startDate = Listbox(self, exportselection=0)
    for day in range(0, 30):
        dateFormat = (now + datetime.timedelta(days=day)).strftime("%d/%m/%y")
        startDate.insert(END, dateFormat)

    endDate = Listbox(self, exportselection=0)
    for day in range(1, 60):
        dateFormat = (now + datetime.timedelta(days=day)).strftime("%d/%m/%y")
        endDate.insert(END, dateFormat)

    endDate.grid(row=4, column=5, columnspan=5)
    startDate.grid(row=4, column=0, columnspan=5)

    return startDate

def Question_Choice(self):
    lblChooseQ = Label(self, text='Choose questions for test:', font=('MS', 15,'bold'))
    lblChooseQ.grid(row=8, column = 0, sticky=W)

    self.varCB1 = IntVar()
    CB1 = Checkbutton(self, text="Q: What is the capital of France, A: Paris", variable=self.varCB1)
    CB1.grid(row=9, column=0, columnspan=4, sticky=W)

    self.varCB2 = IntVar()
    CB1 = Checkbutton(self, text="Q: What does RAM stand for, A: Random Access Memory", variable=self.varCB2)
    CB1.grid(row=10, column=0, columnspan=4, sticky=W)

    self.varCB3 = IntVar()
    CB1 = Checkbutton(self, text="Q: 23 + 2, A: 25", variable=self.varCB3)
    CB1.grid(row=11, column=0, columnspan=4, sticky=W)

    self.varCB4 = IntVar()
    CB1 = Checkbutton(self, text="Q: , A:", variable=self.varCB4)
    CB1.grid(row=12, column=0, columnspan=4, sticky=W)

    self.varCB5 = IntVar()
    CB1 = Checkbutton(self, text="Q: , A:", variable=self.varCB5)
    CB1.grid(row=13, column=0, columnspan=4, sticky=W)

    self.varCB6 = IntVar()
    CB1 = Checkbutton(self, text="Q: , A:", variable=self.varCB6)
    CB1.grid(row=14, column=0, columnspan=4, sticky=W)

    self.varCB7 = IntVar()
    CB1 = Checkbutton(self, text="Q: What is the capital of Spain, A: Madrid", variable=self.varCB7)
    CB1.grid(row=9, column=6, columnspan=4, sticky=W)

    self.varCB8 = IntVar()
    CB1 = Checkbutton(self, text="Q: What does ROM stand for, A: Read Only Memory", variable=self.varCB8)
    CB1.grid(row=10, column=6, columnspan=4, sticky=W)

    self.varCB9 = IntVar()
    CB1 = Checkbutton(self, text="Q: 1 + 1, A: 2", variable=self.varCB9)
    CB1.grid(row=11, column=6, columnspan=4, sticky=W)

    self.varCB10 = IntVar()
    CB1 = Checkbutton(self, text="Q: , A:", variable=self.varCB10)
    CB1.grid(row=12, column=6, columnspan=4, sticky=W)

    self.varCB11 = IntVar()
    CB1 = Checkbutton(self, text="Q: , A:", variable=self.varCB11)
    CB1.grid(row=13, column=6, columnspan=4, sticky=W)

    self.varCB12 = IntVar()
    CB1 = Checkbutton(self, text="Q: , A:", variable=self.varCB12)
    CB1.grid(row=14, column=6, columnspan=4, sticky=W)

def Create_Buttons(self):
    lblBlank = Label(self, text="  ")
    lblBlank.grid(row=15, column = 0, sticky=W)

    btnSubmit = Button(self, text='Create Test', width=10, font=('MS', 8,'bold'))
    btnSubmit.grid(row=16, column=0, columnspan=3)

    btnClear = Button(self, text='Clear', width=10, font=('MS', 8,'bold'), command=Confirm_test)
    btnClear.grid(row=16, column=2, columnspan=3)

    btnCancel = Button(self, text='Cancel', width=10, font=('MS', 8,'bold'))
    btnCancel.grid(row=16, column=4, columnspan=3, padx=65)

def Confirm_test(startDate):
    #This piece of code reads the value of the listbox
    wrtStartDate=str((startDate.get(ACTIVE)))
    print(wrtStartDate)


    '''
    classRoom = classR.get()
    lessonChoice = lessonVar.get()
    departmentChoice = departmentVar.get()
    harwdareChoice = hardwareVar.get()

    #open the file to append
    fileObject = open("Bookings.csv","a")
    #This code writes the values of each piece in a seperate column
    writeFileObject = csv.writer(fileObject)
    writeFileObject.writerow([teacherID , teacherName , harwdareChoice , lessonChoice , dateChoice , classRoom , departmentChoice])
    fileObject.close()
    '''


root = Tk()
root.title("Create Test")
app = CreateTest(root)
root.mainloop()
