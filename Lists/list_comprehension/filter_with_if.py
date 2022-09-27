scores = [12, 47, 38, 10, 25, 89]
# we can filter elements of list with list comprehension using conditional
high_scores = [score for score in scores
               if score > 20]

print(high_scores)

prices = [150, 45, 99, 200, 350]

apply_taxes = [price for price in prices
               if price > 150]
print(apply_taxes)

item_prices = [120, 25, 40, 80, 33]
under_50 = [item_price for item_price in item_prices if item_price < 50]
print(under_50)

websites = ["nytimes.com", "lemonde.fr", "economist.com", "lapen.fr"]
french = [website for website in websites if website.count(".fr") > 0]
print(french)

humidity = [40, 35, 20, 70]
ideal = [level for level in humidity if level >= 30 and level <= 50]
print(ideal)
