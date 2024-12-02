path = r"C:\Users\Alejandro\Desktop\AoC\AoC_2024\input_02.txt"
with open(path, "r") as f:
    data = [list(map(int,l.split())) for l in f.readlines()]
print(data)

def isSafe(lista):
    '''
    By comparing first and last element, we decide whether 
    the whole list will be increasing or decreasing.
    Afterwards, check individual jumps
    '''
    first, last = lista[0], lista[-1]
    if first==last:
        return False
    elif first>last:
        lista = list(reversed(lista)) #we make it increasing 
    else:
        pass # we leave it increasing
    # List is now increasing, check all jumps
    for n in range(1, len(lista)): #we go looking back
        diff = lista[n]-lista[n-1]
        if diff>=1 and diff<=3:
            pass
        else: 
            return False
    return True

sol = 0
for l in data:
    print(l)
    if isSafe(l):
        sol+=1
print(f'Safe lists: {sol}')


# %%
