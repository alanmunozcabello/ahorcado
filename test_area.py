
def nuevo_estado(p_adv,l_corr,est_actual):
    frase_nueva=""
    j=0
    while(j<len(est_actual)):
        i=0
        while(i<len(l_corr)and j<len(est_actual)):
            if(l_corr[i]==p_adv[j]):
                frase_nueva+=l_corr[i]
                j+=1
                i=0
            
            else:
                i+=1
        if(i==len(l_corr)):
            frase_nueva+=est_actual[j]
        j+=1
    print(frase_nueva)

p_adv="perro sentado"
l_corr="prr"
frase_actual=""

i=0
while(i<len(p_adv)):
    if(p_adv[i]==" "):
        frase_actual+="/" #para dibujar, si p_adv[i]=="/" -> dibujar -/- (linea cruzada con guion)
    else:
        frase_actual+="-"
    i+=1

nuevo_estado(p_adv,l_corr,frase_actual)