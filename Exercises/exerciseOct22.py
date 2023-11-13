# import crypt
# def testPass(cryptPass):
#     salt = cryptPass[0:2]

#     dictFile = open('dictionary.txt', 'r')
#     for word in dictFile.readlines():
#         word = word.strip('\n')
#         cryptWord = crypt.crypt(word.salt)
#         if (cryptWord  == cryptPass):
#             print ("[+] Foudn password: "+word+"\n")
#             return
#     print("[-] Password not found.\n")
#     return
# def main():
#     passFile = open("passwords.txt")
#     for line in passFile.readlines():
#         if ":" in line:
#             user = line.split(":")[0]
#             cryptPass = line.split(":")[1].strip('')
#             print("[*] Cracking Password for :  " + user)
#             testPass(cryptPass)
# if __name__ == "__main__":
#  main()

import hashlib

def testPass(cryptPass):
    salt = cryptPass[:2]
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        # Hash the dictionary word with the same salt as the password
        cryptWord = hashlib.sha256(salt.encode() + word.encode()).hexdigest()
        if cryptWord == cryptPass:
            print("[+] Found password: " + word + "\n")
            return
    print("[-] Password not found.\n")
    return

def main():
    passFile = open("passwords.txt")
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(":")[0]
            cryptPass = line.split(":")[1].strip('\n')
            print("[*] Cracking Password for :  " + user)
            testPass(cryptPass)

if __name__ == "__main__":
    main()
