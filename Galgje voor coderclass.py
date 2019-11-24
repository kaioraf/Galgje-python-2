import random
text = """Tijdens een muntenveiling van de Postzegel en Muntenveiling zaterdag in heeft een zilveren kwartje met de afbeelding
van koning uit euro opgeleverd Volgens de Muntenveiling is dit het hoogste bedrag ooit voor munt Het muntje kwam uit een
collectie van een recent overleden verzamelaar die dit exemplaar eerder op een andere veiling op de kop had getikt Hij is onlangs overleden waardoor
zijn gehele muntencollectie geveild werd Ook andere munten uit zijn collectie zijn voor forse bedragen geveild Zaterdag is ook de sterfdag van Koning
hij overleed op november op Paleis Het Hij was vanaf maart tot zijn dood koning van Nederland"""
text = text.lower()
woorden = text.split(" ")
plaatjes = [

    """    
________
""",
    """
    |    
    |    
    |    
    |   
____|____
""",
    """
    ______
    |    
    |    
    |    
    |   
____|____
""",
    """
    ______
    |    |
    |    
    |    
    |   
____|____
""",
    """
    ______
    |    |
    |    o
    |    
    |   
____|____
""",
    """
    ______
    |    |
    |    o
    |   /|\  
    |   / \\
____|____
"""]


Answer_Galgje = woorden[random.randrange(len(woorden))]
print("Welcome to Hangman!")
All_correct = ""
Fouten = 0
klaar = 0
pogingen = []


def Display_galg():
    global Fouten, klaar

    print("Fout! probeer het nog een keer")
    print(plaatjes[Fouten])
    Fouten += 1
    if Fouten == len(plaatjes):
        print("Je hebt verloren!")
        klaar = 1
        print("het woord was: " + Answer_Galgje)


while klaar == 0:
    soort_input = input(
        "raad of een enkele letter of een heel woord. Voor een letter typ: een letter voor een woord typ: '?'")
    if soort_input != "?":
        guess = soort_input
        if len(guess) > 1:
            print("Niet meer dan één letter!")
        else:
            if guess in pogingen:
                print("Die letter heb je al geraden!")
            else:
                pogingen.append(guess)
                allesgoed = True
                if guess in Answer_Galgje:
                    print("Goed!")
                    All_correct = All_correct + guess

                else:
                    Display_galg()

                # hier word het woord met streepjes getoont en kijkt hij naar de All_correct string om te kijken naar welke letters de speler al heeft geraden
                # hij kijkt of er nog letters niet geraden zijn, anders is alles goed en stopt hij het spel
                Display = ("")
                for letter in Answer_Galgje:
                    if letter in All_correct:
                        Display = Display + letter + " "
                    else:
                        Display = Display + "_" + " "
                        allesgoed = False
                print(Display)
                if allesgoed:
                    print("Je hebt gewonnnen!")
                    klaar = 1
    else:
        guess = input("Welk woord?")
        if guess == Answer_Galgje:
            print("Je hebt gewonnnen!")
            klaar = 1
        else:
            Display_galg()
