def main():
    summarize()

slist = {}

def summarize():
    while True:
        try:
            n = input()
            if n in slist:
                q += 1   #change value of n by 1
            else:
                q = 1
            slist[n] = q
        except EOFError:
                # sorts the dict alphabetically and prints the list
            for item, quantity in sorted(slist.items()):
                print(quantity, item.upper())
            break
        except KeyError:
            pass



main()