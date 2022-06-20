#Importing tkinter module
from tkinter import *
from tkinter import scrolledtext
from timeit import default_timer as timer
import random

#words/sentences for levels in test
level1_words=['Literally','ironic','Irregardless','whom','Colonel','nonplussed','Disintrested','enormity','Lieutenant','unbashed','Abstract','demanding','Baffling','ambiguous','chandelier']
level2_words=['Incomprehensibilties','troubleshooitng','Personification','transparentness','Acknowledgeable','trustworthiness','Interchangeable','notwithstanding','Foresightedness','interdependence','Semitranslucent','insurmountable','Disagreeable']
level3_words=['I see a big bird','It is a red bat','The gun is old','The ten is red','The tap is on','The man has a van','I ran for an hour','The van is green','The sky is blue','Henry is reading','I love my dog','London is the capital of England',]
level4_words=['How can i help you?',"George brushes her teeth twice a day",'A ship has arrived at the harbour','Please pin these papers','Sheeps are grazing in the feild','He is petty shopkeeper','This shoe is very tight','The table is costly','This mango is over ripe']
level5_words=["I'll get chicken from the oven and some soup with it","Tomorrow early morning first i go to morning walk",'They go to a gallery every Saturday','Her shoes were brand new, and now they are missing',"I and my sister don't see each other anymore",
              'I met a homeless person in Newyork','There are so few people in the class, so one can talk to each other','My mother is taller than my brother','There are some green apples on the plate']

#creating Tk window
root = Tk()
root.geometry('900x550')                                           #size of the widget(widthxheight)
root.title('Typing Speed Test')                                    #title of widget
root.resizable(0,0)
c = Frame(root,width=900,height=550,bg="#000000").place(x=0,y=0)   #frame for background colour

def main():
    def next_():                                      #next function to start the game after entering name
        user = u_name.get()
        file=open('TypingSpeedTest.txt','a')          #opening file in which data will be stored
        file.write('\n')                              #writing data to file
        file.write(user)
        file.close                                    #closing file
        c = Frame(root,width=900,height=550,bg="#000000").place(x=0,y=0)
        tst = Label(root, text = "TYPING SPEED TEST",font='Gabriola  40',fg="white",bg="#000000").grid(row=3,column=3, padx = 280,pady = 150)
        level1 = Label(root,text="Level 1",font='Gabriola 25',fg="white",bg="#000000").place(x=420,y=230)
        Start = Button(root,text="Start", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = game_level1).place(x = 400, y = 300)

    c = Frame(root,width=900,height=550,bg="#000000").place(x=0,y=0)
    tst = Label(root, text = "TYPING SPEED TEST",font=('Gabriola 40'),fg="white",bg="#000000").grid(row=3,column=3, padx = 280,pady = 150)          #header
    name = Label(root,text="Name:",font='Gabriola 18',fg="white",bg="#000000").place(x=300,y=269)
    u_name = Entry(root, font='Gabriola 15', width = 27,bd = 0)
    u_name.place(x=371,y=275)
    u_name.focus()
    Open = Button(root,text='View saved data', fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = files).place(x = 300, y = 325)
    Next = Button(root,text='Next', fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = next_).place(x = 530, y = 325)



#functions for level header and start button  
def level2():
    c = Frame(root,width=900,height=550,bg="#000000").place(x=0,y=0)
    tst = Label(root, text = "TYPING SPEED TEST",font='Gabriola  40',fg="white",bg="#000000").grid(row=3,column=3, padx = 280,pady = 150)
    level2 = Label(root,text="Level 2",font='Gabriola 25',fg="white",bg="#000000").place(x=420,y=230)
    Start = Button(root,text="Start", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = game_level2).place(x = 400, y = 300)
    
def level3():
    c = Frame(root,width=900,height=550,bg="#000000").place(x=0,y=0)
    tst = Label(root, text = "TYPING SPEED TEST",font='Gabriola  40',fg="white",bg="#000000").grid(row=3,column=3, padx = 280,pady = 150)
    level3 = Label(root,text="Level 3",font='Gabriola 25',fg="white",bg="#000000").place(x=420,y=230)
    Start = Button(root,text="Start", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = game_level3).place(x = 400, y = 300)

def level4():
    c = Frame(root,width=900,height=550,bg="#000000").place(x=0,y=0)
    tst = Label(root, text = "TYPING SPEED TEST",font='Gabriola  40',fg="white",bg="#000000").grid(row=3,column=3, padx = 280,pady = 150)
    level4 = Label(root,text="Level 4",font='Gabriola 25',fg="white",bg="#000000").place(x=420,y=230)
    Start = Button(root,text="Start", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = game_level4).place(x = 400, y = 300)

def level5():
    c = Frame(root,width=900,height=550,bg="#000000").place(x=0,y=0)
    tst = Label(root, text = "TYPING SPEED TEST",font='Gabriola  40',fg="white",bg="#000000").grid(row=3,column=3, padx = 280,pady = 150)
    level5 = Label(root,text="Level 5",font='Gabriola 25',fg="white",bg="#000000").place(x=420,y=230)
    Start = Button(root,text="Start", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = game_level5).place(x = 400, y = 300)



#level 1 function
def game_level1():
    def result(event):                         #nested function to show result of input word
        def quitt():                           #functions for quit button and destroy the main window
            file=open('TypingSpeedTest.txt','a')
            file.write('\n')
            file.write('Level: 1 Time: ')
            file.write(time)
            file.close()
            root.destroy()

        end=timer()                       #to stop timer
        time=format(end-start,',.2f')     #to calculate total time taken by user to type anything
        c = Frame(root,width=900,height=550,bg="#000000").place(x=0,y=0)
        tst = Label(root, text = "TYPING SPEED TEST",font='Gabriola  40',fg="white",bg="#000000").grid(row=3,column=3, padx = 280,pady = 150)
        if (entry.get() == level1_words[word]):                                                                         #to check if the typed statement matches the given statement
            time1 = Label(root,text="You took ",font='Gabriola 25',fg="white",bg="#000000").place(x=320,y=230)
            time2 = Label(root,text=time,font='Gabriola 23',fg="white",bg="#000000").place(x=430,y=228)
            sec = Label(root,text="seconds",font='Gabriola 25',fg="white",bg="#000000").place(x=490,y=230)
            another_word=Button(root,text="Another word", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = game_level1).place(x = 300, y = 300)   #button for another word in the same level
            Quit = Button(root,text="Quit", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = quitt).place(x = 480, y = 300)                     #button to quit 
            next_level = Button(root,text="Next level", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = level2).place(x = 400, y = 370)          #button for going to next level
            
        else:
            time1 = Label(root,text="Wrong spelling",font='Gabriola 25',fg="white",bg="#000000").place(x=360,y=225)
            try_again = Button(root,text="Try Again", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = game_level1).place(x = 300, y = 300)
            Quit = Button(root,text="Quit", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = quitt).place(x = 480, y = 300)
            
            
    word=random.randint(0,len(level1_words)-1)                   #for choosing a random word from levels list
    start= timer()                                               #time start
    c = Frame(root,width=900,height=550,bg="#000000").place(x=0,y=0)
    tst = Label(root, text = "TYPING SPEED TEST",font='Gabriola  40',fg="white",bg="#000000").grid(row=3,column=3, padx = 280,pady = 150)
    type1 = Label(root,text="Type: ",font='Gabriola 25',fg="white",bg="#000000").place(x=370,y=230)
    word1 = Label(root,text=level1_words[word],font='Gabriola 25',fg="white",bg="#000000").place(x=430,y=230)
    entry = Entry(root, font='Gabriola 15', width = 27,bd = 0)                                                #entry widget to enter the given word/sentence
    entry.bind("<Return>",result)
    entry.place(x=345,y=300)                                                                                  
    entry.focus()                                                                                             #for focus in the entry widget
    Submit = Button(root,text="Submit", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = result).place(x = 400, y = 350)     #submit button to check results



#level 2 function
def game_level2():
    def result(event):
        def quitt():
            file=open('TypingSpeedTest.txt','a')
            file.write('\n')
            file.write('Level: 2 Time: ')
            file.write(time)
            file.close()
            root.destroy()

        end=timer()
        time=format(end-start,',.2f')
        c = Frame(root,width=900,height=550,bg="#000000").place(x=0,y=0)
        tst = Label(root, text = "TYPING SPEED TEST",font='Gabriola  40',fg="white",bg="#000000").grid(row=3,column=3, padx = 280,pady = 150)
        if (entry.get() == level2_words[word]):
            time1 = Label(root,text="You took ",font='Gabriola 25',fg="white",bg="#000000").place(x=320,y=230)
            time2 = Label(root,text=time,font='Gabriola 23',fg="white",bg="#000000").place(x=430,y=228)
            sec = Label(root,text="seconds",font='Gabriola 25',fg="white",bg="#000000").place(x=490,y=230)
            another_word=Button(root,text="Another word", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = game_level2).place(x = 300, y = 300)
            Quit = Button(root,text="Quit", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = quitt).place(x = 480, y = 300)
            next_level = Button(root,text="Next level", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = level3).place(x = 400, y = 370)
            
        else:
            time1 = Label(root,text="Wrong spelling",font='Gabriola 25',fg="white",bg="#000000").place(x=360,y=225)
            try_again = Button(root,text="Try Again", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = game_level2).place(x = 300, y = 300)
            Quit = Button(root,text="Quit", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = quitt).place(x = 480, y = 300)
            
            
    word=random.randint(0,len(level2_words)-1)
    start= timer()
    c = Frame(root,width=900,height=550,bg="#000000").place(x=0,y=0)
    tst = Label(root, text = "TYPING SPEED TEST",font='Gabriola  40',fg="white",bg="#000000").grid(row=3,column=3, padx = 280,pady = 150)
    type1 = Label(root,text="Type: ",font='Gabriola 25',fg="white",bg="#000000").place(x=370,y=230)
    word1 = Label(root,text=level2_words[word],font='Gabriola 25',fg="white",bg="#000000").place(x=430,y=230)
    entry = Entry(root, font='Gabriola 15', width = 27,bd = 0)
    entry.bind("<Return>",result)
    entry.place(x=345,y=300)
    entry.focus()
    Submit = Button(root,text="Submit", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = result).place(x = 400, y = 350)



#level 3 function
def game_level3():
    def result(event):
        def quitt():
            file=open('TypingSpeedTest.txt','a')
            file.write('\n')
            file.write('Level: 3 Time: ')
            file.write(time)
            file.close()
            root.destroy()

        end=timer()
        time=format(end-start,',.2f')
        c = Frame(root,width=900,height=550,bg="#000000").place(x=0,y=0)
        tst = Label(root, text = "TYPING SPEED TEST",font='Gabriola  40',fg="white",bg="#000000").grid(row=3,column=3, padx = 280,pady = 150)
        if (entry.get() == level3_words[word]):
            time1 = Label(root,text="You took ",font='Gabriola 25',fg="white",bg="#000000").place(x=320,y=230)
            time2 = Label(root,text=time,font='Gabriola 23',fg="white",bg="#000000").place(x=430,y=228)
            sec = Label(root,text="seconds",font='Gabriola 25',fg="white",bg="#000000").place(x=490,y=230)
            another_word=Button(root,text="Another word", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = game_level3).place(x = 300, y = 300)
            Quit = Button(root,text="Quit", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = quitt).place(x = 480, y = 300)
            next_level = Button(root,text="Next level", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = level4).place(x = 400, y = 370)
            
        else:
            time1 = Label(root,text="Wrong spelling",font='Gabriola 25',fg="white",bg="#000000").place(x=360,y=225)
            try_again = Button(root,text="Try Again", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = game_level3).place(x = 300, y = 300)
            Quit = Button(root,text="Quit", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = quitt).place(x = 480, y = 300)
            
            
    word=random.randint(0,len(level3_words)-1)
    start= timer()
    c = Frame(root,width=900,height=550,bg="#000000").place(x=0,y=0)
    tst = Label(root, text = "TYPING SPEED TEST",font='Gabriola  40',fg="white",bg="#000000").grid(row=3,column=3, padx = 280,pady = 150)
    type1 = Label(root,text="Type: ",font='Gabriola 25',fg="white",bg="#000000").place(x=320,y=230)
    word1 = Label(root,text=level3_words[word],font='Gabriola 25',fg="white",bg="#000000").place(x=380,y=230)
    entry = Entry(root, font='Gabriola 15', width = 27,bd = 0)
    entry.bind("<Return>",result)
    entry.place(x=345,y=300)
    entry.focus()
    Submit = Button(root,text="Submit", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = result).place(x = 400, y = 350)



#level 4 function
def game_level4():
    def result(event):
        def quitt():
            file=open('TypingSpeedTest.txt','a')
            file.write('\n')
            file.write('Level: 4 Time: ')
            file.write(time)
            file.close()
            root.destroy()

        end=timer()
        time=format(end-start,',.2f')
        c = Frame(root,width=900,height=550,bg="#000000").place(x=0,y=0)
        tst = Label(root, text = "TYPING SPEED TEST",font='Gabriola  40',fg="white",bg="#000000").grid(row=3,column=3, padx = 280,pady = 150)
        if (entry.get() == level4_words[word]):
            time1 = Label(root,text="You took ",font='Gabriola 25',fg="white",bg="#000000").place(x=320,y=230)
            time2 = Label(root,text=time,font='Gabriola 23',fg="white",bg="#000000").place(x=430,y=228)
            sec = Label(root,text="seconds",font='Gabriola 25',fg="white",bg="#000000").place(x=490,y=230)
            another_word=Button(root,text="Another word", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = game_level4).place(x = 300, y = 300)
            Quit = Button(root,text="Quit", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = quitt).place(x = 480, y = 300)
            next_level = Button(root,text="Next level", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = level5).place(x = 400, y = 370)
            
        else:
            time1 = Label(root,text="Wrong spelling",font='Gabriola 25',fg="white",bg="#000000").place(x=360,y=225)
            try_again = Button(root,text="Try Again", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = game_level4).place(x = 300, y = 300)
            Quit = Button(root,text="Quit", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = quitt).place(x = 480, y = 300)
            
            
    word=random.randint(0,len(level4_words)-1)
    start= timer()
    c = Frame(root,width=900,height=550,bg="#000000").place(x=0,y=0)
    tst = Label(root, text = "TYPING SPEED TEST",font='Gabriola  40',fg="white",bg="#000000").grid(row=3,column=3, padx = 280,pady = 150)
    type1 = Label(root,text="Type: ",font='Gabriola 25',fg="white",bg="#000000").place(x=300,y=230)
    word1 = Label(root,text=level4_words[word],font='Gabriola 25',fg="white",bg="#000000").place(x=360,y=230)
    entry = Entry(root, font='Gabriola 15', width = 27,bd = 0)
    entry.bind("<Return>",result)
    entry.place(x=345,y=300)
    entry.focus()
    Submit = Button(root,text="Submit", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = result).place(x = 400, y = 350)



#level 5 function
def game_level5():
    def result(event):
        def quitt():
            file=open('TypingSpeedTest.txt','a')
            file.write('\n')
            file.write('Level: 5 Time: ')
            file.write(time)
            file.close()
            root.destroy()

        def finish():                              #finish function for when game has reached maximum levels
            file=open('TypingSpeedTest.txt','a')
            file.write('\n')
            file.write('Level: 5 Time: ')
            file.write(time)
            file.write('  Finished')
            file.close()
            root.destroy()


        end=timer()
        time=format(end-start,',.2f')
        c = Frame(root,width=900,height=550,bg="#000000").place(x=0,y=0)
        tst = Label(root, text = "TYPING SPEED TEST",font='Gabriola  40',fg="white",bg="#000000").grid(row=3,column=3, padx = 280,pady = 150)
        if (entry.get() == level5_words[word]):
            time1 = Label(root,text="You took ",font='Gabriola 25',fg="white",bg="#000000").place(x=320,y=230)
            time2 = Label(root,text=time,font='Gabriola 23',fg="white",bg="#000000").place(x=430,y=228)
            sec = Label(root,text="seconds",font='Gabriola 25',fg="white",bg="#000000").place(x=490,y=230)
            another_word=Button(root,text="Another word", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = game_level5).place(x = 300, y = 300)
            Finish = Button(root,text="Finish", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = finish).place(x = 480, y = 300)
            
        else:
            time1 = Label(root,text="Wrong spelling",font='Gabriola 25',fg="white",bg="#000000").place(x=360,y=225)
            try_again = Button(root,text="Try Again", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = game_level5).place(x = 300, y = 300)
            Quit = Button(root,text="Quit", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = quitt).place(x = 480, y = 300)
            
            
    word=random.randint(0,len(level5_words)-1)
    start= timer()
    c = Frame(root,width=900,height=550,bg="#000000").place(x=0,y=0)
    tst = Label(root, text = "TYPING SPEED TEST",font='Gabriola  40',fg="white",bg="#000000").grid(row=3,column=3, padx = 280,pady = 150)
    type1 = Label(root,text="Type: ",font='Gabriola 25',fg="white",bg="#000000").place(x=400,y=220)
    word1 = Label(root,text=level5_words[word],font='Gabriola 25',fg="white",bg="#000000").place(x=240,y=270)
    entry = Entry(root, font='Gabriola 15', width = 27,bd = 0)
    entry.bind("<Return>",result)
    entry.place(x=345,y=350)
    entry.focus()
    Submit = Button(root,text="Submit", fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = result).place(x = 400, y = 400)


def files():
    c = Frame(root,width=900,height=550,bg="#000000").place(x=0,y=0)
    tst = Label(root, text = "TYPING SPEED TEST",font='Gabriola  40',fg="white",bg="#000000").grid(row=3,column=3, padx = 280,pady = 150)
    file = open('TypingSpeedTest.txt','r')
    line = file.read()
    text = scrolledtext.ScrolledText(root, width = 40,height = 7, font='Gabriola  15' )
    text.place(x = 280, y = 269)
    text.insert(INSERT, line)                                                               #to set scrolled text content
    file.close
    Back = Button(root,text='Back', fg = '#000000',width = 15, height = 2, bg ='white', cursor = 'hand2',command = main).place(x = 630, y = 490)
    


main()
root.mainloop()
