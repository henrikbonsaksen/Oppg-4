from hangman import correct_guess

def main():
    løsning = "hangman"
    forsøk = "efgh"
    neste = input("Tipp EN bokstav \n")
    resultat = correct_guess(løsning, forsøk, neste)

    if resultat == True:
        print("Korrekt!")
    elif resultat == None:
        print("Enten for langt eller allerede tippet!")
    else:
        print("Feil")
        
main()

if __name__ == "__main__":
    main()
