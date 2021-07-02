class Frutas:
    def __init__(self, nomFruta, cantKilos):
        self.nomFruta=nomFruta
        self.cantKilos=cantKilos

    def precioXkg(self):
        if self.nomFruta == "manzana": precioKG = 2
        if self.nomFruta == "platano": precioKG = 1.5
        if self.nomFruta == "pera": precioKG = 5
        if self.nomFruta == "durazno": precioKG = 4.5
        if self.nomFruta == "papaya": precioKG = 4.3
        if self.nomFruta == "melon": precioKG = 6.2
        if self.nomFruta == "uva": precioKG = 3.8
        if self.nomFruta == "kiwi": precioKG = 9.5

        return precioKG

    def totalPrecio(self):
        totalPrecio=self.cantKilos*self.precioXkg()
        return totalPrecio




def ingresoInformacion(listaFrutas):

    cantFrutas=int(input("ingrese la cantidad de frutas a comprar: "))

    while cantFrutas<=0:
        cantFrutas=int(input("ingrese la cantidad de frutas a comprar mayor que 0: "))


    for i in range(cantFrutas):
        nomFruta=input("ingrese el nombre de la fruta numero "+str(i)+": ")
        cantKilos=int(input("ingrese la cantidad de kilos "+str(i)+": "))
        nomFruta = nomFruta.lower()
        objFruta=Frutas(nomFruta,cantKilos)
        listaFrutas.append(objFruta)

def valorPagarxFruta(listaFrutas):
    print("nombre","\t","PrecKg","\t","cant","\t","Total")
    for i in range(len(listaFrutas)):
        print(listaFrutas[i].nomFruta,"\t", listaFrutas[i].precioXkg(),"\t\t", listaFrutas[i].cantKilos,"\t\t", round(listaFrutas[i].totalPrecio(),2))

def montoTotalApagar(listaFrutas):
    montoTotalApagar=0
    for i in range(len(listaFrutas)):
        montoTotalApagar=montoTotalApagar+listaFrutas[i].totalPrecio()

    print("el monto total a pagar es: ",montoTotalApagar)


listaFrutas=[]
ingresoInformacion(listaFrutas)
valorPagarxFruta(listaFrutas)
montoTotalApagar(listaFrutas)