import random
from animacion import *
"defs"

# easter-egg: si sale la frase matar al ladron tendrá la opcion de lanzar una piedra al ladron y que caiga por el barranco ;) 
def selector_palabra(): #segun un numero random se elige la frase o palabra
    p1="mandarina"
    p2="macetero"
    p3="perro sentado"
    p4="escrituras falsas"
    p5="pompella"
    p6="matar al ladron"
    numero=random.randint(1,5) #comentar esto para probar easter-egg, yo se que quiere
    #numero=6 #descomentar esta variable para probar easter-egg

    egg=0
    if(numero==1):
        p_adv=p1
        egg=0
    elif(numero==2):
        p_adv=p2
        egg=0
    elif(numero==3):
        p_adv=p3
        egg=0
    elif(numero==4):
        p_adv=p4
        egg=0
    elif(numero==5):
        p_adv=p5
        egg=0
    elif(numero==6):
        p_adv=p6
        egg=1
    return p_adv,egg


def adivinador(p_adv,frase_actual,egg):
    print(p_adv) #borrar
    vida=6 #cantidad base de vidas
    malas=0
    buenas=0 #variable cantidad de letras buenas
    l_usadas="" #letras usadas
    l_corr=""#letras correctas usadas
    l_corr_nr=" " #letras correctas pero sin repetir (no repetidas: nr)
    l_incorr=""
    frase_nueva="" #variable de apoyo para mostrar frase con guiones
    mostrar_frase(p_adv,l_corr,frase_actual,frase_nueva)
    k=0
    while(k<len(p_adv)): #chequea por espacios, si se encuentran se da una buena por cada espacio
        if(p_adv[k]==" "): #sirbe para que se tomen por correctos todos los caracteres vacios/espacios
            buenas+=1
            k+=1
        else:
            k+=1
    
    mostrar_letras_correctas(l_corr_nr)
    mostrar_letras_incorrectas(l_incorr)
    while(malas<6 and buenas<len(p_adv)):#ciclo para ingresar letras hasta que pierda o gane
        #letra=str(input("ingrese una letra: ")) #ingresar letra
        letra=entradas()
        usada=0 #variable check si se usó la letra
        k=0
        while(k<len(l_usadas) and usada!=1): #revisar si la letra fue usada
            if(letra==l_usadas[k]):
                usada=1
                k+=1
            else:
                k+=1

        if(usada==0): #si usada == 0 significa que no se a utilizado
            l_usadas+=letra
            l_buena=0 #variable check si la letra ingresada es correcta o no
            i=0
            while(i<len(p_adv)): #chequea si la letra se encuentra en la palabra a adivinar
                if(letra==p_adv[i]): #si es que se encuentra en p_adv
                    l_corr+=letra
                    len_corr_nr=len(l_corr_nr)-2 #-2 para chequear antes del espacio
                    len_corr=len(l_corr)-1
                    if(l_corr[len_corr]!=l_corr_nr[len_corr_nr]): #si ultima letra en letras correctas usadas es distinta a la ultima letra correcta_nr, se agrega a l_corr_nr
                        l_corr_nr+=letra+" " #agrega un espacio para mejor legibilidad (GUI)
                     #sino no se agrega
                    l_buena+=1
                    buenas+=1
                    frase_nueva=mostrar_frase(p_adv,l_corr,frase_actual,frase_nueva)
                    print(letra) #cambiar po dibujar letras #borrar
                    i+=1

                else: #sino se pasa al siguiente index
                    i+=1
            if(l_buena==0):
                l_incorr+=letra+" "
                mostrar_letras_incorrectas(l_incorr)
                print(l_incorr) #cambiar por mostar letras incorrectas usadas #borrar
                vida-=1 
                vidas(vida)
                malas+=1
                animacion_fuego(malas)
                print("letra mala", malas) #cambiar por escribir en posicion letras usadas #borrar
            mostrar_letras_correctas(l_corr_nr)
        else:
            print("letra usada")

    if(malas==6):
        return 0,egg
    else:
        return 1,egg

def gana_o_pierde(g_o_p,egg):
    if(g_o_p==0):
        animacion_pierde()
        print("perdiste")#borrar
    else:
        if(g_o_p==1 and egg==1):
            lanzar_piedra()
            animacion_gana() #cambiar por matar al ladron d:
            print("ganaste")#borrar
        else:
            animacion_gana()
            print("ganaste")
# p_adv="perro sentado"
# l_corr="prr"

def guines(p_adv):
    frase_actual=""
    i=0 #setea guiones
    while(i<len(p_adv)):
        if(p_adv[i]==" "):
            frase_actual+="/" #para dibujar, si p_adv[i]=="/" -> dibujar -/- (linea cruzada con guion)
        else:
            frase_actual+="-"
        i+=1
    return frase_actual

    #nuevo_estado(p_adv,l_corr,frase_actual)

def main():
    intro_anim()
    p_adv,egg=selector_palabra() #variable p_adv es palabra a adivinar
    frase_actual=guines(p_adv)
    g_o_p,egg=adivinador(p_adv,frase_actual,egg)
    gana_o_pierde(g_o_p,egg)

"main"

main()