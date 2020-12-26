# Brazilian Soccer Championship

ranking = ("São Paulo", "Flamengo", "Atlético-MG", "Internacional", "Grêmio", "Palmeiras", "Fluminense",
 "Santos", "Corinthians", "Ceará","Atlético-GO", "Athletico-PR", "Red Bull Bragantino", "Fortaleza", "Sport",
 "Bahia", "Vasco da Gama", "Botafogo", "Coritiba", "Goiás")

print("-=" * 30)
print(f"List of the teams of Brazilian Championship: {ranking}")
print("-=" * 30)
print(f"The top 5 teams are: {ranking[0:5]}")
print("-=" * 30)
print(f"Teams sorted in Alphabetic order: {sorted(ranking)}")
print("-=" * 30)
flu = ranking.index("Fluminense")
print(f"Fluminense is on the {flu + 1}th position.")