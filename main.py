from tkinter import *
import translator, flashcard

class FlashcardSetup(Toplevel):
	def __init__(self):
		super().__init__()
		self.title('Flashcards Setup')
		Label(self, text='Set Width').grid(column=0, row=0)
		self.Width=Entry(self)
		self.Width.grid(column=1, row=0)
		Label(self, text='Set Height').grid(column=0,row=1)
		self.Height=Entry(self)
		self.Height.grid(column=1, row=1)
		Label(self, text='Set Margin').grid(column=0, row=2)
		self.Margin=Entry(self)
		self.Margin.grid(column=1, row=2)
		Label(self, text='Set Font Size').grid(column=0, row=3)
		self.Fontsize=Entry(self)
		self.Fontsize.grid(column=1, row=3)
		Button(self, text='Submit', command=self.submit).grid(column=0, row=4, sticky=E+W)
		Button(self, text='Cancel', command=self.destroy).grid(column=1, row=4, sticky=E+W)
		
	def submit(self):
		self.width=float(self.Width.get())
		self.height=float(self.Height.get())
		self.margin=float(self.Margin.get())
		self.fontsize=float(self.Fontsize.get())
		self.setups=[self.width, self.height, self.margin, self.fontsize]
		ls.receive(self.setups)

class LeftSide(Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.grid(sticky=N+S+E+W)
		self.createwidgets()
		self.width=100
		self.height=50
		self.fontsize=12
		self.margin=40
		
	def createwidgets(self):
		self.to_trans=Entry(self)
		self.to_trans.grid(column=0, row=0)
		self.word=Entry(self)
		self.word.grid(column=3, row = 0)
		Button(self, text='----->', command=self.doit).grid(column=2,row=0,sticky=E+W)
		Button(self,text='save', command=self.saveit).grid(column=2,row=1, sticky=E+W)
		Button(self, text='create flashcards', command=self.cards).grid(column=2, row=2,sticky=E+W)
		Button(self, text='flashcards options', command=self.opt).grid(column=2, row=3,sticky=E+W)
		Button(self, text='Exit', command=root.destroy).grid(column=2, row=4,sticky=E+W)
		#~ self.binding()
				
	def doit(self):
		self.tex=self.to_trans.get()
		self.word.delete(0, last=len(self.word.get()))
		self.res=translator.trans(self.tex).lower()
		self.word.insert(0,self.res)

	def saveit(self):
		self.to_write=self.tex+'-'+self.word.get()+'\n'
		with open('word_list.txt','a') as f:
			f.write(self.to_write)
			
	def cards(self):
		flashcard.create_cards(wid=self.width, hei=self.height,margin=self.margin,fontsize=self.fontsize)
	
	def opt(self):
		self.window=FlashcardSetup()
		
	def receive(self,setups):
		self.width,self.height,self.margin,self.fontsize=setups
		self.window.destroy()

root=Tk()
root.geometry()
ls=LeftSide(master=root)
root.mainloop()
