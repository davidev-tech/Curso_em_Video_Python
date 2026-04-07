def calcular_fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = calcular_fatorial(5)
f2 = calcular_fatorial(4)
f3 = calcular_fatorial()

print(f"O resultados foram: {f1}, {f2}, {f3}")