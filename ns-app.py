
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

