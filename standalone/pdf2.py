# Python program to create
# a pdf file

from PyPDF2 import PdfFileWriter, PdfFileReader
from fpdf import FPDF
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas




doc = SimpleDocTemplate("a.pdf", pagesize=letter)
# container for the 'Flowable' objects
elements = []


styleSheet = getSampleStyleSheet()



P0 = Paragraph('''
<b>A pa<font color=red>r</font>a<i>graph</i></b>
<super><font color=yellow>1</font></super>''',
styleSheet["BodyText"])
P = Paragraph('''
<para align=center spaceb=3>The <b>ReportLab Left
<font color=red>Logo</font></b>
Image</para>''',
styleSheet["BodyText"])
data= [['A', 'B', 'C', P0, 'D','e'],
['00', '01', '02', [P], '04','e'],
['10', '11', '12', [P], '14','e'],
['20', '21', '22', '23', '24','e'],
['30', '31', '32', '33', '34','e']]
t=Table(data,style=[('GRID',(1,1),(-2,-2),1,colors.green),
('BOX',(0,0),(1,-1),2,colors.red),
('LINEABOVE',(1,2),(-2,2),1,colors.blue),
('LINEBEFORE',(2,1),(2,-2),1,colors.pink),
('BACKGROUND', (0, 0), (0, 1), colors.pink),
('BACKGROUND', (1, 1), (1, 2), colors.lavender),
('BACKGROUND', (2, 2), (2, 3), colors.orange),
('BOX',(0,0),(-1,-1),2,colors.black),
('GRID',(0,0),(-1,-1),0.5,colors.black),
('VALIGN',(3,0),(3,0),'BOTTOM'),
('BACKGROUND',(3,0),(3,0),colors.limegreen),
('BACKGROUND',(3,1),(3,1),colors.khaki),
('ALIGN',(3,1),(3,1),'CENTER'),
('BACKGROUND',(3,2),(3,2),colors.beige),
('ALIGN',(3,2),(3,2),'LEFT'),
])
t._argW[3]=1.5*inch


elements.append(t)


packet = "AG.pdf"
doc.build(elements)
can = canvas.Canvas(packet, pagesize=letter)
'''text = "Now is the time for all good men to..."
x = 1.8*inch
y = 2.7*inch
can.setFont("Helvetica", 10)
can.drawString(x,y,text)'''
img_file ="C:/Users/user/Downloads/images.png"
x_start =0
y_start =675
can.drawImage(img_file, x_start, y_start, width=120, preserveAspectRatio=True, mask='auto')

can.save()
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("a.pdf", "rb"))
b_pdf = PdfFileReader(open("b.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
third=b_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
third.mergePage(page)
output.addPage(third)
# finally, write "output" to a real file
outputStream = open("GFG.pdf", "wb")
output.write(outputStream)
outputStream.close()
