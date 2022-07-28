from tkinter import *
from random import randint

number_of_number=3
outcome=""																																																																		


def buton_situation():
	global buton
	buton=1
	global users_input
	users_input=user.get()+" "
	root.destroy()
	root.mainloop()

	
while (True):
	
	level=number_of_number-2
	for sayi in range(1,number_of_number+1):
		root=Tk()
		root.title("Level %d" %(level))	
		number=randint(1,9)																	
		strnumber=str(number)							
		number_of_blank=randint(-65,65)															
		if   number_of_blank>=0 :location_of_number=(" "*number_of_blank)+strnumber				
		else	 			    :location_of_number=strnumber+(" "*abs(number_of_blank))									
		letter=str(sayi)+". Number"																
		label =Label(root,text=letter, font='Helvetica 18 bold')
		label.configure(foreground="darkblue")		
		label.pack(padx=130, pady=30)
		label =Label(root,text=location_of_number, font='Helvetica 18')
		label.configure(foreground="blue")
		label.pack(pady=30)
		root.after(2000,lambda:root.destroy())
		root.mainloop()
		outcome+=strnumber
		outcome+=" "
	
	
	root=Tk()
	root.title("Result Scane")
	screen=Label(root,text="Please Enter Results", fg="darkblue",font='Helvetica 15')
	user=Entry(root)
	screen.grid(row=0,padx=50, pady=70)
	user.grid(row=0, column=1,padx=50, pady=30)
	buton=Button(root,text="OK",command=buton_situation, bg="green",font='Helvetica 15')
	buton.place(x=173,y=126)
	butonx=Button(root,text="QUIT", command=quit, bg="red", font='Helvetica 15')
	butonx.place(x=287,y=126)
	root.mainloop()
	
	if buton==1:
		if outcome==users_input:
			root=Tk()
			outcome=""
			label =Label(root,text="Congratulation!", fg="green3",font='Helvetica 15 bold')
			label.pack(padx=100, pady=30)
			label =Label(root,text="Next Level=%d" %(level+1),fg="green3",font='Helvetica 15')
			label.pack(padx=100, pady=30)
			number_of_number=number_of_number+1
			root.after(2000,lambda:root.destroy())
			root.mainloop()
		else :
			root=Tk()
			outcome=""
			label =Label(root,text="GAME OVER",fg="red",font='Helvetica 20 bold')
			label.pack(padx=100, pady=50)
			root.after(2000,lambda:root.destroy())
			root.mainloop()
			break
			
