def duck_num(x):
    y=str(x)
    if "0" in y:
        return True
    else:
        return False

for i in range(1,656):
    if duck_num(i):
        print(i,end=' ')
