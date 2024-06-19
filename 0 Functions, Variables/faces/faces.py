def main():
    text = input(str())
    print(convert(text))

# replaces the emoticon by an emoji
def convert(greeting):
    return(greeting.replace(":)","🙂").replace(":(","🙁"))

main()