import random
def main():
	dice_rolls = 2
	dice_sum = 0
	for i in range (0,dice_rolls):
		print('You rolled a die')
		roll = random.randint(1,20)
		print(f'You rolled a {roll}')
		dice_sum = dice_sum + roll
	print(f'You have rolled a total of {dice_sum}')
if __name__== "__main__":
  main()