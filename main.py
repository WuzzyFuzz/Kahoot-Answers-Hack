import json
import urllib.request
from termcolor import colored

print(colored('Kahoot Answers Hack', 'green'))

def get_answers(id):
  url = f"https://play.kahoot.it/rest/kahoots/{id}"
  color_list = ["red", "blue", "yellow", "green"]
  try:
    with urllib.request.urlopen(url) as response:
      data = response.read()
    questions = json.loads(data)["questions"]

    for index, slide in enumerate(questions):
      for i, choice in enumerate(slide.get("choices", [])):
        if choice.get("correct", False):
          print(colored(f"{index+1}: {choice.get('answer')}", 'green'))
          print(colored(f"{color_list[i]}", 'green'))
          print()
  except urllib.error.HTTPError:
    print(colored('Error: Invalid or non-existent Kahoot ID. Please enter a valid ID.', 'red'))

while True:
  get_answers(input(colored("Enter quizid:", 'green')))

  