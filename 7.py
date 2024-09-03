class sum ():
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    
    def mysum(self):
        return self.x + self.y
    
    def __add__(self,other):
        return sum(self.mysum(), other.mysum())


s1 = sum(3,5)
s2 = sum(4,5)

s1.mysum()
s2.mysum()

s3 = s1+s2

s3_sum = s3.mysum()
 
if(s3_sum % 2 == 0):
    print("Sum is even ",s3_sum)
else:
    print("Sum is odd ",s3_sum)