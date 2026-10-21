#def my_range_while(start, stop, step=1):

    #vysledek = []
    #x = start
    #while (x > stop if step < 0 else x < stop)
        #vysledek.append(x)
        #x += step
    #return vysledek

#def my_enumerate_for(iterable, start=0):
    #vysledek = []
    
    #for value in iterable:
        #vysledek.append((start, value))
        #start += 1
    #return vysledek
    
    
    
    #for x in range(start, len(iterable)):
        #vysledek.append((x + start, iterable[x]))
    #return vysledek

#def my_enumerate_while(iterable, start=0):
    #vysledek = []
    #i = 0
    #while i < len(iterable):
        #vysledek.append((i + start, iterable[i]))
        #i += 1
    #return vysledek

def my_zip(*iterables):


    iterables = [
        ["Alice", "Bob", "Karel", "Eva", "Martin"],
        [ 30,       20,     24,     18,     27   ],
        [ 50,       80,     90,     55,     67   ]
    ]

    results = [
        ('Alice', 30, 50),
        ('Bob',   20, 80),
        ('Karel', 24, 90),
        ('Eva',   18, 55),
        ('Martin',27, 67),
    ]

    vysledek = []
    lenght = len(iterables[0])
    i = 0
    while i < lenght:
        value = []
        for iterable in iterables:
            value.append(iterable[i])
        vysledek.append(tuple(value))
        i += 1
    return vysledek


if __name__ == "__main__":


    jmena = ["Alice", "Bob", "Karel", "Eva", "Martin"]
    vek =   [ 30,       20,     24,     18,     27   ]
    vaha =  [ 50,       80,     90,     55,     67   ]

    vysledek = list(zip(jmena, vek, vaha))
    print(vysledek)

    #for jmeno, vek, vaha in vysledek:
        #print (f'{jmeno} je {vek} let a vazi {vaha} kg')

    # print(list(range(1, 10, 2)))
    # print(my_range_while(1, 10))

    #print(list(enumerate(["aaa", "bbb", "ccc"], 100)))
    #print(my_enumerate_for(["aaa", "bbb", "ccc"], 100))
    #print(my_enumerate_while(["aaa", "bbb", "ccc"], 100))
    