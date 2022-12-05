import pyttsx3
import PyPDF2
book = open('Curso Intensivo de Python.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)


for num in range(39, pages):
    speaker = pyttsx3.init()
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)  #teoricamente fala o livro todo
    speaker.save_to_file(text, "livrocompleto.mp3")
    speaker.runAndWait()
    print("acabou")  #looping infinito? porquê não grava o livro todo?

