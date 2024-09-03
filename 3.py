import array as arr


def fact():
    a = arr.array('i',[1,2,3,4,5])
    result = arr.array('i', [])
    f = 1
    for i in a[::] :
        f = f*i
        result.append(f)
    return result

ans = fact()
print(ans)



