import sys
import clipboard

#from automate the boring stuff - copy and pasting passwords. Obviously insecure, but good practice
#modified a little bit as well

PASSWORDS = {'email': 'lovegmail12!',
             'facebook': 'lovemeta2211!',
             'safe': "1234"}


def main():
    if len(sys.argv) < 2:
        print("Usage: pw.py [account] - copy account password")
        sys.exit()
    
    account = sys.argv[1]
    if account in PASSWORDS:
        clipboard.copy(PASSWORDS[account])
        print(f"Password for {account} copied to clipboard")
    else:
        print(f"{account} not in PASSWORDS.")
        sys.exit()

if __name__=="__main__":
    main()