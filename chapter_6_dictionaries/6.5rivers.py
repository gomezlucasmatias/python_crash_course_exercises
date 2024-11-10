rivers = {'nilo': 'egipto', 'amazonas': 'brasil', 'yangsté': 'china'}
for key, value in rivers.items():
    print(f'\nThe {key.title()} runs through {value.title()}')

print('\nThe rivers are:')

for key in rivers.keys():    
    print(f'\n\t\t{key.title()}')

print('\n\nThe countries are:')

for value in rivers.values():    
    print(f'\n\t\t{value.title()}')
