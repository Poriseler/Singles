from math import ceil
def is_palindrome(word):
    length = len(word)
    half = ceil((length-1)/2)
    index = 0
    if length % 2 !=0:
        while index < half:
            if word[0+index] == word[(length-1)-index]:
                index +=1
            else:
                return False
        return True
    else:
        while index <= (half):
            if word[0 + index] == word[(length - 1) - index]:
                index +=1
            else:
                return False
        return True
word = input("just say a word ")
print(is_palindrome(word))