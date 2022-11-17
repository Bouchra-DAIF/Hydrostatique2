def my_function () :
 print("Question 1 ")
 print("Selon la relation fondamentale de l'hydrostatique On a Pb-Pa= Mvhuil.g.(Za-Zb) ")
 Mvh=input("Entrez la masse volumique de l'huil : ")
 Za=input("Entrez Za : ")
 Zb=input("Entrez Zb : ")
 try:
     Mvh=float(Mvh) 
     Za=float(Za)
     Zb=float(Zb)
     h=Zb-Za
     Patm=10^5
     g=10
     Pb= Patm - (Mves*h*g)
     print("La pression en le point 3 est", Pb)
 except:
     print("Erreur") 

 print("Question 2")
 Ze=Za 
 print(Ze)

 print ("Question 3")
 print("Selon la relation fondamentale de l'hydrostatique On a Pc-Pb= Mveau.g.(Zb-Zc) ")
 Mve=input("Entrez la masse volumique de l'eau : ")
 H2=H2('entrez la hauteur entre B et C ')
  try:
     Mve=float(Mve) 
     H2=float(H2)
     Zb=float(Zb)
     g=10
     Mve= 1000
     Pc= Pb - (Mves*h*g)
     print("La pression en le point 3 est", PC)
 except:
     print("Erreur")

 print ("Question 4")
 Zd= (Pc-Patm)/Mve.g
 print("Zd est", Zd)
my_function