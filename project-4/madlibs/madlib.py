def mad_libs():
    print("Let's play mad libs! Fill in the blanks in your own words.")

    name = input("Give me a name: ")
    place = input("Give me a place: ")
    funny_adj = input("Give me an adjective: ")
    random_obj = input("Give me an object: ")
    animal = input("Give me an animal: ")
    action_verb = input("Give me a verb: ")
    funny_exclamation = input("Give me an exclamation: ")

    story = f'''
    Once upon a time, there was a person named {name} who lived in {place}.
    They were a very {funny_adj} person who loved to {action_verb} {random_obj}.
    One day, they saw a {animal} and {funny_exclamation}!'''

    print("\nHere is your madlib story: ")
    print(story)

if __name__ == "__main__":
    mad_libs()
