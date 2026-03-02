print("Os número entre 1 e 50 que são pares são:")
print("-=-" * 26)

for x in range(2,51, 2):
    if x % 2 == 0:
        print(f"{x}", end=" ")
print("FIM!")
print("-=-" * 26)