#durak
# - passing rule not applied

suits = "SHDC"
faces = "6789TJQKA"
deck = None;
def draw(n=1):
    n = min(n, len(deck))
    drawn = deck[-n:]
    del deck[-n:]
    return drawn
	
def reset_deck():
    global deck
    deck = [(f,s) for s in suits for f in faces]
    shuffle(deck)

reset_deck();
trump = deck[0]
players = [ (id, draw(6)) for id in range(4) ]

suit = lambda card: card[1]
face = lambda card: card[0]
	
def pid(player):
	return player[0]

def hand(player):
	return player[1]

def mintrump(player):
	"""
	"""
	minimum = 1000
	for card in hand(player):
		if suit(card) == suit(trump):
			if faceval[face(card)] < minimum:
				minimum = faceval[face(card)]
	return minimum

curplayer = sorted(players,key=mintrump)[0]

#TO DO IMPLEMENT OPTIONAL
def reqchoice(player, choices, optional, msg=''):
	print("Player %d:"%pid(player), msg)
	for i,c in enumerate(choices):
		print(str(i)+':','%s%s'%c)
	index = int(input("Type in the index of your choice: "))
	
	#not checking for validity yet
	return index

def playcard(player, index):
	card = hand(player)[index]
	del hand(player)[index]
	return card

atkidx = reqchoice(attacker, hand(attacker), optional=False, msg="Play an attack against Player %d"%pid(defender))
attack = playcard(attacker, atkidx)

field = [[attack]] #list of [attack,defence] pairs

def beats(defense, attack):
	"""
	Returns True if defense's card "beats" attack
	"""
	if(suit(defense) == suit(attack)):
		return faceval[face(defense)] > faceval[face(attack)]
	return suit(defense) == suit(trump)
	

pickup = False
	
while !pickup:
	open_attacks = filter(lambda pair: len(pair)<2, field)
	for attack in open_attacks:
		choices = filter(lambda card: beats(card, attack), hand(defender))
		choices = list(choices) #absorb into list
		if len(choices) == 0:
			break
		defidx = reqchoice(defender, choices, True, msg='You are under attack! Prepare Your Defenses!');
		
		attack = playcard(attacker, atkidx)

	
#possible_defenses = filter(lambda card: beats(card, attack), hand(defender))
# this is a generator, not a list.  (Apply next())
		
		
		
		
		
		
		
		
		
		
