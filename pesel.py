PESEL=input()
suma = 9*int(PESEL[0]) + 7*int(PESEL[1]) + 3*int(PESEL[2]) + 1*int(PESEL[3]) + 9*int(PESEL[4]) + 7*int(PESEL[5]) + 3*int(PESEL[6]) + 1*int(PESEL[7]) + 9*int(PESEL[8]) + 7*int(PESEL[9]);
if suma%10 == int(PESEL[len(PESEL)-1]):
  print("1")
else:
  print("0")
asdsadas