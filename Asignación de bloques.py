#Primer ejemplo pra los bloques de memoria
class Proceso:
    def __init__(self, id_proceso, tamano):
        self.id_proceso = id_proceso
        self.tamano = tamano

class BloqueMemoria:
    def __init__(self, id_bloque, capacidad):
        self.id_bloque = id_bloque
        self.capacidad = capacidad
        self.memoria_disponible = capacidad
        self.procesos = []

    def asignar_proceso(self, proceso):
        if proceso.tamano <= self.memoria_disponible:
            self.procesos.append(proceso)
            self.memoria_disponible -= proceso.tamano
            return True
        else:
            return False

def asignar_procesos(procesos, bloques):
    for proceso in procesos:
        for bloque in bloques:
            if bloque.asignar_proceso(proceso):
                break

    print("Asignación de procesos a bloques:")
    for bloque in bloques:
        print(f"Bloque {bloque.id_bloque}: {len(bloque.procesos)} procesos asignados")

# Crear procesos y bloques de memoria
procesos = [
    Proceso(1, 212),
    Proceso(2, 417),
    Proceso(3, 112),
    Proceso(4, 426)
]

bloques = [
    BloqueMemoria(1, 100),
    BloqueMemoria(2, 500),
    BloqueMemoria(3, 200),
    BloqueMemoria(4, 300),
    BloqueMemoria(5, 600)
]

# Asignar procesos a bloques de memoria
asignar_procesos(procesos, bloques)



"""#Segundo ejemplo pra los bloques de memoria
class Proceso:
    def __init__(self, id_proceso, tamano):
        self.id_proceso = id_proceso
        self.tamano = tamano

class BloqueMemoria:
    def __init__(self, id_bloque, capacidad):
        self.id_bloque = id_bloque
        self.capacidad = capacidad
        self.memoria_disponible = capacidad
        self.procesos = []

    def asignar_proceso(self, proceso):
        if proceso.tamano <= self.memoria_disponible:
            self.procesos.append(proceso)
            self.memoria_disponible -= proceso.tamano
            return True
        else:
            return False

def asignar_procesos(procesos, bloques):
    for proceso in procesos:
        bloques_disponibles = [bloque for bloque in bloques if bloque.memoria_disponible >= proceso.tamano]
        if bloques_disponibles:
            bloque_asignado = min(bloques_disponibles, key=lambda x: x.memoria_disponible)
            bloque_asignado.asignar_proceso(proceso)

    print("Asignación de procesos a bloques:")
    for bloque in bloques:
        print(f"Bloque {bloque.id_bloque}: {len(bloque.procesos)} procesos asignados")

# Crear procesos y bloques de memoria
procesos = [
    Proceso(1, 212),
    Proceso(2, 417),
    Proceso(3, 112),
    Proceso(4, 426)
]

bloques = [
    BloqueMemoria(1, 100),
    BloqueMemoria(2, 500),
    BloqueMemoria(3, 200),
    BloqueMemoria(4, 300),
    BloqueMemoria(5, 600)
]

# Asignar procesos a bloques de memoria
asignar_procesos(procesos, bloques)"""

