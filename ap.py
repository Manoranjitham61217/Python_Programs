n=int(input())
a=int(input())
d=int(input())
ap_sequence=[a+i*d for i in range(n)]
print(ap_sequence)
print(sum(ap_sequence))
