#1-Bmw,mercedes,opel,mazda elemanlarına sahip liste olusturun
arabalar = ["Bmw", "Mercedes", "opel", "mazda"]

#2-liste kac elemanlı
result = len(arabalar)
#3-listenın ilk ve son elemanı 
result = arabalar[0]
result = arabalar[3]
#4-mazda değerini toyota ile değiştirin
#  arabalar[3]='Toyota'
result = arabalar
#5-mecedes listenın bir elemanımıdır?
result ='Mercedes' in arabalar
#6-listenın -2 indexindeki değer?
result = arabalar[-2]

#7-listenın ilk 3 elemanı
result = arabalar[0:3]

#8-listenın son iki elemanı yerıne Toyota ve Renault değerini ekleyin
arabalar[-2:]= ['Toyota','Renault']
result = arabalar
#9-listenın üzerine Audi ve nissan değerlerini ekleyin
result = arabalar + ['Auid','Nissan']
#10-listenın son elemanını sılın
del arabalar[-1]
result = arabalar 
#11-liste elemanlarını tersten yazdırın
result = arabalar[::-1]

#12- aşağıdaki verileri bir liste içinde saklayın
   #studentA: Yiğit Bilgi 2010,(70,60,70)
   #studentB: Sena Turan 1999,(80,80,70)
   #studentC: Ahmet Turan 1998,(80,70,90)
studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC= ['Ahmet' ,'Turan', 1998,[(80,70,90)]]


#13-liste elemanlarını yazdırın
result = studentA,studentB,studentC

result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1]+ studentA[3][2])/3}"



print (result)