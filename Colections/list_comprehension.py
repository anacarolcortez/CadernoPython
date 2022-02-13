def acrescenta_um(idade):
    return idade+1


idades = [78, 25, 12, 9, 33, 54, 41, 49, 57, 20, 16]

# list comprehension: gerar listas por meio de iterações mais "enxutas"
idades2 = [acrescenta_um(idade) for idade in idades if idade > 18]

print(idades2)
