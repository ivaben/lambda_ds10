
from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to genarte names

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    products = []
    
    
    # name of product
    for _ in range(num_products):
        adj = sample(ADJECTIVES, 1)
        noun = sample(NOUNS, 1)
        name = adj[0] + ' ' + noun[0]

        

        price = round(uniform(5.0, 55.0), 2)
        weight = round(uniform(5, 85.0), 2)
        flammability = round(uniform(0.0, 2.5), 6)

def genrate_report(products):
    names =[]
    prices =[]
    weights = []
    flammabilities = []

    for _ in products:
        names.append(_.name)
        prices.append(_.price)
        weights.append(_.weight)
        flammabilities.append(_.flammability)


    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names:'{len(set(names))})
    print(f'Average price: $ {round(sum(prices) / len(prices),2)}')
    print(f'Average weight: {round(sum(weights) / len(weights),2)}')
    print(f'Average flammability: {round(sum(flammabilities) / len(flammabilities),2)}')

    return names, prices, weights, flammabilities





        
    



