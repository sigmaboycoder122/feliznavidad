from tkinter import *
root = Tk()
root.title("Calculator")

content = ""
txtinput = StringVar(value="0")
# button input function

def btn(number):
    global content
    content = content+str(number)
    txtinput.set(content)

def execute():
    global content
    result = eval(content)
    txtinput.set(result)
    content = ""

def clear():
    global content
    content = ""
    txtinput.set(content)
    displayText.insert(0,"0")

# Text Display
displayText = Entry(font=('arial',40),fg="white",bg="gray",textvariable=txtinput, justify='right')
displayText.grid(columnspan=4)

# row1
btn7=Button(fg="black", font=('arial',20),text="7",padx=62,pady=15,command=lambda:btn(7)).grid(row=1,column=0)
btn8=Button(fg="black", font=('arial',20),text="8",padx=62,pady=15,command=lambda:btn(8)).grid(row=1,column=1)
btn9=Button(fg="black", font=('arial',20),text="9",padx=62,pady=15,command=lambda:btn(9)).grid(row=1,column=2)
btnc=Button(fg="black", bg="orange",font=('arial',20),text="C",padx=45,pady=15,command=clear).grid(row=1,column=3)

# row2
btn4=Button(fg="black", font=('arial',20),text="4",padx=62,pady=15,command=lambda:btn(4)).grid(row=2,column=0)
btn5=Button(fg="black", font=('arial',20),text="5",padx=62,pady=15,command=lambda:btn(5)).grid(row=2,column=1)
btn6=Button(fg="black", font=('arial',20),text="6",padx=62,pady=15,command=lambda:btn(6)).grid(row=2,column=2)
btnmultiply=Button(fg="black", bg="orange",font=('arial',20),text="x",padx=47,pady=15,command=lambda:btn("*")).grid(row=2,column=3)

# row3
btn1=Button(fg="black", font=('arial',20),text="1",padx=62,pady=15,command=lambda:btn(1)).grid(row=3,column=0)
btn2=Button(fg="black", font=('arial',20),text="2",padx=62,pady=15,command=lambda:btn(2)).grid(row=3,column=1)
btn3=Button(fg="black", font=('arial',20),text="3",padx=62,pady=15,command=lambda:btn(3)).grid(row=3,column=2)
btnplus=Button(fg="black",bg="orange", font=('arial',20),text="+",padx=45,pady=15,command=lambda:btn("+")).grid(row=3,column=3)

# row 4 
btn0=Button(fg="black", font=('arial',20),text="0",padx=62,pady=15,command=lambda:btn(0)).grid(row=4,column=0)
btndot=Button(fg="black", font=('arial',20),text=".",padx=62,pady=15,command=lambda:btn(".")).grid(row=4,column=1)
btndiv=Button(fg="black", bg="orange",font=('arial',20),text="/",padx=65,pady=15,command=lambda:btn("/")).grid(row=4,column=2)
btnsubt=Button(fg="black", bg="orange",font=('arial',20),text="-",padx=48,pady=15,command=lambda:btn("-")).grid(row=4,column=3)

# row 5
btnequal=Button(fg="black",bg="orange", font=('arial',20),text="=",padx=62,pady=15,command=execute).grid(row=5,column=0)
btnopenbrac=Button(fg="black",bg="orange", font=('arial',20),text="(",padx=62,pady=15,command=lambda:("(")).grid(row=5,column=1)
btnclosebrac=Button(fg="black",bg="orange", font=('arial',20),text=")",padx=62,pady=15,command=lambda:(")")).grid(row=5,column=2)

root.mainloop();