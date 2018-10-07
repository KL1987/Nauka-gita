#rasa = 'kot'
#imie = 'Mialczek'
#waga = 5
#dlugosc = 30


#print ('moj ulubione zwierze to ' + rasa + " ma na imie " + imie + " wazy " + str(waga) + "kg" + " i mierzy " + str(dlugosc) + "cm " )


#samochody = ['syrena', 'poloneza']
#for s in samochody:
#    print(s)

#kwiaty = ['bratek', 'roza']
#ilosc = ['3', '5']

#for k in kwiaty:
#    print(k)

#for il in ilosc:
#    print(il)

#kwiaty = ['bratek', 'roza']
#ilosc = ['3', '5']

#for idx in range(len(kwiaty) ) :
#    print( "idx: " + str(idx) + "; " + kwiaty[idx])
#    print(kwiaty[idx] + " zamowiona ilosc " + str(ilosc[idx]))

#samochody = ['syrena', 'polonez']
#print(samochody[0])
#print(samochody[1])

#for s in samochody:
#    print(s)

#for idx in range(len(samochody)):
#    print(samochody[idx])

#samolot = {'name': 'boeing',
#            'przebieg':1000,
#            'type': 'pasazerski' }
#print(samolot['name'])

#for key, value in samolot.iteritems():
#    print(key)
#    print(value)


#samochod = {'name': 'hyundai',
#            'przebieg' :200000,
#            'model': 'i 30'}
#print(samochod['name'])

#for key, value in samochod.iteritems():
#    print(key)
#    print(value)

#for key, value in samochod.iteritems():
#    print("{0}:{1}".format(key, value))
#for key in samochod:
#    print("{0}:{1}".format(key, samochod[key]))

def print_dict(d):
    for key, value in d.iteritems():
        print("{0}:{1}".format(key, value))

if __name__== "__main__":
    samochod = {'name': 'hyundai',
            'przebieg' :200000,
            'model': 'i 30'}

    print_dict(samochod)
    print_dict(samochod)
