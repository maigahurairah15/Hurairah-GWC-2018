# Update this text to match your story.
start = '''
You are at school, in the middle of class. Your physics teacher is explaining how to
calculate the energy that masses can contain. The room is hot, damp, not a favorable
enviornment to learn something so complex. The teacher's monotone voice influences
your mind to wander. Even your peers look like they are going to fall asleep.
As you unconsciously twirl your pencil, you looked out to the grey distance to
find your friends. They were laughing gleefully. You look out the door. You might
make it out before the teacher catches you if you are fast enough...
'''

print(start)

print("Type 'cut class' to leave class or 'stay' to go stay in class.") # Update to match your story.
user_input = input()
if user_input == "cut class":
    print("The teacher turns his back around to write a formula on the board.")
    print("The chance presented itself and you quickly dash out the door.")
    print("Your peers are not going to bother stopping you or let the teacher know.")
    print("You decided this...")
    print("Anyways, you meet up with your friends but it seems like they can't agree with something.")
    print
if user_input == "stay":
    print("The teacher resumes the class while your peers begin to fall asleep.")
    print("You have the choice to join your fellow peers or pick on your teacher.")
    print("Type 'peers' to join them or 'teacher' to pick on teacher.")
user_input= input()
if user_input == "peers":
    print("...zzzz you begin to zone out")
    print(".....dreaming about the party you could have been at,you begin to hear a noise")
    print("THUD! the teacher drops a heavy textbook on your desk")
    print("the teacher, filled with rage asks 'why were you sleeping?'")
    print("why were you sleeping?")
    answer=input("why were you sleeping?")
    print(answer, "THAT IS NOT A GOOD ENOUGH REASON!!!")
    print("yikes! the teacher is not pleased, and now you have detention.")

    # continue code to finish story.

elif user_input == "stay":
    print("You choose to go right and ...") # Update to match your story.
