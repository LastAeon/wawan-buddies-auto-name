# program python untuk membuat file pdf wawancara
  
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

# variabel awal
your_nim = '16519275'
a = 'random'
b = '_16519.pdf'
i = 1

# setting variabel dari module fpdf
pdf = FPDF()
pdf.add_page() 
pdf.set_font("Arial", size = 15)

a = str(input())
while a != 'a':
    pdf.cell(200, 10, txt = a, ln = i, align = 'L')
    if nim(a)!='none':
        b = '_' + nim(a) + '.pdf'
    a = str(input())
pdf.output(your_nim + b)
