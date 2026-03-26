from Cards import Cards
from random import randint
from tkinter import*
cards = Cards()
def choixcarte():
   carte=randint(0,cards.get_number_of_cards()-1)
   return carte

def choixdescription(carte=choixcarte()):
   card= cards.get_card_by_id(carte)
   description=card.get_description()
   return description

def texteatroues():
    carte=choixcarte()
    b=str(cards.get_card_by_id(carte).get_name()).lower()
    description = choixdescription(carte)
    description=str(description)
    tab=description.split(sep=" ")
    t=[0 for _ in range(len(tab))]
    n=4
    check=[]
    for _ in range(n):
       a=randint(0,len(tab)-1)
       while str(t[a]).lower()==b or a in check:
           a=randint(0,len(tab)-1)
       check.append(a)
       t[a]=tab[a]
    for i in range (len(t)):
       if t[i]==0:
          t[i] = "_" * len(tab[i])
    t.append(carte)
    return t


def progression():
   t=texteatroues()
   id=t[-1]
   carte=str(cards.get_card_by_id(id).get_name()).lower()
   description=choixdescription(t[-1])
   description=str(description)
   t.pop(t.index(t[-1]))
   print(t)
   tab=description.split(sep=" ")
   print(tab)
   proposition=input("Quelle est la carte ? ")
   while proposition.lower()!=carte:
      mot=randint(0,len(t)-1)
      while tab[mot] is t[mot]:
         mot=randint(0,len(t)-1)
      t[mot]=tab[mot]
      print(t)
      proposition=input("Quelle est la carte ? ")
   print("Bravo la carte était",carte)
      
  
progression()


         
      



       

      

        
    


 
 
   