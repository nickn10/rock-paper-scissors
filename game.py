import random

user_options = ['(r)Rock','(p)Paper','(s)Scissors','(q)Quit']
comp_options = ['Rock','Paper','Scissors']
winning_cases = [('Rock','Scissors'),('Paper','Rock'),('Scissors','Paper')]
valid_choices = {
  'rock': 'Rock',
  'paper': 'Paper',
  'scissors': 'Scissors',
  'quit': 'quit',
  'r': 'Rock',
  'p': 'Paper',
  's': 'Scissors',
  'q': 'quit'
}

# Display player choices
def showOptions():  
  print('Choose one:')
  for x in user_options:
    print(x)

showOptions()

player_score = 0
comp_score = 0

while True:
  # PROMPT PLAYER FOR INPUT
  player_choice = input('Enter Choice(case-insensitive): ').lower()

  # Check for valid input
  if not valid_choices.get(player_choice, None):
    print('\nPlease enter a valid choice.')
    showOptions()
    continue
  elif valid_choices.get(player_choice) == 'quit':
    break

  player = valid_choices[player_choice]

  # Generate random number for comp choice 
  comp = comp_options[random.randint(0,2)]
  
  #Display player and comp choices
  print('----------------------------')
  print('          Result:           ')
  print(f'You: {player} | Comp: {comp}')

  # Check for draw
  if player == comp:
    print("It's a Draw")
  # Player Wins
  elif (player,comp) in winning_cases:
    print(f'{player} beats {comp}')
    print('You Win!!!')
    player_score += 1
  # Player Loses
  else: 
    print(f'{comp} beats {player}')
    print('You Lose :(')
    comp_score += 1
  print('----------------------------')
  print('Current Score:')
  print(f'You: {player_score} | Comp: {comp_score}')
  print('----------------------------\n')
print('\nThanks for playing!\n')
