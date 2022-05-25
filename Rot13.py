# convert word ROT13
txt = input()

rot13 = str.maketrans('ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz', 'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')

txt2 = txt.translate(rot13)

word = 'raq' # replace 'end'
wordlist = txt2.split()
newtext = [x for x in wordlist if x not in word]
for x in newtext:
  print(x, end=" ")
print()
