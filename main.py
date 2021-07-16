from art import logo, vs
from game_data import data
import random, os

a_dict = random.choice(data)
b_dict = random.choice(data)
is_game_over = False
score = 0

def a_data(a_dict):
  name = a_dict["name"]
  follower_count = a_dict["follower_count"]
  description = a_dict["description"]
  country = a_dict["country"]
  print(f"Compare A: {name}, a {description}, from {country}.")
  return follower_count

def b_data(b_dict):
  name = b_dict["name"]
  follower_count = b_dict["follower_count"]
  description = b_dict["description"]
  country = b_dict["country"]
  print(f"Against B: {name}, a {description}, from {country}.")
  return follower_count 

def compare(choice, a_count, b_count):
  if choice == "a" and a_count > b_count:
    return True
  elif choice == "b" and b_count > a_count:
    return True

while not is_game_over:
  print(logo)

  if score > 0:
    print(f"You got it! Current score: {score}")

  a_count = a_data(a_dict)
  print(vs)
  b_count = b_data(b_dict)

  choice = input("Who has more Instagram followers? Type 'A' or 'B': ").lower()
  comparison = compare(choice, a_count, b_count)
  os.system("clear")
  if comparison:
    a_dict = b_dict
    b_dict = random.choice(data)
    score += 1
  else:
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    is_game_over = True
