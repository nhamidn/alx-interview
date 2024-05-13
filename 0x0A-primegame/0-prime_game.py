#!/usr/bin/python3
"""Prime game Module"""


class PrimeCache:
    def __init__(self):
        self.primes = []
        self.max_checked = 1

    def update_primes(self, end):
        """Update the list of primes up to the end if not already done."""
        if end > self.max_checked:
            for num in range(max(2, self.max_checked + 1), end + 1):
                if all(num % p != 0 for p in self.primes if p * p <= num):
                    self.primes.append(num)
            self.max_checked = end

    def get_prime_count(self, n):
        """Return the number of primes up to n."""
        self.update_primes(n)
        return sum(1 for p in self.primes if p <= n)


def isWinner(x, nums):
    """Function that solves the prime game problem."""
    prime_cache = PrimeCache()
    maria_wins = 0
    ben_wins = 0

    for n in range(x):
        prime_count = prime_cache.get_prime_count(nums[n])

        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
