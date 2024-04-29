def atrapar_ladrones(policias, ladrones, k):
    asignaciones = 0
    i, j = 0, 0  # Índices para policias y ladrones

    while i < len(policias) and j < len(ladrones):
        if abs(ladrones[j] - policias[i]) <= k:
            asignaciones += 1
            i += 1
            j += 1
        elif policias[i] < ladrones[j]:
            i += 1
        else:
            j += 1
    
    return asignaciones

# Ejemplo de uso
arr = ['p', 'p', 'l', 'l', 'p', 'l', 'p', 'p', 'l', 'p']
K = 1
resultado = atrapar_ladrones([i for i, x in enumerate(arr) if x == 'p'], [i for i, x in enumerate(arr) if x == 'l'], K)
print("Número de asignaciones:", resultado)



"""def atrapar_ladrones2(policias, ladrones, k):
    asignaciones = 0
    i, j = 0, 0  # Índices para policias y ladrones

    while i < len(policias) and j < len(ladrones):
        if abs(ladrones[j] - policias[i]) <= k:
            asignaciones += 1
            i += 1
            j += 1
        elif policias[i] < ladrones[j]:
            i += 1
        else:
            j += 1
    
    return asignaciones

# Ejemplo de uso
arr = ['p', 'l', 'l', 'p', 'p', 'l', 'l', 'p', 'l', 'p','l', 'p']
K = 3
resultado = atrapar_ladrones2([i for i, x in enumerate(arr) if x == 'p'], [i for i, x in enumerate(arr) if x == 'l'], K)
print("Número de asignaciones:", resultado)"""



"""def atrapar_ladrones3(policias, ladrones, k):
    asignaciones = 0
    i, j = 0, 0  # Índices para policias y ladrones

    while i < len(policias) and j < len(ladrones):
        if abs(ladrones[j] - policias[i]) <= k:
            asignaciones += 1
            i += 1
            j += 1
        elif policias[i] < ladrones[j]:
            i += 1
        else:
            j += 1
    
    return asignaciones

# Ejemplo de uso
arr = ['l', 'l', 'p', 'l', 'p', 'l', 'l', 'p', 'l', 'p','l', 'p','l','l','p','p','p']
K = 3
resultado = atrapar_ladrones3([i for i, x in enumerate(arr) if x == 'p'], [i for i, x in enumerate(arr) if x == 'l'], K)
print("Número de asignaciones:", resultado)"""
