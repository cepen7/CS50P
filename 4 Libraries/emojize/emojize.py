from emoji import emojize

fromUser = input("Input: ")
toUser = emojize(fromUser, language="alias")

print(f"Output: {toUser}")
