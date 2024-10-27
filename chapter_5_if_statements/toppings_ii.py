available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineaple', 'extra cheese']

recuested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for recuested_topping in recuested_toppings:
    if recuested_topping in available_toppings:
        print(f'Adding {recuested_topping}.')
    else:
        print(f"Sorry, we don't have {recuested_topping}.")

print("\nFinished making your pizza!")
