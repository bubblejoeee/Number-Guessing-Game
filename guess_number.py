import random

def generate(max) :
	random_num = random.randint(1,max)
	return random_num
	
def play() :
	print('🎮Number Guessing Game🎮\n')
	try :
		input_max = int(input('Enter a max number: '))
		secret_num = generate(input_max)
		print(f"Game started\n")
		attempt = 1
	except ValueError :
		print('Please put a number only😡')
		play()
	
	
	while True :
		try :
			print(f"📢Attempt {attempt}📢")
			user_input = int(input(f"Guess the number from 1-{input_max}:\n>>> "))
		
			if user_input == secret_num :
				print(f"\n🎊🎉Congratulations. You guessed the right number from 1-{input_max} within {attempt} attempt🎉🎊")
				attempt = 1
				print("Play again?\nAny keys for yes. Otherwise 'No'")
				play_again = input('>>> ').lower()
				if play_again == 'no' :
					print('Thanks for playing❤')
				else :
					print('Alright!😍\n')
					play()
				break
			
			elif user_input > input_max or user_input < 1 :
				print(f"Please put a number not lower than 1 or higher than {input_max}")
			
			elif user_input < secret_num :
				print('Go higher⏫')
				attempt += 1
				
			elif user_input > secret_num :
				print('Go lower⏬')
				attempt += 1
				
		except ValueError as e :
			print("Please put a number only😡")

play()