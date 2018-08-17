# --- Define your functions below! ---
def intro():
    print("Hi!I'm Chatbot")
def response():
    if answer == "Hey":
        print("How you doing?")
    else:
        print("How are you?")
# --- Put your main program below! ---
def main():
    intro()
    while True:
        response()
        answer = input("(What will you say?) ")
        print("That's cool!")


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
