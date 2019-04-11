import tkinter as tk
import numpy as np
import math

LARGE_FONT = ("Verdana", 12) #default font used throughout the GUI

window = tk.Tk()
window.title("Simon's Calculator Project")
window.geometry("1000x800")
frame=tk.Frame(window)
frame.pack(side="top", fill = "both", expand = True)
label = tk.Label(frame, text = "Simon's Calculator Project", font = LARGE_FONT)
label.pack(pady=10,padx=10)

	

screenFrame=tk.Frame(frame,width=100,height=5,bg='#ffffff',
	borderwidth=1,relief='sunken')
scrollbar = tk.Scrollbar(screenFrame) 
screenArea = tk.Text(screenFrame, width=100, height=5, wrap="none",
			yscrollcommand=scrollbar.set,
			borderwidth=0, highlightthickness=0)
scrollbar.config(command=screenArea.yview)
scrollbar.pack(side="right", fill="y")
screenArea.pack(side="left",fill="both",expand=True)
screenArea.config(state=tk.DISABLED)
screenArea.config(font=("Times New Roman", 24))
screenArea.tag_config("a",justify=tk.CENTER,)

screenFrame.pack(side=tk.TOP)


buttonsFrame = tk.Frame(frame,width=240,height=240,bg='#ffffff',
			borderwidth=1,relief='sunken')
buttonsFrame.pack()
aFill = False

num1 = tk.StringVar()
num2 = tk.StringVar()
num1.set('')
num2.set('')

operationVar = tk.StringVar()
operationVar.set("")

button0 = tk.Button(buttonsFrame,text="0",
	command = lambda: setNum('0'),height=5,width=5)
button1 = tk.Button(buttonsFrame,text="1",
	command = lambda: setNum('1'),height=5,width=5)

button2 = tk.Button(buttonsFrame,text="2",
	command = lambda: setNum('2'),height=5,width=5)

button3 = tk.Button(buttonsFrame,text="3",
	command = lambda: setNum('3'),height=5,width=5)

button4 = tk.Button(buttonsFrame,text="4",
	command = lambda: setNum('4'),height=5,width=5)
button5 = tk.Button(buttonsFrame,text="5",
	command = lambda: setNum('5'),height=5,width=5)

button6 = tk.Button(buttonsFrame,text="6",
	command = lambda: setNum('6'),height=5,width=5)

button7 = tk.Button(buttonsFrame,text="7",
	command = lambda: setNum('7'),height=5,width=5)

button8 = tk.Button(buttonsFrame,text="8",
	command = lambda: setNum('8'),height=5,width=5)

button9 = tk.Button(buttonsFrame,text="9",
	command = lambda: setNum('9'),height=5,width=5)

decimalButton = tk.Button(buttonsFrame,text=".",
	command=lambda:setNum('.'),height=5,width=5)

addButton = tk.Button(buttonsFrame,text="+",
	command=lambda:setOperation("+"),height=10,width=5)

subtractButton=tk.Button(buttonsFrame,text='-',
	command=lambda:setOperation("-"),height=5,width=5)

multiplyButton = tk.Button(buttonsFrame,text="*",
	command = lambda: setOperation("*"),height=5,width=5)

divideButton=tk.Button(buttonsFrame,text="/",
	command=lambda:setOperation("/"),height=5,width=5)

equalButton=tk.Button(buttonsFrame,text='=',
	command = lambda:equals(),height=5,width=5)

clearButton = tk.Button(buttonsFrame,text="clear",
	command = lambda:clear_screen(),height=5,width=5)
sqrtButton=tk.Button(buttonsFrame,text='sqrt',
	command=lambda:sqrt(),height=5,width=5)

exponButton=tk.Button(buttonsFrame,text='^',
	command=lambda:setOperation("^"),height=5,width=5)
button0.grid(row=4,column=0,columnspan=1,padx=5,pady=5)
button1.grid(row=1,column=0,padx=5,pady=5)
button2.grid(row=1,column=1,padx=5,pady=5)
button3.grid(row=1,column=2,padx=5,pady=5)
button4.grid(row=2,column=0,padx=5,pady=5)
button5.grid(row=2,column=1,padx=5,pady=5)
button6.grid(row=2,column=2,padx=5,pady=5)
button7.grid(row=3,column=0,padx=5,pady=5)
button8.grid(row=3,column=1,padx=5,pady=5)
button9.grid(row=3,column=2,padx=5,pady=5)
decimalButton.grid(row=4,column=1,padx=5,pady=5)
addButton.grid(row=3,column=3,rowspan=2,padx=5,pady=5)
subtractButton.grid(row=2,column=3,padx=5,pady=5)
multiplyButton.grid(row=1,column=3,padx=5,pady=5)
divideButton.grid(row=0,column=3,padx=5,pady=5)
equalButton.grid(row=4,column=2,padx=5,pady=5)
clearButton.grid(row=0,column=0,padx=5,pady=5)
sqrtButton.grid(row=0,column=1,padx=5,pady=5)
exponButton.grid(row=0,column=2,padx=5,pady=5)

def setNum(input):
	if operationVar.get()=="":
		aFill=True
		if num1.get() == '':
			num1.set(input)
			insert_answer(num1.get())
		else:
			newInput = num1.get() + input
			num1.set(newInput)
			insert_answer(input)
			newInput=''
	else:
		if num2.get()=='':
			num2.set(input)
			insert_answer(num2.get())
		else:
			newInput = num2.get() + input
			num2.set(newInput)
			insert_answer(input)
			newInput=''

def setOperation(text):
	if operationVar.get() == '':
		operationVar.set(text)
		insert_answer(operationVar.get())
	elif (operationVar.get() == '*') or (operationVar.get() == '+') or (operationVar.get() == '-') or (operationVar.get() == '/') or (operationVar.get( ) == '^'):
		equals()
	else:
		operationVar.set('')
		operationVar.set(text)
		insert_answer(operationVar.get())

def equals():
	operation=operationVar.get()
	a = num1.get()
	b = num2.get()
	a = float(a)
	b = float(b)
	if operation == "+":
		ans = a+b
	elif operation == "-":
		ans = a-b
	elif operation == "*":
		ans = a*b
	elif operation == "/":
		if b ==0:
			clear_screen()
			insert_answer("Are you actually trying to divide by zero? I don't think so :)")
			return
		else:
			ans = a/b
	elif operation == "^":
		ans = a**b
	elif operation == "":
		insert_answer("Error")
	ans = str(ans)
	insert_answer('\n' + str(a) + operationVar.get() + str(b) + "=" + ans+"\n")
	num1.set(ans)
	num2.set('')
	operationVar.set('')
	screenArea.see(tk.END)

def sqrt():
	a = num1.get()
	a = float(a)
	ans = math.sqrt(a)
	insert_answer('\n' + 'sqrt('+str(a)+') = ' + str(ans) + '\n')

	

def insert_answer(text):
	screenArea.config(state=tk.NORMAL)
	screenArea.insert(tk.INSERT,text,"a")
	screenArea.update()
	screenArea.config(state=tk.DISABLED)
def clear_screen():
	num1.set('')
	num2.set('')
	operationVar.set('')
	screenArea.config(state=tk.NORMAL)
	screenArea.delete('1.0',tk.END)
	screenArea.update()
	screenArea.config(state=tk.DISABLED) 

if __name__ == "__main__":
	window.mainloop()