favorite_lenguages = {
                      'carlas': 'ruby on rails',
                      'betti': 'neither',
                      'mati': 'python',
                      'papa': 'cobol',
                      'damaris': 'c#'
                      }

some_friends = ['carlas', 'gustavo', 'ivan', 'romi', 'damaris']

for name in some_friends:
    if name in favorite_lenguages.keys():
        print(f'\n{name.title()}, thank you for take my poll!')
    else:
        print(f'\n{name.title()}, You should to take my poll, please')
 
