# Diversity-String
Problem Statement
Write a function solution that, given an integer N, returns a string of length N containing as many different lower-case letters ('a'-'z') as possible, in which each letter occurs an equal number of times.

Examples
Given N = 3, the function may return "fig", "pea", "nut", etc. Each of these strings contains three different letters with the same number of occurrences.
Given N = 5, the function may return "mango", "grape", "melon", etc.
Given N = 30, the function may return "aabbcc...oo" (each letter from 'a' to 'o' occurs twice). The string contains 15 different letters.
Assumptions
N is an integer within the range [1..200,000].
Solution
Here is the Python solution:

python
Edit
Copy code
def solution(N):
    """
    Returns a string of length N containing as many different lower-case letters ('a'-'z') as possible,
    in which each letter occurs an equal number of times.

    :param N: integer within the range [1..200,000]
    :return: string of length N
    """
    alphabet_size = 26
    num_letters = N // alphabet_size
    remaining_letters = N % alphabet_size

    result = ''
    for i in range(alphabet_size):
        result += chr(ord('a') + i) * num_letters
        if i < remaining_letters:
            result += chr(ord('a') + i)

    return result
Explanation
The solution works by first calculating the number of times each letter will appear in the result string (num_letters). Then, it calculates the remaining letters that need to be added to the string (remaining_letters).

The result string is built by iterating over the alphabet and adding each letter num_letters times. If there are remaining letters, they are added to the string as well.

Time Complexity
The time complexity of this solution is O(1), since the number of operations is constant and does not depend on the input size N.

Space Complexity
The space complexity of this solution is O(N), since the result string has a length of N.