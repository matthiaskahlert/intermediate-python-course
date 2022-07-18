import random
def main():
# playername input
	player1_name = str(input("What is your name Player 1? "))
	player2_name = str(input("What is your name Player 2? "))
# defining variables
	player1_score = 0
	player2_score = 0
# asking for user input about the dice
	dice_size = int(input("How many sides has the dice? "))
	dice_rolls = int(input("How many dice you want to roll? "))
	dice_sum_player1 = 0
	dice_sum_player2 = 0
	for i in range (0,dice_rolls):
		player1_roll = random.randint(1,dice_size)
		player2_roll = random.randint(1,dice_size)
		dice_sum_player1 = dice_sum_player1 + player1_roll
		dice_sum_player2 = dice_sum_player2 + player2_roll
# player 1 rolls
		if player1_roll ==1:
			print(f'{player1_name} You rolled a {player1_roll}! Critical fail')
			dice_sum_player1 = dice_sum_player1 -5
			print(f'{player1_name} You get -5 Points!')
		elif player1_roll == dice_size:
			print(f'{player1_name} You rolled a {player1_roll}! Critical Success!')
			dice_sum_player1 = dice_sum_player1 + 15
			print(f'{player1_name} You get 15 Points Bonus - How awesome is that!')
		else:
			print(f'{player1_name} You rolled a {player1_roll}')
# player 2 rolls
		if player2_roll ==1:
			print(f'{player2_name} You rolled a {player2_roll}! Critical fail')
			dice_sum_player2 = dice_sum_player2 -5
			print(f'{player2_name} You get -5 Points!')
		elif player2_roll == dice_size:
			print(f'{player2_name} You rolled a {player2_roll}! Critical Success!')
			dice_sum_player2 = dice_sum_player2 + 15
			print(f'{player2_name} You get 15 Points Bonus - How awesome is that!')
		else:
			print(f'{player2_name} You rolled a {player2_roll}')
# comparing the values	
		if player1_roll > player2_roll:
			print(f'{player1_name} wins')
			player1_score = player1_score + 1
		elif player2_roll > player1_roll:
			print(f'{player2_name} wins')
			player2_score = player2_score + 1
		else:
			print(f'Its a draw')
		input('Press a key to continue')
		
# aftermath	
	print("### Game Over ###")
	print(f'{player1_name} You have rolled a total of {dice_sum_player1}')
	print(f'{player2_name} You have rolled a total of {dice_sum_player2}')
	print(f'{player1_name} winning counter:', player1_score)
	print(f'{player2_name} winning counter:', player2_score)

if __name__== "__main__":
  main()