def palindrom(szam):
  szam = str(szam)
  rev_szam = szam[::-1]
  rev_szam = int(rev_szam)
  szam = int(szam)
  if szam == rev_szam:
    return True
  else:
    return False

szam = int(input("Kérek egy számot: "))
while True:
  if szam > 100000:
    szam = int(input("A szam 100000 alatt legyen: "))
  else:
    for i in range(1, szam+1):
      if palindrom(i):
        print (i)
    break
