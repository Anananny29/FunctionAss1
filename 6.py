def parent():
    
    def myIndex(x):
       list = [1,2,3,4,5,6]
       ans =  list.index(x)
       print(ans)


    def myPalindrome(x):
        str_x = str(x)
        for i in range(len(str_x)):
            if str_x[i] == str_x[len(str_x)-1-i]:
                print("TRUE")
            return
            
    return myIndex, myPalindrome


myIndex , myPalindrome = parent()
choice = int(input("Enter your choice(1/2):"))
if  choice == 1 :
    num = int(input("Enter number : "))
    myIndex(num)

else :
    num = int(input("Enter number : "))
    myPalindrome(num)