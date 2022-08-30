'''
bilangan primari
list bilangan primari : 
1. tampilkan list 1- dst
2. tapi dengan pembagi yang tifa


algoritma pemeriksa prima
1. Masukkan angka dari 2 sampai range n
2. jika dari 2 sampai n-1 ada yang habis dibagi menjadi 0
3. maka tampilkan bukan bilangan prima
4. jika 2 sampai n-1 tidak habis dibagi
5. maka tampilkan ini bilangan prima'''

n = int(input(''))

# print(bilpri)

# for i in range(1,n):
#     if i % 

# bilangan = [x for x in range(1,n+1)]

# print(bilangan)

# count = 0
# # bilpri = [x for x in range(2,n+1) n x % n-1 != 0 ]
# bilori = [x for x in bilangan if x % 2 == 0]
# print(bilori)

# hitung_dek = 2
# for i in range(2, n):
#     if i % hitung_dek != 0 and i == hitung_dek:
#         print('Ini bilangan prima')
#         break
#     elif i % (hitung_dek - 1) == 0:
#         print('Bukan bilangan prima')
#         break

for i in range(2,n):
    print(i)
    if (n) % i == 0:
        print('ini bukan bilangan prima')
        break
    elif (n) % i != 0 and i == (n-1):
        print('ini bilangan prima')
        
# fungsi insert bilangan prima

def is_prima(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def cari_bilangan_prima (awal, akhir):
  list_bilangan_prima = []

  for x in range(awal, akhir + 1):
    if is_prima(x):
      list_bilangan_prima.append(x)

  return list_bilangan_prima

listprima = cari_bilangan_prima(0, 100)

print(listprima)