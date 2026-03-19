from Cards import Cards
from random import randint
cards = Cards()
def choixcarte():
   carte=randint(0,cards.get_number_of_cards()-1)
   return carte
def choixdescription():
   carte=choixcarte()
   card= cards.get_card_by_id(carte)
   description=card.get_description()
   return description

def texteatroues():
    carte=choixcarte()
    b=str(cards.get_card_by_id(carte)).lower()
    print(b)
    description = choixdescription()
    description=str(description)
    tab=description.split(sep=" ")
    print(tab)
    t=[0 for _ in range(len(tab))]
    n=4
    check=[]
    for _ in range(n):
       a=randint(0,len(tab)-1)
       while str(t[a]).lower()==b or a in check:
           a=randint(0,len(tab)-1)
       check.append(a)
       t[a]=tab[a]
    return t
print(texteatroues())


       

      

        
    


 
 
   