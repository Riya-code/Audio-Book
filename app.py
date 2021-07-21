import PyPDF2
import pyttsx3
  
# path of the PDF file
#"rb" mode opens the file in binary format for reading
path = open('file.pdf', 'rb')
  
# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(path)
  

# this will read the content of 3rd page.
from_page = pdfReader.getPage(2)
  
# extracting the text from the PDF
text = from_page.extractText()
  
# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
