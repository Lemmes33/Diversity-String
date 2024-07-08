def solution(N):
    # Calculate the number of different letters that can be used
    num_letters = N // 26
    remaining = N % 26
    
    # Create a string with the maximum number of different letters
    letters = ''.join(chr(i) for i in range(97, 97 + num_letters))
    
    # Add the remaining letters
    if remaining > 0:
        letters += ''.join(chr(i) for i in range(97, 97 + remaining))
    
    # Repeat the letters to fill the string
    result = (letters * (N // len(letters) + 1))[:N]
    
    return result