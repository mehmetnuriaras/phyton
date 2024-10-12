

sinifinTamami={
   
}


# def all():

#     print('tum sinifin notlari su sekildedir')
#     for x in sinifinTamami.keys():
#         print(x, 'numarali ogrencinin notlari:')
#         print(sinifinTamami.get(x),'\n')

#     #print(sinifinTamami)
    
# def printOgrenci(printEdilecekOgrenci):
#     print(printEdilecekOgrenci, " numarali ogrencinin notlari asagidaki gibidir")
#     print(sinifinTamami.get(int(printEdilecekOgrenci)),'\n') # string olarak devam etmek icin tanimlarken string tanimla
    
def ogrenciNotEkleme(ogrenciBilgileri):
    # numara=ogrenciBilgileri.split()
    ogrenciNo=ogrenciBilgileri[0]
    ogrenciNot=ogrenciBilgileri[1]
    isStudentExist=ogrenciNo not in sinifinTamami.keys()
    if isStudentExist: # ogrenci no string kalabilirdi 
        sinifinTamami.update({ogrenciNo:[]})
    #     sinifinTamami.get(ogrenciNo).append(ogrenciNot)
    #     print(ogrenciNo, 'numarali ogrenci icin yeni kayit olusturulmus ve notu kaydedilmistir.')
    # else: 
    sinifinTamami.get(ogrenciNo).append(ogrenciNot)
    # print(ogrenciNo," numarali ogrencinin", len(sinifinTamami.get(ogrenciNo))+1 ,". notu eklenmistir.")
  # tek satir print icinde halledilir yazi
    print(f'{ogrenciNo} numarali ogrencinin {len(sinifinTamami.get(ogrenciNo))}. notu eklenmistir.' 
          if not isStudentExist else 
          f'{ogrenciNo} numarali ogrencinin kaydi olusturulmus ve ilk sinav girisi yapilmistir.')
   
def ogrenciNotGuncelleme(guncellemeBilgileri):
    ogrenciNo, imtihanNo, yeniNot , *rest =guncellemeBilgileri
    # splite gerek yok cunku liste kendisi assign edilebilinir. *rest kalani yeni liste olusur
    sinifinTamami.get(ogrenciNo)[imtihanNo-1]=yeniNot
    print(ogrenciNo, " numarali ogrencinin ", imtihanNo, " numarali sinav notu guncellenmistir.")
    
def ogrenciNotuYazdir(ogrenciNo):
    if  isinstance(ogrenciNo,int):
        print(ogrenciNo, " numarali ogrencinin notlari asagidaki gibidir")
        print(sinifinTamami.get(ogrenciNo),'\n') # string olarak devam etmek icin tanimlarken string tanimla
    else:
        print('tum sinifin notlari su sekildedir')
        for x in sinifinTamami.keys():
            print(x, 'numarali ogrencinin notlari:')
            print(sinifinTamami.get(x),'\n')
     
    
print('Tum ogrencilerin notlarini gormek icin all','\n',
      'Istediginiz ogrencinin notunu gormek icin print ogrencino,',
      '\n', 'not girmek icin ogrencino ve not yaziniz= ',
      '\n', 'not guncellemek icin update ogrencino kacinci imtihani guncellemek istediginizi ve yeninotu yaziniz',
      '\n', 'ornek1: 123 32, ornek2: update 123 1 42, ornek3: print 123, ornek4:all')
girdi=input()
while girdi!='q':
    bilgi=girdi.split()
   
    if bilgi[0] in ['all','print']:
        try:
            ogrenciNotuYazdir(int(bilgi[1]))
        except:
            ogrenciNotuYazdir('all')
        
    # elif  bilgi[0]=="print":
    #     printOgrenci(bilgi[1])
    
    elif  bilgi[0]=="update":
        try:
            # int(bilgi[1])
            # int(bilgi[2])
            # int(bilgi[3])
         
            
           ogrenciNotGuncelleme(list(map(lambda x: int(x), bilgi[1:])))
            
        except:
                print("yukarida verilen bilgiler dogrultusunda giris yapiniz lutfen.")
            
    else:
        try:
            # int(bilgi[0])
            # int(bilgi[1])
            ogrenciNotEkleme(list(map(lambda x: int(x), bilgi)))
        except:
                print("yukarida verilen bilgiler dogrultusunda giris yapiniz lutfen.")
                
                
    girdi=input('yukarida verilen bilgiler isiginda input giriniz= ')