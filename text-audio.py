import pyttsx3
import PyPDF2
import os
os.chdir("D:/Wavelabs/")
book = open('ML.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
num1= int(input('Enter a number: '))
for num in range(num1, pages):
    page = pdfReader.getPage(num1)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()