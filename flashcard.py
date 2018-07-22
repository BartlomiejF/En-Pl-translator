from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4

pdfmetrics.registerFont(TTFont('LiberationSerif','/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf'))
width,height=A4

def create_cards(wid=100,hei=50,margin=40, fontsize=12):
	
	todo=canvas.Canvas('english_flashcards.pdf', pagesize=A4)
	done=canvas.Canvas('polish_flashcards.pdf', pagesize=A4)
	todo.setFont('LiberationSerif',fontsize)
	done.setFont('LiberationSerif',fontsize)
	
	with open('word_list.txt','r') as f:
		x=f.readlines()
	
	temp_width=margin
	temp_height=margin
	
	for n in range(len(x)):
		if (width-temp_width)>(wid+margin):
			eng=x[n].split('-')[0].strip().lower()
			todo.rect(temp_width,temp_height,wid,hei)
			todo.drawString(temp_width+10, temp_height+(hei*2/5),eng)
			temp_width+=wid
		elif (height-temp_height)<(hei+margin):
			todo.showPage()
			todo.setFont('LiberationSerif',fontsize)
			temp_width=margin
			temp_height=margin
		else:
			temp_height+=hei
			temp_width=margin

	temp_width=int(width)-margin
	temp_height=margin


	for n in range(len(x)):
		if (temp_width-wid)>margin:
			pl=x[n].split('-')[1].strip().lower()
			done.rect(temp_width-wid,temp_height,wid,hei)
			done.drawString(temp_width-wid+10, temp_height+(hei*2/5),pl)
			temp_width-=wid
		elif (height-temp_height)<(hei+margin):
			done.showPage()
			done.setFont('LiberationSerif',fontsize)
			temp_height=margin
			temp_width=int(width)-margin
		else:
			temp_height+=hei
			temp_width=int(width)-margin
	
	todo.showPage()
	done.showPage()
	todo.save()
	done.save()
