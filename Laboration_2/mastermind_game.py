from mastermind_funcs import generate_code
from mastermind_funcs import right_position
from mastermind_funcs import wrong_position

def mastermind_game():
    """Funktionen för mastermind spelet"""
    code = generate_code()
    turn = 0
    while turn < 7:
        turn += 1
        guess = []
        print(f"--------- round {turn} ----------")
        for item in range(0,4):
            a_guess = int(input(f"Guess number {item+1}: "))
            guess.append(a_guess)
        right = right_position(guess,code)
        wrong = wrong_position(guess,code)
        if right == 4:
            text = f"\nCongrats, you win after {turn} try!"
            return True, text
        right = "\033[31m *\033[37m"*right
        wrong = "\033[33m *\033[37m"*wrong
        print(right+wrong)
    text = f"\nRight answer is {code}.\n\tTry agin!\n"
    return False, text

def main():
    """Huvud funktionen"""
    result,text = mastermind_game()
    if result:
        print(text)
    else:
        print(text)

if __name__  ==  "__main__" :
    main()
