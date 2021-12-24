names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000,1998,1987]

#1- "Cenk" ismini listenın sonuna ekleyın
# names.append("Cenk")

#2-"Sena"değerini listenin basına ekleyın
# names.insert(0, "Sena")

#3- "Deniz" ismini listeden silin
#names.remove("Deniz")
#4-"Deniz" isminin indeksi nedir?
# index = names.index("Deniz")
# print(index)
#5- "Ali" listenın elemanı mı?
# results = 'Ali' in names
# print(results)
#6- Liste elemanlarını ters çevirin
   #names.reverse()
#7-Liste elemanlarını alfabetık sıraya göre sıralayın
   #names.sort()
#8- years lıstesıı rakamsal büyüklüğe göre sıralayın
  #years.sort()
   #print(years)
#9- str= "Chevrolet,Dacia" karakter dızısını listeye çevirin

# str= "Chevrolet,Dacia"
# result = str.split(',')
# print(result)
#10- years dizisinin en büyük ve en küçük elemanı nedir?

# min = min(years)
# max = max(years)
# print(min,max)
#11-years dizisinde kaç tane 1998 değeri vardır?
# result = years.count(1998)
# print(result)

#12- years dizisinin tüm elemanlarını silin.

# years.clear()
# print(years)
#13- kullanıcıdan alacagınız 3 tane marka bilgiini bir listede saklayın

markalar = []
marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)
print(markalar)

 #print(names)
