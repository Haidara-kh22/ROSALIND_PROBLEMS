dataset= input("enter the DNA dataset: ")
seq= open(dataset)
Content= seq.read()
a=0
t=0
c=0
g=0
print(Content)
for n in Content:
    if n=='A':
        a+=1
    if n=='T':
        t+=1
    if n=='G':
        g+=1
    if n=='C':
        c+=1
print(a," ",c," ",g," ",t)