def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 :
        if year % 400 == 0:
            leap = True
            return leap
        elif year % 100 == 0:
            leap = False
            return leap
        else:
            leap = True
            return leap
       
    return leap

year = int(input())
print(is_leap(year))

'''
if year == 4 itu kabisat
tapi yang bisa dibagi 100 itu bukan kabisat kecuali bisa dibagi 400'''