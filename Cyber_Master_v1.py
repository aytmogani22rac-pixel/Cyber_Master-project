import hashlib


print("cyber Master v1.1")
agent_name = input("Enter Agent Name:")
print(f"Access Granted, Agent {agent_name}")
print("1. Extract Hash | 2. Crack/Analyze Hash")
choice = input("Select Stage (1 or 2):")
if choice == "2":
    user_hash = input( "Paste the hash to crack: ")
    hash_length = len(user_hash)
    print(f"The length of this hash is: {hash_length}")
    print(f"Cracking Hash: {user_hash} ...")
    with open("pass.txt", "r") as wordlist:
     counter = 0
     for line in wordlist:
        word = line.strip()
        counter += 1
        print(f"[*] Checked: {counter} | Trying: {word}          ", end="\r")
        hashed_word = hashlib.md5(word.encode()).hexdigest()
        if hashed_word == user_hash:
            print(f"[+] Success! Password found: {word}")
            break
