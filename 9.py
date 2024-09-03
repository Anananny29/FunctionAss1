class IPL:
    country = "India"

    def __init__(self,PName,team):
        self.PName = PName
        self.team = team

    def info(self):
        print(self.country)
        print(self.PName)
        print(self.team)

p1 = IPL("Sachin","Mumbai Indians")
p1.info()
print("\n")
p2 = IPL("M.S.D","CSK")
p2.info()