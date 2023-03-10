#!/usr/bin/python3
'''Prime Game'''


def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Generate a set of all numbers from 2 to n
        remaining_numbers = set(range(2, n+1))

        # Keep track of who's turn it is
        maria_turn = True

        # Play the game until there are no primes left
        while True:
            # Find the next prime number in the set
            prime = None
            for num in remaining_numbers:
                if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
                    prime = num
                    break

            # If there are no more primes, the current player loses
            if prime is None:
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            # Remove the prime and its multiples from the set
            for i in range(prime, n+1, prime):
                remaining_numbers.discard(i)

            # Switch turns
            maria_turn = not maria_turn

    # Determine the winner based on who won the most rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
