
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic Hangman word-guessing game to practice Python strings, loops, conditionals, and user interaction.

## 📝 Tasks

### 🛠️ Word Selection and Game Setup

#### Description
Create a list of possible secret words and set up the initial game state before gameplay begins.

#### Requirements
Completed program should:

- Use a predefined list of words.
- Randomly select one secret word using `random.choice()`.
- Initialize variables for guessed letters, remaining attempts, and the current display state.

### 🛠️ Letter Guessing and Progress Display

#### Description
Accept player guesses, update the word display with correctly guessed letters, and show the remaining attempts.

#### Requirements
Completed program should:

- Prompt the player for a letter guess.
- Reveal correctly guessed letters in the hidden word display.
- Maintain blanks for letters not yet guessed.
- Show how many incorrect attempts remain.

### 🛠️ Win/Lose Logic and Feedback

#### Description
End the game when the player either guesses the full word or uses all attempts, then display the appropriate message.

#### Requirements
Completed program should:

- Detect when the player has guessed all letters correctly.
- Detect when the player has exhausted all allowed attempts.
- Print a win message when the word is guessed.
- Print a loss message and reveal the secret word when the player runs out of attempts.
