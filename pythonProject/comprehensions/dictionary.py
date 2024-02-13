cities = ["Nairobi","Kampala", "Mumbai"]
countries = ["Kenya", "Uganda", "India"]

capitals = zip(cities,countries)
print(capitals)

capita = {city:country for city,country in capitals}
print(capita)