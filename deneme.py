number =123
print(number)
print(type(number))

# a=int(input("dogum yili giriniz "))
# b=2024
# print("dogum yiliniz",b-a)

isTrue=True #how r u

isimListesi=['ali',2005,'istanbul',78.5,True]

print(type(isimListesi))

isimListesi.sort

print(isimListesi)

mesafe=int(input('mesafe degerini km cinsinden giriniz='))

km2Mile=0.621371
mile2Km=1.609

mil=mesafe*km2Mile

print(mil)

girdi=str(input('mesafe girin='))

x=girdi.rsplit()

mesafe1=int(x[0])
birim=x[1]

if(birim=='K' or birim=='k'):
    print('mesafe mil cinsinden', mesafe1*km2Mile)
elif(birim=='M' or birim=='m'):
    print('mesafe km cinsinden', mesafe1*mile2Km)
else:
    print('girdi hatali')

