list_of_trails = ['Voge 525 dsx', 'Voge 650 dsx', 'Voge 900 dsx', 'RVM Tekken 300', 'RVM Tekken 500', 'RVM Tekken 250', 'Benelli TRK 702', 'Voge 525 ds', 'Voge 650 ds', 'CFMOTO MT 450']

print('My three favorites trails in terms of price-performance are: ')
for trail in list_of_trails[:3]:
    print(trail)

print("\nThese Trails are mounted in Argentina")
for trail in list_of_trails[3:7]:
    print(trail)

print("\nThese are very good trails")
for trail in list_of_trails[-3:]:
    print(trail)

