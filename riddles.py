# --- Define your functions below! ---
def say_hi(name):
    print("Hi " + name)
    ask()

def ask():
    answer = input("Wanna hear a joke?")
    if  answer == "yes":
        response = input("Okay, Why should you stand in the corner if you get cold?")
        punchline(response)
    elif answer == "no":
        print("oops :(  I'm sorry you're no fun.")

def punchline(guess):
    unknown=["I don't know", "idk", "i dont know", "um"]
    if guess != "it's always 90 degrees":
        print("Try one more time")
    if guess in unknown:
        print("It's always 90 degrees")
        response_2()
    elif guess == "it's always 90 degrees":
        print("Yay!! You got it.")
        response_2()
def response_2():
    answer = input("Want to hear another joke?")
    if  answer == "yes":
        print("Alright, what did the ocean say to the sailboat?")
    elif answer == "no":
        print("oops :(  I'm sorry you're no fun.")
def answer_2():
    idk=["I don't know", "idk", "i dont know", "um"]
    guess= input()
    if guess in idk:
        print("Nothing, it just waved.")
        reponse_3
    if guess == "Nothing, it just waved":
        print("Yay!! You got it.okay last one.")
        reponse_3
def reponse_3():
    print("knock, knock")

# --- Put your main program below! ---
def main():
    user = input("what's your name?")
    say_hi(user)

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
