from tkinter import *
import translator, flashcard

class LeftSide(Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.grid(sticky=N+S+E+W)
		self.createwidgets()
		
	def createwidgets(self):
		self.to_trans=Entry(self)
		self.to_trans.grid(column=0, row=0)
		self.word=Entry(self)
		self.word.grid(column=3, row = 0)
		Button(self, text='--->', command=self.doit).grid(column=2,row=0)
		Button(self,text='save', command=self.saveit).grid(column=1, columnspan=2,row=1, sticky=E+W)
		Button(self, text='create flashcards', command=self.cards).grid(column=2, row=2)
		
	def doit(self):
		self.tex=self.to_trans.get()
		self.word.delete(0, last=len(self.word.get()))
		self.res=translator.trans(self.tex)
		self.word.insert(0,self.res)

	def saveit(self):
		self.to_write=self.tex+'-'+self.res+'\n'
		with open('word_list.txt','a') as f:
			f.write(self.to_write)
			
	def cards(self):
		flashcard.create_cards()

root=Tk()
root.geometry()
LeftSide(master=root)
root.mainloop()
