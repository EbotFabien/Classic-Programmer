import pandas as pd
from pandas.plotting import table
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from fpdf import FPDF
# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]
  
# Create the pandas DataFrame
df = pd.DataFrame(data, columns = ['Name', 'Age'])
  
# print dataframe.



pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 15)
  
# create a cell
pdf.cell(200, 10, txt = "Facture du mois de septembre", 
         ln = 1, align = 'C')
  
# add another cell
pdf.cell(200, 10, txt = "Veuillez voir vos facture de releve 5",
         ln = 2, align = 'C')

pdf.output('b.pdf', 'F')

ax = plt.subplot(121, frame_on=False)
ax.xaxis.set_visible(0)
ax.yaxis.set_visible(0)
table(ax, df, loc='upper center')
plt.savefig('GFG.pdf')


    
    
