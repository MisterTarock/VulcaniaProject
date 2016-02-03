##_______________  __.__        __                
##\__    ___/    |/ _|__| _____/  |_  ___________ 
##  |    |  |      < |  |/    \   __\/ __ \_  __ \
##  |    |  |    |  \|  |   |  \  | \  ___/|  | \/
##  |____|  |____|__ \__|___|  /__|  \___  >__|   
##                  \/       \/          \/       


import json
from tkinter import *
from tkinter import messagebox
from bottle import Bottle, route , run , template , post , request


cles = ['Nom', 'Prenom', 'Annee', 'Cal', 'Fonct', 'Ordre','Cont','Anniv','Age',\
        'Ecole','Etude','Met','Boite']
valeurs = ['Nom de baptême', 'Nom', 'Année de baptême', 'Année de Calotte',\
           'Fonction','Ordre','Contact', 'Anniversaire', 'Age', 'Ecole',\
           "Année d'étude", "Métier", "Boîte"]

class page():
    def __init__(self):
        try:
            document = open('BaseDeDonnees.txt','r')
            dico = json.load(document)
            document.close()
        except FileNotFoundError:                       
            print("l'emplacement est introuvable")
        except IOError:
            print("erreur d'ouverture")

        self.listing=Tk()
        self.listing.title("Listing")
        self.listing.grid_rowconfigure(0, weight=1)
        self.listing.grid_columnconfigure(0, weight=1)
        
        # The canvas
        cnv = Canvas(self.listing)
        cnv.grid(row=0, column=0, sticky='nswe')

        # The scrollbars
        hScroll = Scrollbar(self.listing, orient=HORIZONTAL, command=cnv.xview)
        hScroll.grid(row=1, column=0, sticky='we')
        vScroll = Scrollbar(self.listing, orient=VERTICAL, command=cnv.yview)
        vScroll.grid(row=0, column=1, sticky='ns')
        cnv.configure(xscrollcommand=hScroll.set, yscrollcommand=vScroll.set)

        # The Frame, in the Canvas, but without pack or grid
        frm = Frame(cnv)
        
        gens=[]
        for l in dico:
            gens += [l]
        # The labels and entry in the frame
        for i in range(len(gens)):
            Label(frm, text=gens[i]).grid(row=i, column=0)

        Label(frm, text="Recopier minutieusement la personne recherchée").grid(row=0, column=1)
        self.case = Entry(frm)
        self.case.grid(row=1, column=1)             #We can't group this line with the previous for the get() function afterwards
        self.btnc = Button(frm, text = 'ok',command=self.modif).grid(row=2, column=1)

        
        #To be sure that the dimensions are calculated
        frm.update()

        # To create the window in the canvas
        cnv.create_window(0, 0, window=frm, anchor=NW)

        # The scrollregion is the boxe with all the canvas
        cnv.configure(scrollregion=cnv.bbox(ALL))

    def modif(self):
        lapersonne=self.case.get()

        self.listing=Tk()
        self.listing.title("Modification")
        
        try:
            document = open('BaseDeDonnees.txt','r')
            dico = json.load(document)
            document.close()
        except FileNotFoundError:
            print("l'emplacement est introuvable")
        except IOError:
            print("erreur d'ouverture")
            
        baptise=dico[lapersonne]
        for i in range(len(cles)):
            Label(self.listing,text=valeurs[i]+' :').grid(row=i,column=0)
            if i ==0:
                Label(self.listing,text=lapersonne).grid(row=i,column=1)
            else :
                Label(self.listing,text=baptise[valeurs[i]]).grid(row=i,column=1)
            

        self.case0 = Entry(self.listing)
        self.case0.grid(row=0, column=2)
        self.case1 = Entry(self.listing)
        self.case1.grid(row=1, column=2)
        self.case2 = Entry(self.listing)
        self.case2.grid(row=2, column=2)
        self.case3 = Entry(self.listing)
        self.case3.grid(row=3, column=2)
        self.case4 = Entry(self.listing)
        self.case4.grid(row=4, column=2)
        self.case5 = Entry(self.listing)
        self.case5.grid(row=5, column=2)
        self.case6 = Entry(self.listing)
        self.case6.grid(row=6, column=2)
        self.case7 = Entry(self.listing)
        self.case7.grid(row=7, column=2)
        self.case8 = Entry(self.listing)
        self.case8.grid(row=8, column=2)
        self.case9 = Entry(self.listing)
        self.case9.grid(row=9, column=2)
        self.case10 = Entry(self.listing)
        self.case10.grid(row=10, column=2)
        self.case11 = Entry(self.listing)
        self.case11.grid(row=11, column=2)
        self.case12 = Entry(self.listing)
        self.case12.grid(row=12, column=2)
        
        self.bouton1=Button(self.listing,text='Confirmer',command=self.envoie).grid(row=14,column=2)
        self.bouton2=Button(self.listing,text='Quitter',command=self.listing.destroy).grid(row=14,column=0)
        


    def envoie(self):
        try:
            document = open('BaseDeDonnees.txt','r')
            dico = json.load(document)
            document.close()
        
            dico[self.case0.get()]={valeurs[1]:self.case1.get(),\
                                    valeurs[2]:self.case2.get(),\
                                    valeurs[3]:self.case3.get(),\
                                    valeurs[4]:self.case4.get(),\
                                    valeurs[5]:self.case5.get(),\
                                    valeurs[6]:self.case6.get(),\
                                    valeurs[7]:self.case7.get(),\
                                    valeurs[8]:self.case8.get(),\
                                    valeurs[9]:self.case9.get(),\
                                    valeurs[10]:self.case10.get(),\
                                    valeurs[11]:self.case11.get(),\
                                    valeurs[12]:self.case12.get()}

            document = open('BaseDeDonnees.txt','w')
            document.write(json.dumps(dico, sort_keys=True, indent=4, ensure_ascii=False))
            document.close()
        except FileNotFoundError:
            print("l'emplacement est introuvable")
        except IOError:
            print("erreur d'ouverture")

            
f=page()
f.listing.mainloop()

