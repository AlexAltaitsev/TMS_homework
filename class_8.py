from re import M
from telnetlib import GA
from tkinter import N

    

class GameCharacter:
    def  __init__(self,name, gender, weight, height, race) -> None:
        self.name = name
        self.gender = gender
        self.weight = weight
        self.height = height
        self.race = race

    def greeting():
        for i in self.gender:
            if self.gender is 'Male':
                print(f'Добро пожаловать воин. Ты у нас {self.race}, это о многом говорит')
                break
            elif self.gender is 'Female':
                print(f'Приветсвую воительница. Рад что {self.race}, на нашей стороне')
                break
            else:
                print(f'Я не могу понять кто ты {self.race}')
                break
                

class TheСharacter(GameCharacter):
    def __init__(self, name, gender, weight, height, race) -> None:
        super().__init__(name, gender, weight, height, race)
    
    def greeting(self):
        print(f'Приветсвуюем вас {self.name}, в нашем мире')



if __name__ == '__main__':

    nord_character = GameCharacter(
        'Geralt',
        'Male',
        120,
        200,
        'Nord'
    )


    nord_character.greeting()
    
   
    

    player = GameCharacter()
    print(player.greeting())
    
    
    
