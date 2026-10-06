def add(a, b):
    c = a + b
    return c

def mul(a, b, c):
      vysledek = a * b * c
      return vysledek

def div(a, b):
     if b == 0:
          vypocet = 0
     else:
          vypocet = a / b
     return vypocet

def je_delitelne_beze_zbytku(a, b):
     x = a % b
     if x == 0:
          return "je delitelne beze zbytku"
     else:
          return "neni delitelne beze zbytku"

def je_delitelne_3(a):
     x = a % 3
     if x == 0:
          return "je delitelne 3"
     else:
          return "neni delitelne 3"

if __name__ == "__main__":
    # x = add(1, 2)    
    # x = mul(1, 2, 3)
    # x = div(10, 0)
    # vysledek = je_delitelne_beze_zbytku(10,3)
    vysledek = je_delitelne_3(9)
    print(vysledek)
