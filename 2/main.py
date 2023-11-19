def fonksiyon(sayi):

    return (sayi**3)+4*(sayi**2)-10

x1=1
x2=2
for i range(4):
 koktahmini=(x1+x2)/2

 if(fonksiyon(koktahmini)*fonksiyon(x1)<0):
    x2=koktahmini
else:
 x1=koktahmini


 print( i+1,f".iterasyon kok tahmını:"koktahmini)

