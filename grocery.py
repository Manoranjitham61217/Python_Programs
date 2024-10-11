milk = 30
biscut = 10
rice = 20
a = int(input("no of rice    :"))
b = int(input("no of milk    :"))
c = int(input("no of biscut  :"))

print('| ITEM    |  QUANTITY |  AMOUNT  |')
print("| rice    |    ",a,'  |   ',a*rice,"  |")
print("| milk    |    ",b,'  |   ',b*milk,"  |")
print("| biscut  |    ",c,'  |   ',c*biscut,"  |")
total = (a*rice)+(b*milk)+(c*biscut)
print("                        total = ",total)
