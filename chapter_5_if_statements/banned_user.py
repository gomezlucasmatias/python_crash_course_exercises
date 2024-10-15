banned_users = ['Vanina', 'Pablo', 'Paulina', 'Rosalia']

user = input("Login your usser: ")

if user in banned_users:
    print(f"{user} Can't  comment, {user} is banned")
else:
    print("You can comment in this forum")
