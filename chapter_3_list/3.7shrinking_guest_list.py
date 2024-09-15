guest_list = ['Lewis Carrol', 'Nicola Tesla', 'Roald Dahl', 'Albert Einstein', 'Linus Torvalds', 'Isaac Newton']
print("I'm very sorry dear friends, I can only invite two peoples to my dinner")
print(f"Dear {guest_list.pop()} I am very sorry I can invite you to my dinner")
print(f"Dear {guest_list.pop()} I am very sorry I can invite you to my dinner")
print(f"Dear {guest_list.pop()} I am very sorry I can invite you to my dinner")
print(f"Dear {guest_list.pop()} I am very sorry I can invite you to my dinner")
print(f"Dear {guest_list[0]}, I would love it if you could come to a dinner that I will be hosting with other great minds that humanity has had.")
print(f"Dear {guest_list[1]}, I would love it if you could come to a dinner that I will be hosting with other great minds that humanity has had.")
del guest_list[0]
del guest_list[0]
print(guest_list)