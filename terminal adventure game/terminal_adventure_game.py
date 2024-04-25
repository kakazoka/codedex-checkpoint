class Player:
  def __init__(self, name):
    self.name = name

def get_choice():
  return int(input('\nWhich option do you choose? '))

def wrong_answer(player):
  print(f'\n{player.name}\'s fear overwhelms them, clouding their judgment and increasing the chances of making fatal mistakes.')
  return get_choice()

def new_game(player):
  print('\nEnter the void again?')
  print('\n1. Yes.'
        '\n2. No.')
  choice = get_choice()
  while choice != 1 and choice != 2:
    choice = get_choice()
  if choice == 1:
    start_game(player)
  if choice == 2:
    print(f'\n{player.name} exited the void.')

def survival(player):
  print(f'\n{player.name} survived the void.')
  new_game(player)

def death(player):
  print(f'\n{player.name} entered the void and sccumbed to its dark embrace.')
  new_game(player)

def confront_hide(player):
  print('\n1. Confront the entity.'
        '\n2. Hide.')
  choice = get_choice()
  while choice != 1 and choice != 2:
    choice = wrong_answer(player)
  if choice == 1:
    print(f'\n{player.name} manages to overpower the entity and escapes the ship.')
    return survival(player)
  elif choice == 2:
    print(f'\nWhile {player.name} evades the entity for a while, it eventually discovers {player.name}\'s hiding place and attacks, resulting in a fatal encounter.')
    return death(player)

def hack_investigate(player):
  print('\n1. Hack into security systems.'
        '\n2. Investigate the engine room.')
  choice = get_choice()
  while choice != 1 and choice != 2:
    choice = wrong_answer(player)
  if choice == 1:
    print(f'\n{player.name} gained access to restricted areas. However, this triggers an alarm that attracts the entity\'s attention, leading to a fatal encounter.')
    return death(player)
  elif choice == 2:
    print(f'\n{player.name} focused on repairing the ship\'s engine, restoring power and functionality.')
    return survival(player)

def repair_salvage(player):
  print('\n1. Repair comunications'
        '\n2. Salvage for survival gear')
  choice = get_choice()
  while choice != 1 and choice != 2:
    choice = wrong_answer(player)
  if choice == 1:
    print(f'\n{player.name} prioritizes repairing the ship\'s communications, sending out a distress signal. A rescue ship arrives in time.')
    return survival(player)
  elif choice == 2:
    print(f'\n{player.name} found enough resources to sustain theirself for a while. However, {player.name} is unable to call for help, and eventually, the entity catches up with them.')
    return death(player)

def start_game(player):
  print(f'\nChoose wisely, captain {player.name}, for your decisions will be either your salvation or your doom.')
  print('\n1. Confront or hide.'
        '\n2. Hack into security systems or investigate the engine room.'
        '\n3. Repair the ship\'s communications or salvage for survival gear.')
  choice = get_choice()
  while choice != 1 and choice != 2 and choice != 3:
    choice = wrong_answer(player)
  if choice == 1:
    confront_hide(player)
  elif choice == 2:
    hack_investigate(player)
  elif choice == 3:
    repair_salvage(player)

name = input('Enter your name: ')
player = Player(name)

print(f'\nYou\'re {player.name}, a valiant captain trapped aboard Elysium, a drifting spaceship.'
      '\nFace an unseen horror lurking in the shadows. Navigate choices that shape your fate as you unravel the ship\'s mysteries and confront the relentless entity hunting you.'
      '\nWill you survive the void and save your crew or succumb to its dark embrace?')

start_game(player)
