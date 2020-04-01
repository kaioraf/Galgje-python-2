import random

def Create_wordlist():
    text = """Tijdens een muntenveiling van de Postzegel en Muntenveiling zaterdag in heeft een zilveren kwartje met de afbeelding
    van koning uit euro opgeleverd Volgens de Muntenveiling is dit het hoogste bedrag ooit voor munt Het muntje kwam uit een
    collectie van een recent overleden verzamelaar die dit exemplaar eerder op een andere veiling op de kop had getikt Hij is onlangs overleden waardoor
    zijn gehele muntencollectie geveild werd Ook andere munten uit zijn collectie zijn voor forse bedragen geveild Zaterdag is ook de sterfdag van Koning
    hij overleed op november op Paleis Het Hij was vanaf maart tot zijn dood koning van Nederland"""
    text = text.lower()
    woorden = text.split(" ")
    return woorden

woorden = Create_wordlist()
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
Correct_letters = ""
Fouten = 0
klaar = 0
pogingen = []

Play()

def Display_galg():
    global Fouten, klaar

    print("That is not the word... Try again!")
    print(plaatjes[Fouten])
    Fouten += 1
    if Fouten == len(plaatjes):
        print("You lost!")
        klaar = 1
        print("The word was: " + Answer_Galgje)



# hier word het woord met streepjes getoont en kijkt hij naar de Correct_letters string om te kijken naar welke letters de speler al heeft geraden
# hij kijkt of er nog letters niet geraden zijn, anders is alles goed
def Check_word():
    Display = ("")
    for letter in Answer_Galgje:
        if letter in Correct_letters:
            Display = Display + letter + " "
        else:
            Display = Display + "_" + " "
            allesgoed = False
    print(Display)
    return allesgoed


def Guess_letter():
    guess = soort_input
    if len(guess) > 1:
        print("No more than one letter!")
    else:
        if guess in pogingen:
            print("You already guessed that letter!")
        else:
            pogingen.append(guess)
            allesgoed = True
            if guess in Answer_Galgje:
                print("Correct!")
                Correct_letters = Correct_letters + guess

            else:
                Display_galg()

            allesgoed = Check_word()
            if allesgoed:
                Won()

def Won():
    print("You won!")
    klaar = 1


def Guess_word():
    guess = input("Which word?")
    if guess == Answer_Galgje:
        Won()
    else:
        Display_galg()


def Play():
    while klaar == 0:
        soort_input = input(
            "Guess one letter by typing the letter or guess the word by typing '?'")
        if soort_input != "?":
            Guess_letter()
        else:
            Guess_word()

