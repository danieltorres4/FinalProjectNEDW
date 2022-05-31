from turtle import clear
import speech_recognition as sr
import filecmp
from PyPDF2 import PdfFileMerger
from reportlab.pdfgen import canvas
def voiceToText(text):
    file = open("python/file.txt",'w', encoding = "utf-8")
    file.write(text)
    file.close()

def comparisonFiles():
    sample = "python/texto.txt"
    myFile = "python/file.txt"


    result = filecmp.cmp(sample,myFile)
    #print(result)

    if(result == True):
        print("Same info")
    else:
        print("Different info")

def voiceRecognition():
    
    r = sr.Recognizer()
   # with open("python/preguntas.txt","r") as archivo:
    #    for linea in archivo:
     #       print(linea)
    
    with sr.Microphone() as source: 
        print("\n\nSay something! :D")

        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='es-MX')
            print("You have said:")
            print("{}".format(text))
            voiceToText(text)
            comparisonFiles()
            c = canvas.Canvas("Test.pdf")
            c.drawImage("logo.jpg", 20,700,width=150, height=150)
            with open("python/file.txt","r") as archivo:
                for linea in archivo:
                    c.drawString(45, 650,"You have said: "+ linea)
                    c.setFont("Times-Roman", 45)
                    c.save()
           
            
        except:
            print("Sorry, cannot understand you :(")
        

#It determines the percetage 
def intersection():
    counter = 0
    sampleCounter = 0
    fileCounter = 0
    filelist=0
    percentage = 0
    sampleList = []
    fileList = []
    inter = []
    sample = open("python/texto.txt",'r')
    file = open("python/file.txt",'r')
    

    for line in sample:
        sampleList.extend(line.split())

    for lines in file:
        fileList.extend(lines.split())
    
    sampleCounter = len(sampleList)
    fileCounter = len(fileList)
    filelist= len(inter)
    print("It has " + str(sampleCounter) + " elements")
    print("It has " + str(fileCounter) + " elements")

    for words in fileList:
        for otherWords in sampleList:
            if words == otherWords:
                inter.append(words)
                counter = counter + 1
    
    print("\nWords in common: " + str(inter))
    print("#Words in common: " + str(counter))


    #Operation
    grade = (counter * 10) / sampleCounter
    #print("\nPercetage: " + str(round(percentage, 2)) + "%")
    c = canvas.Canvas("Test2.pdf")
    c.drawImage("logo.jpg", 20,700,width=150, height=150)
    c.drawString(45, 650,"Grade: " + str(round(grade, 2)))
    c.drawString(45, 450,"#Words in common: " + str(counter))
    c.save()
   

    sample.close()
    file.close()
def unir_documentos():
    pdfs = ["Test.pdf", "Test2.pdf"]
    nombre_archivo_salida = "TestResults.pdf"
    fusionador = PdfFileMerger()

    for pdf in pdfs:
        fusionador.append(open(pdf, 'rb'))

    with open(nombre_archivo_salida, 'wb') as salida:
        fusionador.write(salida)
    

#Main
voiceRecognition()
intersection()
unir_documentos()
