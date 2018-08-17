import json
# TODO Part I: Add your survey questions to this empty list.
survey = ["What is your name?", "What is your favorite color?", "What is your favorite food?", "What is your favorite book?", "What is your favorite candy?"]

# TODO Part I: store the related keys corresponding to the survey answers here.
keys = ["name", "color", "food", "book", "candy"]

# Create a list that will store each person's individual survey responses.
# Use for Part II.
list_of_answers = []

# Creates the dictionary to store responses.
answers = {}

# TODO Part I: write code that asks each survey question and prompts the user for a response.
# Hint: how can you go through each element of a list?
while True:
    answers = {}
    for i in range(len(survey)):
        response = input(survey[i] + " ")
        answers[keys[i]] = response
    list_of_answers.append(answers)
    user_input =input("Do you want to continue?")
    if user_input == "no":
        break
print(list_of_answers)
# Open the file containing all past results and append them to our current list.
f = open("allanswers.json", "r")
olddata = json.load(f)
list_of_answers.extend(olddata)
f.close()

# Reopen the file in write mode and write each entry in json format.
f = open("allanswers.json", "w")
f.write('[\n')
index = 0
for t in list_of_answers:
    if (index < len(list_of_answers)-1):
        json.dump(t, f)
        f.write(',\n')
    else:
        json.dump(t, f)
        f.write('\n')
    index += 1

f.write(']')
f.close()


# Print the context of the dictionary.
print(answers)

#TODO Part II: Delete the quotes. This will print each individual's survey responses
"""
#Example of how to iterate over the list of dictionaries and pull out particular pieces of information.
names = []
for s in range(len(list_of_answers)):
    names.append(list_of_answers[s]["name"])
print(names)
"""
