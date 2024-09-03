class Player:

    #class variable
    teamName = "India"

    #constructor
    def __init__(self,Name,JNo) :
        self.PName = Name   #instance variable
        self.Jno = JNo
    
    #instancemethod
    def Info(self):
        print(self.PName)
        print(Player.teamName)
        print(self.Jno)


p1 = Player("Virat",18)

p1.Info()