from tkinter import *
from PIL import ImageTk, Image
import requests
import xmltodict


#returnt een lijst met alle vertrektijden als strings
def vertrekTijd(code):
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + code
    response = requests.get(api_url, auth=inlogGegevens)
    vertrekXML = xmltodict.parse(response.text)
    vertrekList = []
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        str = vertrek['EindBestemming'] + ';'
        str += vertrek['VertrekTijd'][11:16] + ';'
        str += vertrek['TreinSoort'] + ';'
        #voor het geval er geen spoor bekend is
        try:
            str += vertrek['VertrekSpoor']['#text']
        except:
            str += 'onbekend'
        vertrekList.append(str)
    return vertrekList


#opent de reisinformatie van het huidige station
def reisInformatie(code):
    infoFrame = Frame(width=1280,
                      height=720,
                      bg="gold")
    listBox = Listbox(infoFrame,
                      height= 25,
                      width= 128,
                      font=('Consolas',14),
                      bg='gold')
    # for loop die de juiste tijden ophaalt via vertrekTijd() en ze daarna in de ListBox zet met de juiste opmaak via makeString()
    for tijd in vertrekTijd(code):
        listBox.insert(END, makeString(tijd))
    listBox.insert(END,'')
    listBox.place(x=0,y=25)
    infoLabel = Label(master= infoFrame,
                      text=makeString('Bestemming;Tijd;Type;Spoor'),
                      font=('Consolas',14,'bold'),
                      bg='gold',
                      width=50)
    infoLabel.place(x=10 ,y=0)
    # terug knop
    back = Button(master=infoFrame,
                  text='terug',
                  activebackground="black",
                  activeforeground="black",
                  font=('Helvetica', 14, 'bold'),
                  width=14,
                  height=2,
                  command= infoFrame.destroy)
    back.place(x=1000, y=610)
    infoFrame.place(x=0, y=0)

#reisinformatie Utrecht
def reisInfoUtrecht():
    reisInformatie('ut')

#Station naam invoeren
def reisInfoAnder():
    #bekijkt of het ingevoerde station juist is, en opent de juiste informatie
    def checkStation():
        found = ''
        for naam in stationDict:
            if naam == textInvoer.get():
                found = naam
                break
        if found == '':
            melding = Label(master=selectFrame,
                            text='Kies uw station en voer hem opnieuw in:',
                            bg="gold",
                            fg="black",
                            font=('Helvetica', 15),
                            width=30,
                            height=1)
            melding.place(x=50,y=110)
            listBox = Listbox(master=selectFrame,
                              height=10,
                              width=30,
                              selectborderwidth= 0,
                              fg= 'black',
                              font=('Helvetica', 15),
                              bg='gold')
            for naam in stationDict:
                if textInvoer.get() in naam:
                    listBox.insert(END,naam)
            listBox.place(x=500,y=110)
        else:
            reisInformatie(stationDict[found])
            selectFrame.destroy()

    #maakt het frame aan met de textinvoer en de buttons
    selectFrame = Frame(width=1280,
                        height=720,
                        bg="gold")

    info = Label(master=selectFrame,
                    text='*Let op! Gebruik hoofdletters bij uw station.',
                    bg="gold",
                    fg="black",
                    font=('Helvetica', 15),
                    width=30,
                    height=1)
    info.place(x=50, y=10)
    info = Label(master=selectFrame,
                 text='Voorbeeld: Amsterdam, Den Haag, Almere.',
                 bg="gold",
                 fg="black",
                 font=('Helvetica', 12),
                 width=30,
                 height=1)
    info.place(x=55, y=35)
    textInvoer = Entry(master=selectFrame,
                       font=('Helvetica', 34))
    textInvoer.place(x=50,y=60)
    goButton = Button(master=selectFrame, text='>',
                  activebackground="Blue",
                  activeforeground="White",
                  font=('Helvetica', 19, 'bold'),
                  width=7,
                  height=1,
                  command=checkStation)
    goButton.place(x=550,y=50)
    back = Button(master=selectFrame, text='terug',
                  activebackground="black",
                  activeforeground="black",
                  font=('Helvetica', 14, 'bold'),
                  width=14,
                  height=2,
                  command=selectFrame.destroy)
    back.place(x=1000, y=600)
    selectFrame.place(x=0,y=0)

#maakt de string geordend door er spaties tussen te zetten
def makeString(inputString):
    outputString = ''
    for word in inputString.split(';'):
        while len(word) < 27:
            word += ' '
        outputString += word
    return outputString


#inloggegevens om bij de NS api te kunnen
inlogGegevens = ('akram.tarioui@student.hu.nl', 'zmIyWhZ3ycFGkRYVAWPFV9KYQZYwnZbuBuYSEsfAkkMI6oAUAnjCfg')
response = requests.get('http://webservices.ns.nl/ns-api-stations-v2', auth=inlogGegevens)

#zet alle stationsnamen en de bijhoorende codes in een dictionary
stationDict = {}
for station in xmltodict.parse(response.text)['Stations']['Station']:
    stationDict[station['Namen']['Lang']] = station['Code']

#stel het TK window in met de goede afmetingen en de buttons en labels van het startscherm
root = Tk()
root.geometry("1280x720")
root.configure(background='Gold')

#haalt de afbeelding op
img1 = Image.open('achtergrond.jpg')
img = ImageTk.PhotoImage(img1)


plaatje = Label(master= root,
                image = img
                )
plaatje.pack(side = "bottom", fill = "both", expand = "yes")
plaatje.place(x= 0, y=0)

#button om de reisinformatie voor Utrecht te laten zien
button05 = Button(master= root,
                  text='Reisinformatie \nUtrecht',
                  activebackground= "black",
                  activeforeground= "black",
                  font=('Helvetica', 14, 'bold'),
                  width=14,
                  height=2,
                  command=reisInfoUtrecht)
button05.place(x=460,y=400)

#button die een window opent om een Station in te voeren
button06 = Button(master= root,
                  text='Reisinformatie \nander station',
                  activebackground= "black",
                  activeforeground= "black",
                  font=('Helvetica', 14, 'bold'),
                  width=14,
                  height=2,
                  command=reisInfoAnder)
button06.place(x=660,y=400)

#start de mainloop van TKinter
root.mainloop()