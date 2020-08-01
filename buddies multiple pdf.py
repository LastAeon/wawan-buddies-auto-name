# Python program to create 
# a pdf file 
  
# untuk yang memiliki masalah menggunakan module
import sys
sys.path.append('C:/Users/syihab/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.7_qbz5n2kfra8p0/LocalCache/local-packages/Python37/site-packages/')

from fpdf import FPDF 
import os

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
  
# inisialisasi variabel
nim_kamu = str(input("NIM Kamu"))
b = '_16519.pdf'
selesai = False

# petunjuk penggunaan
print('masukkan data setiap orang, dipisahkan dengan baris kosong setiap orangnya. masukkan "selesai" jika sudah selesai')

while not(selesai):
    # save FPDF() class into a variable pdf
    pdf = FPDF() 

    # Add a page 
    pdf.add_page() 
      
    # set style and size of font  
    pdf.set_font("Arial", size = 15)

    # Inisialisasi setiap file
    teks = str(input())
    i = 1
    b = '_'

    # input data file dan menentukan nama file
    while (teks != '' and teks != 'selesai'):
        pdf.cell(200, 10, txt = teks, ln = i, align = 'L')
        if nim(teks)!='none':
            b = b + nim(teks) + '.pdf'
        teks = str(input())

    # save file sebagai pdf 
    pdf.output(str(nim_kamu) + b, 'F')
    if teks == 'selesai':
        selesai = True

print('selesai')
