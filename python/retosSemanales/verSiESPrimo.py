def verSiEsPrimo(variable ):
    guardar =list()
    for i in variable:
        if (i <4):
            guardar.append(i)
        elif (i>3):
            cociente =0
            resto =0
            for j in range(4,cociente < j,1):  #buscar la forma de hacerlo recursiivo 
                cociente, resto = divmod(i, j)
                if (resto == 0) and (cociente > j):
                    break
                else:
                    guardar.append(i) 
    return guardar

def generarLista(n):
    a=[]
    for i in range(n+1):
        a.append(i)
    return a

if __name__=="__main__":
   ParaCalculo = generarLista(100)
   mostrar = verSiEsPrimo(ParaCalculo)
   print(ParaCalculo)
   print(mostrar)

    
   


              
