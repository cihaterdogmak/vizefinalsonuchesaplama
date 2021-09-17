''' VİZE VE FİNAL SINAVLARI YÜZDELİK HESAPLAMA'''
final = float(input('Final sonucunuzu giriniz = '))
if final < 55.0 :
     print('Final sonucunuz 55 puandan düşük olduğu için kaldınız.')
else:
     vize = float(input('Vize sonucunuzu giriniz = '))
     finaly = final * 60/100
     vizey = vize * 40/100
     sonuc = finaly + vizey
     if sonuc >= 55:
         print('Tebrikler dersi geçtiniz sonucunuz ') 
         print(sonuc)
     else:
     	print('Yüzdelik sonucunuz 55 puandan düşük olduğu için kaldınız sonucunuz =')
     	print(sonuc)