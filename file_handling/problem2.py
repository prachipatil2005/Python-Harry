import random

def game():
    print("You are playing the game:")
    score = random.randint(1, 62)  # Generate a random score
    
    # Read the highscore from the file
    highscore_path = "D:\\c drive\\cs\\Sem6\\Python-harry\\file_handling\\file.txt"
    try:
        with open(highscore_path, "r") as f:
            highscore = f.read()
            if highscore.strip():  # Check if highscore is not empty
                highscore = int(highscore)
            else:
                highscore = 0
    except FileNotFoundError:
        highscore = 0  # If file doesn't exist, assume highscore is 0

    print(f"Your highscore: {highscore}")
    print(f"Your score: {score}")
    
    # Update highscore if the current score is greater
    if score > highscore:
        print("Congratulations! You have a new highscore!")
        with open(highscore_path, "w") as f:
            f.write(str(score))
    else:
        print("Better luck next time!")

    return score

game()
