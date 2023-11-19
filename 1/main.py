def fonksiyon(sayi):

    return (sayi**3)-2*(sayi**2)-5

x1=2
x2=4
for i range(4):

 koktahmini=(x1+x2)/2

 if(fonksiyon(koktahmini)*fonksiyon(x1)<0):
    x2=koktahmini
else:
 x1=koktahmini


print(i+1,".iterasyon kok tahmını:"koktahmini)

