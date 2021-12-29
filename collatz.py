#import sys

# x=0
while True:
    print('Podaj x: 1-100')
    x = int(input())
    first = x
    if x==0 or x>100:
        print('Liczba powinna być z zakresu 1-100. Wprowadz jeszcze raz!')
        continue

    a=0
    licznik=0
    while True:
        a +=1


# b=int(sys.argv[1])
# for ile in range(b):

        if x == 1:

# licznik=licznik-1

            licznik += 1
            print("Długość ciągu do osiągniecia jedynki to:", licznik, ", gdy rozpoczyna się liczbą:", first)
            break

        if x % 2 == False:
            x=(x/2)
            print(x)
            licznik += 1
        else:
            x=(3 * x+1)
            print(x)
            licznik +=1
            print('Aktualna długość ciągu to:', licznik+1, '(liczę dalej)...')
            continue
    print("End")
    break

# print('Koniec zadeklarowanego przebiegu sys.argv[1]')











