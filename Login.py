
"""
Login.py

1)	Creamos una lista de usuarios:
a.	Usuario (lista)
i.	Id
ii.	Nombre
iii.	Password
2)	Inicializamos la lista pidiendo datos al usuario: no validamos type, el usuario siempre me lo que se pide
3)	Pedimos que inserte usuario y contraseña
a.	Si existe usuario pero la contraseña no coincide
i.	Inserta la contraseña correcta (hasta que atine)
b.	Si no existe el usuario:
i.	“Usuario no encontrado. ¿Quiere registarse?”
	Sí: pedimos datos como en el primer punto
	No: “Hasta luego Mari Carmen!!”

"""

#Admin usuarios
usuarios=[[0,"Jose","pwjo"],[1,"Juan","PWju"]]
usuario=[]
insertarOtro=1
nombre=""
pss=""
iden=2

while(insertarOtro==1):
    print("Inserta tu nombre, por favor")
    nombre=input()
    print("Inserta tu contraseña, por favor")
    pss=input()
    usuario.insert(0,pss)
    usuario.insert(0,nombre)
    usuario.insert(0,iden)
    
    usuarios.append(usuario)
  
    iden=iden+1
    usuario=[]
    print("Quiere insertar otro usuario? (1-Si  2-No)")   
    insertarOtro=int(input())
    print(">>",usuarios)


#Mostrar lista de usuarios con for (es como tiene que ser ;) )
else:
    for usu in usuarios:
        print("Usu: ", usu[0], "Nom: ", usu[1], "PW: ", usu[2])
    
print("Hasta luego Mari Carmen!!")
        
