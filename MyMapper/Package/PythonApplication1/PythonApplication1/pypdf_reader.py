from PyPDF2 import PdfFileWriter, PdfFileReader
import io


pdf_name= "c:\\Me\\Python\\MySample01.pdf"

pdf= PdfFileReader( open(pdf_name, 'rb' ) )

pdf_page=pdf.getPage(0)
str=pdf_page.extractText()

print(str)


  

        
   

