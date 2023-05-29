times = [
    "Fluminense",
    "Botafogo",
    "Fortaleza",
    "Palmeiras",
    "Vasco da Gama",
    "Internacional",
    "Bragantino",
    "Flamengo",
    "São Paulo",
    "Goiás",
    "Athletico-PR",
    "Grêmio",
    "Corinthians",
    "Cuiabá",
    "Atlético-MG",
    "Santos",
    "Bahia",
    "Coritiba",
    "América-MG"
]
print('Lista de Times', times)
print(f'Cinco primeiros {times[:5]}')
print(f'Cinco primeiros {times[-4:]}')

print(f'A ordem alfabetica {sorted(times)}')
print(f'Onde está o Flamengo? {times.index("Flamengo")+1}' + 'ª posição')
#print(times)