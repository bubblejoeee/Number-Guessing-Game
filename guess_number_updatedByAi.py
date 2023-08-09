import random

def generate(max):
    random_num = random.randint(1, max)
    return random_num

best_attempts = {'easy': float('inf'), 'medium': float('inf'), 'hard': float('inf'), 'insane': float('inf')}

def save_best_attempts_to_file(best_attempts):
    with open('best_attempts.txt', 'w') as file:
        for mode, attempts in best_attempts.items():
            file.write(f"{mode.capitalize()}: {attempts}\n")

def load_best_attempts_from_file():
    try:
        with open('best_attempts.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                mode, attempts = line.strip().split(': ')
                try:
                    best_attempts[mode.lower()] = int(attempts)
                except ValueError:
                    continue
    except FileNotFoundError:
        pass

def display_stats():
    print("\nBest Attempts Statistics:")
    for mode, attempts in best_attempts.items():
        print(f"{mode.capitalize()}: {attempts}")

def play():
    load_best_attempts_from_file()

    def input_difficulty():
        print('🎮Number Guessing Game🎮\n')
        print('Choose Difficulty: Easy, Medium, Hard, Insane')
        difficulty = 0
        difficulty_mode = None
        while difficulty == 0:
            chosen_difficulty = input('>>> ').lower()
            if chosen_difficulty == 'easy':
                difficulty = 10
                difficulty_mode = 'Easy'
            elif chosen_difficulty == 'medium':
                difficulty = 50
                difficulty_mode = 'Medium'
            elif chosen_difficulty == 'hard':
                difficulty = 100
                difficulty_mode = 'Hard'
            elif chosen_difficulty == 'insane':
                difficulty = 200
                difficulty_mode = 'Insane'
            else:
                print('Please type EASY, MEDIUM, HARD, OR INSANE only')
        return difficulty, difficulty_mode

    def play_again():
        print("Play again?\nAny key for yes. Otherwise 'No'.")
        play_again = input('>>> ').lower()
        return play_again == 'no'

    while True:
        difficulty, difficulty_mode = input_difficulty()
        secret_num = generate(difficulty)
        print(f"Game started\n-{difficulty_mode} Mode-")
        attempt = 1

        while True:
            try:
                print(f"📢Attempt {attempt}📢")
                user_input = int(input(f"Guess the number from 1-{difficulty}:\n>>> "))

                if user_input == secret_num:
                    print(f"\n🎊🎉Congratulations. You guessed the right number from 1-{difficulty} ({difficulty_mode} Mode) within {attempt} attempt🎉🎊")
                    best_attempt_for_mode = best_attempts.get(difficulty_mode, float('inf'))
                    if attempt < best_attempt_for_mode:
                        best_attempts[difficulty_mode] = attempt
                        print(f"🎉 New best attempt for {difficulty_mode} mode: {attempt} 🎉")
                    break

                elif user_input > difficulty or user_input < 1:
                    print(f"Please put a number not lower than 1 or higher than {difficulty}")

                elif user_input < secret_num:
                    print('Go higher⏫')
                    attempt += 1

                elif user_input > secret_num:
                    print('Go lower⏬')
                    attempt += 1

            except ValueError as e:
                print("Please put a number only😡")

        save_best_attempts_to_file(best_attempts)

        if play_again():
            display_stats()
            print('Thanks for playing❤')
            break
        else:
            print('Alright!😍\n')

if __name__ == "__main__":
    play()
