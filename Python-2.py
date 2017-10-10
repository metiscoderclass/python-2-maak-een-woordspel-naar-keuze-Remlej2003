print("We gaan galgje spelen")
gwoord = "visjes"
while True:
    letter = str(input("Geef een letter "))
    print("je schreef " + letter)
    if letter in gwoord:
        print ("letter is goed")
    elif letter == "?":
        hwoord = str(input("geef het hele woord"))
        if hwoord == gwoord:
            print("je hebt gewonnen")
            break
    elif letter != gwoord:
        print ("je bent slecht")

