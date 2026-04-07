def teste():
    global n
    x = 8
    print(f"Na função N vale: {n}")
    print(f"A variavel local X vale: {x}")
    n += x


n = 2
print(f"No programa principal N vale: {n}")
teste()
print(f"N Global agora vale: {n}")