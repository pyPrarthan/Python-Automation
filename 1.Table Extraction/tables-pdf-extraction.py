#Extracting table from pdf

#(Fist you have to install a library 'camelot-py'! But before that, you need to pip install tk and ghostscript)

import camelot
tables = camelot.read_pdf('assets/foo.pdf', pages='1')
print(tables)

#(This is not working, will fix it soon!)