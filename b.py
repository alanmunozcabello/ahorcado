
def nuevo_estado(p_adv,l_corr,est_actual):
    est_nuevo=""
    j=0
    while(j<len(est_actual)):
        i=0
        while(i<len(l_corr)and j<len(est_actual)):
            if(l_corr[i]==p_adv[j]):
                est_nuevo+=l_corr[i]
                print(est_nuevo)
                j+=1
                i=0
                print(j)
            
            else:
                i+=1
            print(est_nuevo)
        if(i==len(l_corr)):
            est_nuevo+=est_actual[j]
        j+=1
    print(est_nuevo)

p_adv="perro sentado"
l_corr="rtdo"
est_actual=""

i=0
while(i<len(p_adv)):
    if(p_adv[i]==" "):
        est_actual+="/"
    else:
        est_actual+="-"
    i+=1

nuevo_estado(p_adv,l_corr,est_actual)