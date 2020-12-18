# First and Last occurrence of a string

phrase = input("Please type a Phrase: ")

phrase_v1 = phrase.lower().strip()

print("The letter 'A' appears %s times in this phrase." % (phrase.count("a")))

print("The first time where the letter 'A' appears is on the position %s." % (phrase.find("a") + 1))

print("The last time where the letter 'A' appears is on the position %s." % (len(phrase_v1) - int((phrase_v1[::-1])
                                                                                                  .find("a"))))
