x = input("File name: ").strip().lower()
def main():
    koncovka(x)


def koncovka(word):

    # checks if user entered a filename with a file extension
    if "." in word:

        # separates the file name and extension type
        name, extension = word.rsplit(".", 1)


        match extension:
            case "jpg" | "jpeg":
                print("image/jpeg" )
            case "gif" | "png":
                print("image/" + extension)
            case "pdf" | "zip":
                print("application/" + extension)
            case "txt":
                print("text/plain")
            case _:
                print("application/octet-stream")

    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()