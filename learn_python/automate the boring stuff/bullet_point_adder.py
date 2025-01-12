import clipboard

#from automate the boring stuff - gets whatever is on your clipboard and adds a bunch of asterisks to it

def main():
    #get what is on the clipboard
    data = clipboard.paste()
    result = ""

    #split data into a list based on newline, strip out any whitespaces
    list_data = data.strip().split('\n')

    for i in range(0, len(list_data)):
        if i == len(list_data) - 1:
            result += "*" + " " + list_data[i]
        else:
            result += "*" + " " + list_data[i] + '\n'
    
    #copy result to clipboard
    print(result)
    clipboard.copy(result)
    print("------------------------")
    print("Modifed string copied to clipboard")
    print("------------------------")


if __name__=="__main__":
    main()