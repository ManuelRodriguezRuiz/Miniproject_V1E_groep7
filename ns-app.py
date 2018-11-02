#maakt de string geordend door er spaties tussen te zetten
def makeString(inputString):
    outputString = ''
    for word in inputString.split(';'):
        while len(word) < 27:
            word += ' '
        outputString += word
    return outputString

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
