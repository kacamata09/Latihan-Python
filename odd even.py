''' Algoritma
1. Jika n adalah ganjil maka print weird
2. iF n adalah genap dan dalam range 2 to 5 maka print Not weird
3. if n adalah genap dan dalam range 6 to 20 maka print weird
4. if n adalah genap dan n > 20 maka print Not weird'''

n = int(input(' : '))

if n % 2 == 0 and n in range(2,6):
    print('Not Weird')
elif n % 2 == 0 and n in range(7,21):
    print('Weird')
elif n % 2 == 0 and n > 20:
    print('Not Weird')
else:
    print('Weird')