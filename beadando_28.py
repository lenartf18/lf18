#28
#Háromszög oldalai a<=b<=c
#Hány olyan háromszög van, amely kerülete nem haladja meg az 1000000 és teljesül, hogy a, b  és c számok relatív prímek, azaz a legnagyobb közös osztójuk 1.abs

def r_prime(a,b,c):
  i=2
  while i <= c:
    if (a<=b<=c):
      if ((a%i==0) and (b%i==0) and (c%i==0)):
        return False
      elif i < c:
        i += 1
      else:
        return True


#print (r_prime(4,9,7))

temp = 0
for a in range(1,20):
  for b in range (1,20):
    for c in range (1,20):
      if ((a<=b<=c) and (a+b)>c and (a+b+c)<1000): #Kiegészítettem azzal, hogy a két rövidebb oldal összegének nagyobbnak kell lennie, mint a leghosszabb oldal, hogy szerkeszthető legyen a háromszög: (a+b)>c
        if r_prime(a,b,c):
          temp += 1
          print (a, b, c)
print (temp)
