def numero_feliz(numero, somas_realizadas=None):
    somas_realizadas = somas_realizadas or []
    if numero in somas_realizadas:  
        return False
    else:   
        somas_realizadas.append(numero)    
    quadrados_dos_digitos=[]
    a=numero

    while a>0:
        quadrados_dos_digitos.append((a%10)**2)
        a//=10
    soma=sum(quadrados_dos_digitos)

    if soma == 1:
        return True

    return numero_feliz(soma, somas_realizadas)

