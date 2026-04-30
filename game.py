"""A tiny terminal number-guessing game.

Run:
    python3 game.py
"""

from __future__ import annotations

import random


def play() -> None:
    print("Welcome to the Small Game!")
    print("I'm thinking of a number between 1 and 20.")

    secret = random.randint(1, 20)
    attempts = 0
    max_attempts = 6

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        guess_text = input(f"Enter your guess ({remaining} attempt(s) left): ").strip()

        if not guess_text.isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(guess_text)
        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Nice! You guessed it in {attempts} attempt(s).")
            return

    print(f"Game over! The number was {secret}.")


if __name__ == "__main__":
    play()
