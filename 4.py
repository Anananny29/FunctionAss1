import array as arr

def countElement(a,x):
    num = a.count(x)
    return num



a = arr.array('i',[1,2,3,3,4,5,3])
ans = countElement(a,3)
print("3 found in list",ans,"times in list")