import random
print("---------------------------------------------------------------")
player=input("Ingrese su nombre: ")
print("---------------------------------------------------------------")
vida_jugador=100
vida_pc=100
print("---------------------------------------------------------------")
print("⚔️Bienvenido jugador: ",player)
while(vida_jugador>0 and vida_pc>0):
    eleccion=int(input("⚔️Para atacar, escriba 1, para defender, escriba 2⚔️: "))
    eleccion_pc=random.randint(1,2)
    if(eleccion==1 and eleccion_pc==2):
        print("💥¡Atacaste primero! pero se defendio la maquina🛡")
        print("---------------------------------------------------------------")
        vida_pc=vida_pc-10 
        print("Tu vida actual es: ",vida_jugador)
        print("Vida de la PC: ",vida_pc)
        print("---------------------------------------------------------------")
        
    elif(eleccion==2 and eleccion_pc==1):
        print("🛡Defendiste primero! pero ataco la maquina💥")
        vida_pc=vida_pc-10
        print("Tu vida actual es: ",vida_jugador)
        print("Vida de la PC: ",vida_pc)
        print("---------------------------------------------------------------")
        
    elif(eleccion==1 and eleccion_pc==1):
        print("💥Atacaste pero la computadora tambien ataco primero.💥 ")
        vida_jugador=vida_jugador-50
        vida_pc=vida_pc-50
        print("Tu vida actual es: ",vida_jugador)
        print("Vida de la PC: ",vida_pc)
       
    elif(eleccion==2 and eleccion_pc==2):
        print("🛡Te defendiste pero la maquina tambien!🛡 ")
        print("Tu vida actual es: ",vida_jugador)
        print("Vida de la PC: ",vida_pc)
        
    else:
        print("Esa opcion no existe, vuelva a intentarlo.")
        
if(vida_jugador>vida_pc):
    print("🎉Gano: ",player)
    print("Perdio la PC 💀")
    print("Vida actual del jugador: ",vida_jugador)
    print("Vida de la pc: ",vida_pc)
elif(vida_jugador<vida_pc):
    print("🎉Gano LA PC")
    print("Perdio 💀: ",player)
    print("Vida actual del jugador: ",vida_jugador)
    print("Vida de la PC: ",vida_pc)
else:
    print("--Empate--")
    print("Vida actual del jugador: ",vida_jugador)
    print("Vida de la pc: ",vida_pc)
    
