from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.converter import  PDFPageAggregator
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams,LTTextBoxHorizontal,LTImage,LTFigure,LTRect,LTTextBox,LTLine
import io



pdf_name= "c:\\Me\\Python\\MySample01.pdf"
pdf_file =open(pdf_name,'rb')
#pdf_parser=PDFParser(pdf_file)
#pdf =  PDFDocument(pdf_parser,"")
pdf_resource=PDFResourceManager()
pdf_params=LAParams()
pdf_device=PDFPageAggregator(pdf_resource,laparams=pdf_params)
pdf_interpreter=PDFPageInterpreter(pdf_resource,pdf_device)


no_of_images=0
no_of_figures=0
no_of_rect=0
no_of_text=0
no_of_othertext=0
no_of_line=0
str=""


for pdf_page in PDFPage.get_pages(pdf_file):
    pdf_interpreter.process_page(pdf_page)
    pdf_layout=pdf_device.get_result()
    for element in pdf_layout:
        
          if isinstance(element,LTFigure):
            no_of_figures=no_of_figures+1
          elif isinstance(element,LTImage):
              no_of_images=no_of_images+1
          elif isinstance(element,LTRect):
              no_of_rect=no_of_rect+1
          elif isinstance(element,LTLine):
              no_of_line=no_of_line+1
          elif isinstance(element,LTTextBox):
              no_of_text=no_of_text+1
              str=str+element.get_text() 
              str=str+"|"
          else:
             no_of_othertext=+1

print ('No of Figures',no_of_figures)
print ('No of Images', no_of_images)
print('No of Rectangle', no_of_rect)
print('No of TextBox', no_of_text)
print('No of OtherText', no_of_othertext)
print('No of Line', no_of_line)
print('Extracted Text',str)

