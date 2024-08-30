
import itertools

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTER_VALUES = {
    'A': 1,
    'B': 3,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 4,
    'G': 2,
    'H': 4,
    'I': 1,
    'J': 8,
    'K': 5,
    'L': 1,
    'M': 3,
    'N': 1,
    'O': 1, 
    'P': 3,
    'Q': 10,
    'R': 1,
    'S': 1,
    'T': 1,
    'U': 1,
    'V': 4,
    'W': 4,
    'X': 8,
    'Y': 4,
    'Z': 10,
}

def display(word: str, hand: str):
    counts = {}
    for ch in hand:
        if ch not in counts:
            counts[ch] = 1
        else:
            counts[ch] += 1

    output = ''
    for ch in word:
        if ch not in counts:
           output += bcolors.OKGREEN + ch + bcolors.ENDC 
        else:
            counts[ch] -= 1
            if counts[ch] == 0:
                counts.pop(ch)

            output += ch

    if len(word) == 8:
        output = f'{bcolors.OKBLUE}[all 7 characters]{bcolors.ENDC} ' + output

    return output

def score(word):
    val = 0
    for ch in word:
        val += LETTER_VALUES[ch]

    return val

def main():
    word_list = []

    with open('words.txt') as f:
        word_list = f.read().split()

    words = set()
    for word in word_list:
        words.add(word)

    print('Input your 7 letter scrabble hand: \n> ', end='')
    hand = input()

    if len(hand) != 7:
        print('Not 7 letters. Aborting.')
        return
    
    hand = hand.upper()

    possible_moves = set()
    for i in range(1, len(hand) + 1):
        for subhand in itertools.combinations(hand, i):
            for ch in ALPHABET:
                guess_pool = list(subhand)
                guess_pool.append(ch)
                for guess in itertools.permutations(guess_pool):
                    guess = ''.join(guess)
                    if guess in words:
                        possible_moves.add((score(guess), guess))
                        
    possible_moves = list(possible_moves)
    possible_moves.sort(reverse=True)

    for (val, word) in possible_moves[:800]:
        print(f'{display(word, hand)} ({val} points)')
    
    print(f'{len(possible_moves)} moves found. Scores shown ignore modifiers, and each include exactly one external tile.')
    if len(possible_moves) > 800:
        print('Note: Only top 800 moves shown.')

if __name__ == '__main__':
    main()
