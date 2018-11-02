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
