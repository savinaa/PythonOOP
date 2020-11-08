def palindrome(word,index):
    if index>len(word)/2:
        result=format(f'{word} is a palindrome')
        return result
    if word[index]==word[len(word)-1-index]:
        return palindrome(word,index+1)
    else:
        return f'{word} is not a palindrome'



print(palindrome("abca", 0))
