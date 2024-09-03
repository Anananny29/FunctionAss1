
def fun(x):
    result = []
    def digit():
        num_digits = len(str(abs(x)))  
        result.append(num_digits)
            
    def Even():
        count2=0
        for i in  (str(x)):
            if (int(i)%2==0):
                count2 += 1
        result.append(count2)
    def Odd():
        count3=0
        for i in  (str(x)):
            if (int(i)%2==1):
                count3 += 1
        result.append(count3)
    digit() 
    Even()
    Odd()
    return result
y = int(input("Enter a number : "))
ans = fun(y)
print(ans)
