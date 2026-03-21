import hashlib
import re 
import os


print("cyber Master v1.1")
agent_name = input("Enter Agent Name:")
print(f"Access Granted, Agent {agent_name}")
print("1. Extract Hash | 2. Crack/Analyze Hash")
choice = input("Select Stage (1 or 2):")
# --- Stage 1: Cracking ---
if choice == "1":
    file_path = input("[?] Drag and drop the file here: ").strip('"')
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        found_hashes = re.findall(r'[a-f0-9]{32}', content.lower())    
        if found_hashes:
            print(f"\n[+] Found {len(found_hashes)} hash(es) in the file.")
            target_hash = found_hashes[0]
            print(f"[!] Target hash: {target_hash}")
            ask_save = input("[?] Save hash to Desktop? (y/n): ").lower()
            if ask_save == 'y':
# هذا السطر يجد سطح المكتب تلقائياً في أي جهاز ويندوز
                desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'hash.txt')
                with open(desktop_path, "w") as out:
                    out.write(target_hash)
                print(f"[+] Done! Hash saved to your Desktop as hash.txt")
            else:
                print(f"[!] Hash was NOT saved. Just copy it: {target_hash}")
        else:
            print("[-] No MD5 hashes found in this file.")
# --- Stage 2: Cracking --- 
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
                print(f"[*] Checked: {counter} | Trying: {word}            ", end="\r")
                hashed_word = hashlib.md5(word.encode()).hexdigest()
                if hashed_word == user_hash:
                    print(f"[+] Success! Password found: {word}")
                break
            else:
                print("\n[-] Password not found in the wordlist.")