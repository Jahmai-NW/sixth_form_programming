import random

# Predefined word lists
nouns = ["cat", "dog", "robot", "teacher", "car", "banana"]
verbs = ["jumps", "runs", "flies", "eats", "drives", "sings"]
adjectives = ["happy", "blue", "fast", "loud", "silly", "bright"]

# Function to generate a random sentence
def generate_sentence():
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    adjective = random.choice(adjectives)
    sentence = "The " + adjective + " " + noun + " " + verb + "."
    return sentence

# Generate and print 5 random sentences
for count in range(5):
    print(generate_sentence())
