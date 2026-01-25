my_empty_dictionary = {}

my_menu = {"lasagna": 14.75, "moussaka": 21.15, "sushi": 16.05}

my_menu = {
    "sushi": {"price": 19.25, "best_served": "cold"},
    "paella": {"price": 15, "best_served": "hot"},
}

########## get
print(my_menu["sushi"])
print(my_menu.get("paella"))
print(my_menu['paella'])

########## items, keys & values
print(my_menu.items())
print(my_menu.keys())
print(my_menu.values())

########## insert
my_menu["samosas"] = 13
print(my_menu.items())

########## modify
print(my_menu.get("sushi"))
my_menu["sushi"] = 20
print(my_menu.get("sushi"))

########## remove
del my_menu
del my_menu["sushi"]
my_menu.clear()

########## iterate
for key, value in my_menu.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")

for dish in my_menu:
    print(dish)

for prices in my_menu.values():
    print(prices)