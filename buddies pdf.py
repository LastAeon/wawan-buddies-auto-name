# Python program to create 
# a pdf file 
  
# untuk yang memiliki masalah menggunakan module
import sys
sys.path.append('C:/Users/syihab/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.7_qbz5n2kfra8p0/LocalCache/local-packages/Python37/site-packages/')

from fpdf import FPDF 

# fungsi mencari nim
def nim(a):
    b = a.find('1651')
    if b==-1:
        return 'none'
    else:
        c = ''
        for i in range(8):
            c += a[b+i]
        return c

# save FPDF() class into a  
# variable pdf 
pdf = FPDF() 
  

your_nim = '16519275'
a = 'random'
b = '_16519.pdf'

# Add a page 
pdf.add_page() 
  
# set style and size of font  
# that you want in the pdf 
pdf.set_font("Arial", size = 15)

a = str(input())
i = 1
while a != 'a':
    pdf.cell(200, 10, txt = a, ln = i, align = 'L')
    if nim(a)!='none':
        b = '_' + nim(a) + '.pdf'
    a = str(input())
# save the pdf with name .pdf 
pdf.output(your_nim + b)
print('selesai')
