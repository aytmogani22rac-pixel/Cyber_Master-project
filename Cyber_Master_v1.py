import hashlib
import re 
import os
import sys
import py7zr
import binascii


print("Cyber Master v3.0 - Binary Hunter Mode")
agent_name = input("Enter Agent Name:")
print(f"Welcome back, Agent {agent_name}. Standing by for instruction...")
print("\n[1] Extract File Signature(7z, ZIP, MD5)")
print("[2] Crack / Match Signatures (Future Stage)")
choice = input("\nSelect Stage: ")
# --- Stage 1: Cracking ---
if choice == "1":
    file_path = input("\n[?] Drag and drop the file here: ")
    file_path = file_path.strip().replace('"', ' ')
    file_extension = os.path.splitext(file_path)[1].lower()
    print(f"[*] File type detected: {file_extension}")
    if file_extension == ".7z":
                with open(file_path, "rb") as f:
                       header_data = f.read(32)
                       target_hash = binascii.hexlify(header_data).decode()
                       print(f"\n[+] Security Header Captured: {target_hash}")                   
    else:
        with open(file_path, "rb") as f:
            content = f.read()
            target_hash = hashlib.md5(content).hexdigest()
            print(f"\n[+] MD5 Hash (Full File):{target_hash} ")
      # هذا السطر يجد سطح المكتب تلقائياً في أي جهاز ويندوز
    desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'hash.txt')
    with open(desktop_path, "w") as out:
        out.write(target_hash)
    print(f"[+] Done! Hash saved to your Desktop as hash.txt") 
    go_next = input("\n[?] Success! Do ypu want to proceed to Stage 2 (Cracking)? (y/n): ")     
    if go_next.lower() == 'y':
          print(f"\n{YELLOW}[*] Switching to Stage 2...{RESET}")
          PRINT(F"[*] Signature Loaded: {target_hash}")
    else:
          print(f"\n{GREEN}[+] Agent {agent_name}, mission completed.Goodbye!{RESET}")
# --- Stage 2: Cracking --- 
if choice == "2":
            user_hash = input( "Paste the hash to crack: ").strip().lower()
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
                    if hashed_word == user_hash.strip():
                        print(f"\n[+] Success! Password found: {word}")
                        break
                else:
                    print("\n[-] Password not found in the wordlist.")