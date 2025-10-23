colour = input("What's your favourite colour?: ")
age = input("How old are you?: ")

if colour.lower() == "red" and age == 16:
  print("Snap! Are you my twin?")

if colour.lower() == "red" or age == 16:
  print("Spooky! You're a bit like me.")

else:
  print("We're not so similar, you and I.")