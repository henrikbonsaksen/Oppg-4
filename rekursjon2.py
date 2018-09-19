#Oppgave 4 - Rekursjon


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def main():
    try:
        ask = input("Skriv inn et tall\n")
        ask = int(ask)
        if ask == int:
            return ask    
    except:
        print("Dette var jammen ikke et heltall! :(")

    print(fibonacci(ask))

main()
