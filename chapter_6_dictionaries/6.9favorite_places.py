favorite_places = {
                   'darian': ['rusia', 'paraguay', 'new zeland'],
                   'ame': ['korea', 'japon', 'mexico'],
                   'artemisa': ['window', 'stairs', 'yard'],
                   }

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite place are:")
    for place in places: 
        print(f"\t\t\t\t{place.title()}")
