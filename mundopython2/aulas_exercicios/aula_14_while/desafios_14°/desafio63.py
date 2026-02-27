numeros_fibonacci = int(input("Quantos números da sequencia de Fibonacci deseja ver? "))
fibonacci = 0
fibonacci_antecessor = 1
fibonacci_atual = fibonacci_antecessor + fibonacci
contador = 2
print(f"{fibonacci} --> {fibonacci_antecessor}", end=" --> ")
while contador < numeros_fibonacci:
    fibonacci_atual = fibonacci_antecessor + fibonacci
    fibonacci = fibonacci_antecessor
    fibonacci_antecessor = fibonacci_atual
    print(f"{fibonacci_atual}", end=" --> " if contador < numeros_fibonacci - 1 else "")
    contador += 1