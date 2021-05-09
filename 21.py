def header(text = "", size = 108, spaces = 6):
    new_size = size - len(text) - spaces
    print_spaces = int(spaces / 2) * " "
    half_size = int((new_size) / 2)
    if text == "":
        print("\n" + "$" * size + "\n")
    elif new_size % 2 == 0:
        print("\n" + "$" * half_size + f"{print_spaces}{text}{print_spaces}" + "$" * half_size + "\n")
    else:
        print("\n" + "$" * half_size + f"{print_spaces}{text}{print_spaces}" + "$" * (half_size + 1) + "\n")

def menu(list, title):
    header(title)
    c = 1
    for item in list:
        print(f"[{c}] {item}")
        c +=1
    answer = int(input("\nEscolha uma opção: "))
    return answer

header()
print("""\
  /$$$$$$    /$$         /$$$$$$$  /$$                     /$$          /$$$$$                     /$$      
 /$$__  $$ /$$$$        | $$__  $$| $$                    | $$         |__  $$                    | $$      
|__/  \ $$|_  $$        | $$  \ $$| $$  /$$$$$$   /$$$$$$$| $$   /$$      | $$  /$$$$$$   /$$$$$$$| $$   /$$
  /$$$$$$/  | $$        | $$$$$$$ | $$ |____  $$ /$$_____/| $$  /$$/      | $$ |____  $$ /$$_____/| $$  /$$/
 /$$____/   | $$        | $$__  $$| $$  /$$$$$$$| $$      | $$$$$$/  /$$  | $$  /$$$$$$$| $$      | $$$$$$/ 
| $$        | $$        | $$  \ $$| $$ /$$__  $$| $$      | $$_  $$ | $$  | $$ /$$__  $$| $$      | $$_  $$ 
| $$$$$$$$ /$$$$$$      | $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$ \  $$
|________/|______/      |_______/ |__/ \_______/ \_______/|__/  \__/ \______/  \_______/ \_______/|__/  \__/\
""")
menu1 = 0
while menu1 != 4:
    menu1 = int(menu(["Play", "How to play", "History", "End"], "Welcome to 21 BlackJack!"))
    if menu1 == 1:
        print(1)
    elif menu1 == 2:
        print(2)
    elif menu1 == 3:
        header("History")
        print("History")
        input("\nAperte a tecla enter para retornar.")
    elif menu1 == 4:
        print(4)
    
