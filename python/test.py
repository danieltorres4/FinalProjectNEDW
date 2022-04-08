import speech_recognition as sr
import filecmp

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

    with sr.Microphone() as source:
        print("Say something! :D")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='es-MX')
            print("You have said: {}".format(text))
            voiceToText(text)
            comparisonFiles()
        except:
            print("Sorry, cannot understand you :(")

#It determines the percetage 
def intersection():
    counter = 0
    sampleCounter = 0
    fileCounter = 0
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
    percentage = (counter * 100) / sampleCounter
    print("\nPercetage: " + str(round(percentage, 2)) + "%")

    sample.close()
    file.close()

#Main
voiceRecognition()