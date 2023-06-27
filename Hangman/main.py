import curses
import random

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.addstr(0, 0, "Welcome to Hangman!")
    
    # Load word list
    with open("wordlist.txt") as f:
        words = f.read().splitlines()
    
    # Select a random word
    word = random.choice(words).upper()
    word_len = len(word)
    revealed = ["_" for _ in range(word_len)]
    guesses = set()
    max_guesses = 6
    num_guesses = 0
    
    # Draw initial state
    draw_hangman(stdscr, num_guesses)
    draw_word(stdscr, revealed)
    
    # Game loop
    while True:
        # Get user input
        key = stdscr.getch()
        if key != -1:
            letter = chr(key).upper()
            if letter.isalpha() and letter not in guesses:
                guesses.add(letter)
                if letter in word:
                    for i, c in enumerate(word):
                        if c == letter:
                            revealed[i] = letter
                    if "_" not in revealed:
                        stdscr.addstr(word_len + 2, 0, "You win!")
                        stdscr.refresh()
                        stdscr.getch()
                        break
                else:
                    num_guesses += 1
                    if num_guesses >= max_guesses:
                        stdscr.addstr(word_len + 2, 0, "You lose! The word was {}.".format(word))
                        stdscr.refresh()
                        stdscr.getch()
                        break
        
        # Draw updated state
        stdscr.erase()
        draw_hangman(stdscr, num_guesses)
        draw_word(stdscr, revealed)
        draw_guesses(stdscr, guesses)
        stdscr.refresh()
    
    # Clean up curses
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

def draw_hangman(stdscr, num_guesses):
    hangman = [
        " ____",
        " |  |",
        " |  {}",
        " | {}{}{}".format("/" if num_guesses >= 1 else "", "|" if num_guesses >= 2 else "", "\\" if num_guesses >= 3 else ""),
        " | {} {}".format("/" if num_guesses >= 4 else "", "\\" if num_guesses >= 5 else ""),
        "_|_",
    ]
    for i, line in enumerate(hangman):
        stdscr.addstr(i + 2, 0, line)

def draw_word(stdscr, revealed):
    stdscr.addstr(8, 0, " ".join(revealed))

def draw_guesses(stdscr, guesses):
    stdscr.addstr(10, 0, "Guesses: " + ", ".join(sorted(guesses)))

if __name__ == "__main__":
    curses.wrapper(main)
