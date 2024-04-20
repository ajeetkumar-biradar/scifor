# Aarush and Yash are two friends in the same grade and they decided to create their secret language to communicate with each other. First of all, they decided to reverse each word. For example: come here = "emoc ereh". But this was very easy to understand for other students. They tried to make it a bit difficult and decided to put all the characters which are at odd indices first then all the characters which are at even indices. For example: come here = "oecm eehr". Write a program in python to create such type of secret language and convert the word Codeyoung into secret language using the same program. Can we convert the secret language back to normal language using python? Discuss
def create_secret_language(word):
    reversed_word = word[::-1]

    odd_chars = reversed_word[1::2]
    even_chars = reversed_word[::2]

    secret_language = odd_chars + even_chars

    return secret_language


word = input("Enter a word to convert to secret language: ")

secret_language = create_secret_language(word)

print("Secret language:", secret_language)
