#The only dictionary and set needed
players = {"Suarez": "Uruguay", "Messi": "Argentina", "Coutinho": "Brazil", "Vidal": "Chile", "Rakitic": "Croatia", "Busquets": "Spain", "Roberto": "Spain", "Pique": "Spain", "Lenglet": "France", "Alba": "Spain", "Ter Stegen": "Germany"}
different_countries = set()
#Add the different countries to one set
for player in players:
  different_countries.add(players[player])
#Print the amount of different countries
print("FC Barcelona has players from " + str(len(different_countries)) + " different different countries.\n")
#Print all of the different countries
print("FC Barcelona's players come from: ")
for country in different_countries:
  print(country)