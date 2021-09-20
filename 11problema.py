n=int(input('dati numarul de elemente a vectorului '))
z=[]
print('introduceti ',n,' elemente pentru vectorul creat')
for i in range(0,n):
    x=int(input('dati elementul: '))
    z.extend([x])
print(z)
print('b) afişează pe ecran numerele în ordinea inversă a introducerii în calculator')
for b in reversed(z):
    print(b, end = " ")
print('c) sortează componentele tabloului în ordine descrescătoare')
c=sorted(z)
c.sort(reverse=True)
print(c)
print('d) afişează pe ecran doar componentele pare')
d=[]
for d in z:
    if d%2==0:
        print(d, end = " ")
print('f) afişează pe ecran doar componentele impare')
f=[]
for f in z:
    if f%2!=0:
        print(f, end = " ")
print('n) creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură')
w=[]
n=list(filter(lambda x: (x%3==0), z))
print('w=',n)
print('e) afişează pe ecran media aritmetică a componentelor pare')
print(sum(d)/len(d))