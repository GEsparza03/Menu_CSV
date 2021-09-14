import datetime

class Automovil:
    matricula = ""
    marca = ""
    modelo = ""
    año = 0
    estado = ""
    momento = ""
    def __init__(self, matricula, marca, modelo, año, estado, momento = ""):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.estado = estado
        if momento == "":
            x = datetime.datetime.now()
            momento = x.strftime("%d/%m/%Y %H:%M:%S")
            self.momento = momento
        else:
            self.momento = momento
