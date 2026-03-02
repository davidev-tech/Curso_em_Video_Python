times1 = ("Athletico-PR ", "Atlético-MG", "Bahia", "Botafogo", "Chapecoense", "Corinthians", "Coritiba", "Cruzeiro", "Flamengo", "Fluminense")
times2 = ("Grêmio", "Internacional", "Mirassol", "Palmeiras", "Red Bull Bragantino", "Remo", "Santos", "São Paulo", "Vasco da Gama", "Vitória") 
times = times1 + times2

print("=" * 30)
print(f"A lista do Brasileirão por posição do primeiro para o ultimo: {times}")
print("=" * 30)
print(f"Os cinco primeiros times da tabela do campeonato Brasileirão: {times[0:5]}")
print("=" * 30)
print(f"Os Quatro ultimos times da tabela do Brasileirão: {times[-4:]}")
print("=" * 30)
print(f"A lista de times do campeonato em ordem alfabetica: {sorted(times)}")
print("=" * 30)
print(f"O time da Chapecoense se encontra no indice {times.index("Chapecoense") + 1}° Posição.")