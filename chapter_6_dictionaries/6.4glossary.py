glossary = {
            'variable': 'it is a tag poiting to a memory address', 
            'list': 'Store any kind of data', 
            'dictionary': 'Like a list, but stores key-value pair of information', 
            'str': 'String value', 
            'bool': 'True or false value'
            }

new_definitions = {
                    'print': 'function that print the specified message to the sceem',
                    'for loop': 'a way to repeat a block of code a fixed number of times',
                    'range': 'returns a sequence of numbers',
                    'int': 'integer numbers',
                    'float': 'real numbers'
                   }

for key, value in glossary.items():
    print(f'{key.title()}: \n\t{value}')
    print('\n')

glossary.update(new_definitions)

for key, value in glossary.items():
    print(f'{key.title()}: \n\t{value}')
    print('\n')


