import pickle


class listaItems:
    lista = []
    def __init__(self):
        listaDeItems=open("ficheroExterno", "ab+")
        listaDeItems.seek(0)
        self.lista=pickle.load(listaDeItems)
        try:
            print("se cargaron {} personas".format(len(self.lista)))
        except:
            print("el fichero esta vacio")
        finally:
            listaDeItems.close()
            del(listaDeItems)


    def agregarItems(self, p):
        self.agregarItems.append(p)
        self.guardarItemsEnFicheroExterno()
    
    def mostrarItems(self):
        for p in self.lista:
            print(p)
    
    def guardarItemsEnFicheroExterno(self):
        listaItems=open("ficheroExterno", "wb")
        pickle.dump(self.lista, listaItems)
        listaItems.close
        del(listaItems)
