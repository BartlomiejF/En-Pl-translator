from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('LiberationSerif','/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf'))
todo=canvas.Canvas('english_flashcards.pdf')
done=canvas.Canvas('polish_flashcards.pdf')
todo.setFont('LiberationSerif',12)
done.setFont('LiberationSerif',12)

def create_cards():
	with open('word_list.txt','r') as f:
		x=f.readlines()

	z=0
	col=0
	for n in range(len(x)):
		if z==5:
			z=0
			col+=1
		eng=x[n].split('-')[0].strip()
		todo.rect(40+z*100,40+col*100,100,100)
		todo.drawString(50+z*100, 100+col*100,eng)
		z+=1
	z=0
	col=0
	for n in range(len(x)):
		if z==5:
			z=0
			col+=1
		pl=x[n].split('-')[1].strip()
		done.rect(40+z*100,40+col*100,100,100)
		done.drawString(50+z*100, 100+col*100,pl)
		z+=1
	todo.showPage()
	done.showPage()
	todo.save()
	done.save()
