list_corvidos = {
                'trails': ['voge dsx 900', 'voge dsx 650', 'voge dsx 525',], 
                'enduro': ['royal enfield himalayan 450', 'voge 300 rally', 'cfmoto 450 mt',], 
                'others': ['zontes 703f', 'benelli trk 702 x', 'cfmoto 650 gt',]
                }

for kind, motos in list_corvidos.items():
    print(f"{kind.title()}:")
    for moto in motos:
        print(f"\n\t\t\t{moto.title()}")
