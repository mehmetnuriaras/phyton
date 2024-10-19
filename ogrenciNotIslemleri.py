from fileio import getUserList,writeUserList

sinifinTamami={}
try:
    sinifinTamami=getUserList()
except:
    print('Gecmis veri seti okunamadi')

def ogrenciNotEkleme(ogrenciBilgileri):
    ogrenciNo, ogrenciNot, *rest=ogrenciBilgileri
    print(type(sinifinTamami.keys),' ',type(ogrenciNo),'\n',sinifinTamami)
    isStudentExist=ogrenciNo not in sinifinTamami.keys()
    print(isStudentExist)
    if isStudentExist: 
        sinifinTamami.update({ogrenciNo:[]})
        
    sinifinTamami.get(ogrenciNo).append(ogrenciNot)
    try:
        writeUserList(sinifinTamami)
    except:
        print("bir hata olustu")

    print(f'{ogrenciNo} numarali ogrencinin {len(sinifinTamami.get(ogrenciNo))}. notu eklenmistir.' 
          if not isStudentExist else 
          f'{ogrenciNo} numarali ogrencinin kaydi olusturulmus ve ilk sinav girisi yapilmistir.')
   
def ogrenciNotGuncelleme(guncellemeBilgileri):
    ogrenciNo, imtihanNo, yeniNot , *rest =guncellemeBilgileri
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
            
def yazdir():
    print(sinifinTamami)