import random
import time
secret_number = random.randint(1, 100)
guesses = 0
max_guesses = 10
low = 1
high = 100
play_again = "yes"
while play_again.lower()== "yes":
        secret_number =random.randint(1, 100)
        guesses = 0
        max_guesses =10
        low =1
        high = 10
        start_time = time.time()
        level = int(input("choose level (1:easy, 2 : meduium, 3: hard): "))
        if level == 1:
                max_guesses = 15
                range_max = 50
        elif level == 2:
                max_guesses = 10
                range_max = 100
        else:
                max_guesses =  5
                range_max = 200
        secret_number =random.randint(1, range_max)
        hint_count = 3
        while guesses < max_guesses and time.time()-start_time <60 and hint_count>0:
                if input("want a hint?(yes/no)").lower()=="yes":
                        hint = (low + high) // 2
                        print(f"hint: Try around {hint}")
                        hint_count -= 1
                        guesses += 1
                else:
                        guess = int(input(f"guess a number({low}-{high}): "))
                        guess +=1
                        if guess == secret_number:
                                score = 1000 - (guesses*100)
                                if score<0:
                                        score=0
                                print(f"Awsome! you got it in {guesses} guesses! your score:")
                                break
                        elif guess < secret_number:
                                print("too low! Try again.")
                                low =guess +1
                        else : 
                                print("too high! Try again")
                                high = guess -1
                        if guesses == max_guesses:
                                print(f" Game over! the number was {secret_number}.")
                        if time.time() - start_time >= 60:
                                print(f"time's up! the number was {secret_number}")
                                break
                print("=== welcome to number guessing game ===")
# https://youtu.be/XX44XYjK_JQ?t=3513
"""Skip to content
Chat history


You said:
explain import random
import time
secret_number = random.randint(1, 100)
guesses = 0
max_guesses = 10
low = 1
high = 100
play_again = "yes"
while play_again.lower()== "yes":
        secret_number =random.randint(1, 100)
        guesses = 0
        max_guesses =10
        low =1
        high = 10
        start_time = time.time()
        level = int(input("choose level (1:easy, 2 : meduium, 3: hard): "))
        if level == 1:
                max_guesses = 15
                range_max = 50
        elif level == 2:
                max_guesses = 10
                range_max = 100
        else:
                max_guesses =  5
                range_max = 200
        secret_number =random.randint(1, range_max)
        hint_count = 3
        while guesses < max_guesses and time.time()-start_time <60 and hint_count>0:
                if input("want a hint?(yes/no)").lower()=="yes":
                        hint = (low + high) // 2
                        print(f"hint: Try around {hint}")
                        hint_count -= 1
                        guesses += 1
                else:
                        guess = int(input(f"guess a number({low}-{high}): "))
                        guess +=1
                        if guess == secret_number:
                                score = 1000 - (guesses*100)
                                if score<0:
                                        score=0
                                print(f"Awsome! you got it in {guesses} guesses! your score:")
                                break
                        elif guess < secret_number:
                                print("too low! Try again.")
                                low =guess +1
                        else : 
                                print("too high! Try again")
                                high = guess -1
                        if guesses == max_guesses:
                                print(f" Game over! the number was {secret_number}.")
                        if time.time() - start_time >= 60:
                                print(f"time's up! the number was {secret_number}")
                                break
                print("=== welcome to number guessing game ===")
# https://youtu.be/XX44XYjK_JQ?t=3513


ChatGPT said:
Alright Mike, grab a coffee — let’s walk through this thing together. I’ll keep it friendly but clear, like we’re looking over your shoulder while you’re coding.

🚀 What this program is
It’s a “guess the number” game with:

Difficulty levels

Time limit (60 seconds)

Limited guesses

Optional hints

Scoring system
Replay loop
Pretty cool — just a few logic issues, but we’ll get 
to that.
🧩 Line-by-line explanation (in simple words)
📦 Imports
import random
import time
random → so you can generate random numbers.
time → so you can measure how long the player is taking.
🎯 Initial setup
secret_number = random.randint(1, 100)
guesses = 0
max_guesses = 10
low = 1
high = 100
play_again = "yes"
You’re defining default starting values before the game 
loop.

🔁 Main loop: play again?
while play_again.lower() == "yes":
The game restarts as long as the player types "yes".

Inside the loop, you reset the game:

secret_number = random.randint(1, 100)
guesses = 0
max_guesses = 10
low = 1
high = 10   # <-- tiny mistake (should be 100 maybe?)
start_time = time.time()
start_time tracks when the countdown begins.

🏷️ Difficulty levels
level = int(input("choose level..."))
The player picks difficulty:

if level == 1:
    max_guesses = 15
    range_max = 50
elif level == 2:
    max_guesses = 10
    range_max = 100
else:
    max_guesses = 5
    range_max = 200
Then you generate a new secret number within that 
difficulty:

secret_number = random.randint(1, range_max)
Nice.

💡 Hints setup
hint_count = 3
Player gets up to 3 hints per game.

🎮 Guessing loop
This is the core gameplay:

while guesses < max_guesses and time.time()-start_time < 60 and hint_count > 0:
This continues as long as:

Not too many guesses

Time not exceeded

Still have hints

🔍 If player asks for a hint
if input("want a hint?").lower() == "yes":
    hint = (low + high) // 2
    print(f"hint: Try around {hint}")
    hint_count -= 1
    guesses += 1
Your hint is basically: midpoint between low and high.

🔢 If player wants to guess
else:
    guess = int(input(f"guess a number({low}-{high}): "))
    guess += 1    # <-- BIG mistake: this changes the guess!
⚠️ Here is a bug →
guess += 1 increases the guess incorrectly.

If they enter “50”, your code turns it into 51.

Probably meant:
guesses += 1
Right now you’re incrementing the wrong variable.
⚖️ Check the guess
if guess == secret_number:
    score = 1000 - (guesses * 100)
Score starts at 1000 and drops by 100 per guess.
If they guessed right → you stop the loop.
🔼 Too low
elif guess < secret_number:
    print("too low!")
    low = guess + 1
Updates the lower bound.

🔽 Too high
else:
    print("too high!")
    high = guess - 1
Updates the upper bound.

⏱️ Time or guesses end
if guesses == max_guesses:
    print("Game over!")
if time.time() - start_time >= 60:
    print("time's up!")
❓ Debug message
print("=== welcome to number guessing game ===")
This randomly prints inside the loop — looks like it was meant to be at the top of the program.

🔥 Summary of the key issues in your code
Here’s the stuff you probably want to fix:

1️⃣ high = 10 at the start
Probably meant high = 100.

2️⃣ You increase the player's guess, not guesses counter
guess += 1   # ❌ wrong
Should be:

guesses += 1   # ✔️ correct
3️⃣ Your while-loop condition uses hint_count > 0
If hints drop to 0, the player can't guess anymore.
Probably not intended.

If you want, I can rewrite this whole game in a clean, tidy, bug-free version that works perfectly.

Wanna do that?




No file chosenNo file chosen
ChatGPT can make mistakes. Check important info.
"""



