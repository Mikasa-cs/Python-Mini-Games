import random
def check_move_validity(move):
    moves = ['rock', 'paper', 'scissors']
    return move.lower() in moves
def determine_winner(user_move, computer_move):
    if user_move == computer_move:
        return "It's a tie!"
    user_move = user_move.lower()
    computer_move = computer_move.lower()
    if (user_move == 'rock' and computer_move == 'scissors') or \
       (user_move == 'scissors' and computer_move == 'paper') or \
       (user_move == 'paper' and computer_move == 'rock'):
        return "You win!"
    else:
        return "You lose."
def get_user_move():
    move = input("Enter your move (rock, paper, or scissors): ")
    while not check_move_validity(move):
        move = input("Invalid move. Enter your move (rock, paper, or scissors): ")
    return move
def get_computer_move():
    moves = ['rock', 'paper', 'scissors']
    return random.choice(moves)
def play_game():
    user_move = get_user_move()
    computer_move = get_computer_move()
    print(f"You choose {user_move}, the computer choose {computer_move}.")
    print(determine_winner(user_move, computer_move))
if __name__ == "__main__":
    play_game()