import io

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter,PDFPageAggregator
#from pdfminer.pdfpage import PDFPage
import PyPDF2
from pdfminer.pdfparser import PDFParser, PDFDocument, PDFNoOutlines
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage





def with_pdf (pdf_doc, pdf_pwd, fn, *args):
    """Open the pdf document, and apply the function, returning the results"""
    result = None
    try:
        # open the pdf file
        fp = open(pdf_doc, 'rb')
        # create a parser object associated with the file object
        parser = PDFParser(fp)
        # create a PDFDocument object that stores the document structure
        doc = PDFDocument()
        # connect the parser and document objects
        parser.set_document(doc)
        doc.set_parser(parser)
        # supply the password for initialization
        doc.initialize(pdf_pwd)

        if doc.is_extractable:
            # apply the function and return the result
            result = fn(doc, *args)

        # close the pdf file
        fp.close()
    except IOError:
        # the file doesn't exist or similar problem
        pass
    return result

def _parse_toc (doc):
    """With an open PDFDocument object, get the table of contents (toc) data
    [this is a higher-order function to be passed to with_pdf()]"""
    toc = []
    try:
        outlines = doc.get_outlines()
        for (level,title,dest,a,se) in outlines:
            toc.append( (level, title) )
    except PDFNoOutlines:
        pass
    return toc


def get_toc (pdf_doc, pdf_pwd=''):
    """Return the table of contents (toc), if any, for this pdf file"""
    return with_pdf(pdf_doc, pdf_pwd, _parse_toc)



#doc=get_toc(file01)


#res=with_pdf(file01,"",)

#s=convert_pdf_to_txt(file01)
#s=convert_pdf_to_image(file01)

print(res)

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()
    
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
    #layout = retstr.get_result()
    
    fp.close()
    device.close()
    retstr.close()
    return text





def convert_pdf_to_image(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.BytesIO()
    laparams = LAParams()
    device = PDFPageAggregator( rsrcmgr,  laparams=laparams)
 #  fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    #password = ""
    #maxpages = 0
    #caching = True
    #pagenos = set()

    for page in PDFPage.get_pages(path):
        interpreter.process_page(page)
        
    #text = retstr.getvalue()
    layout=retstr.get_result()
    
    fp.close()
    device.close()
    retstr.close()
    return layout






