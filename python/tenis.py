class Tenis():
    def __init__(self, puntaje) -> None:
        self._puntaje = puntaje
        

    
    def contar(self, puntaje):
        
        for i in puntaje:
            
            if (puntaje [i] =='P1'):
                if ((puntaje[i]=='P1' & puntaje[i+1]=='P1' & puntaje[i+2]=='P1' & puntaje[i+3]=='P1') == 4):
                    print('ha ganado el competidor 1')
            elif (puntaje [i] =='P2'):
                if ((puntaje[i] +puntaje[i+1] +puntaje[i+2] + puntaje[i+3]) == 4):
                    print('ha ganado el competidor 2')
            else:

            





if __name__=="__main__":
    lista = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']
    ver = Tenis(lista)

