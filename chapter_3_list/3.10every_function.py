cosa = ['pen', 'notes', 'darian', 'tv']
print(cosa[1].title())
print(f"The {cosa[0].title()} is broken")
cosa.sort()
print(cosa)
cosa.sort(reverse=True)
print(cosa)
print(sorted(cosa))
cosa.append('betti')
del cosa[3]
print(cosa)
cosa.insert(2,'darian')
print(cosa)
message = f"{cosa.pop()} isn't a thing"
print(message)
cosa.remove('darian')
print(cosa)
print(len(cosa))