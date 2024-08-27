
import random

def losMonety():

    programChoice = {1:'Orzel', 2:'Reszka'}
    progchoiceNumber = random.randint(1,2)

    for key in programChoice:
            if progchoiceNumber in programChoice:
                return programChoice[progchoiceNumber]


####################################################################

print('Zagrajmy w orzeł czy reszka! Jesli chcesz koniec - wpisz koniec')

checGrania = True

punktyGracza = 0
punktyAi = 0

while checGrania:


    choice = input('Orzel czy reszka: ')
    choice = choice.capitalize()

    if choice == 'Koniec':
        checGrania = False
  
    if choice == 'Orzel' or choice == 'Reszka':
        
            doneChoiceAi = losMonety()
            

            print(f'Twój wybór to: {choice}!')
            print(f'Mój wybór to {doneChoiceAi}')

            
            wynik = losMonety()

            print(f'Rzucono monetę, a wynik to:... {wynik}')
            
            if wynik == doneChoiceAi and wynik == choice:
                print('Remis!')
            elif wynik != doneChoiceAi and wynik != choice:
                print('Nikt nie wygrał!')
            elif wynik == doneChoiceAi:
                punktyAi += 1
                print(f'Wygrałem tę rundę! Punkt dla mnie! Mam {punktyAi} punktów!')
            elif wynik == choice:
                punktyGracza += 1
                print(f'Wygrałeś tę rundę! Punkt dla Ciebie! Masz {punktyGracza} punktów!')
            
            else:
                print('REMIS')

            

    
        
            
       
            


        
       



