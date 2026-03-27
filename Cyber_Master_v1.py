import hashlib
import os
import py7zr
import binascii
import rarfile
import subprocess
import time

# تعريف الألوان ليعمل الكود بدون أخطاء
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

print(f"{GREEN}Cyber Master v4.5 - The Multi-Format Engine{RESET}")
agent_name = input("Enter Agent Name: ")
print(f"Welcome back, Agent {agent_name}. Standing by for instruction...")
print("\n[1] Extract File Signature (7z, RAR, ZIP, MD5)")
print("[2] Crack Archive - Wordlist Mode (7z, RAR, ZIP)")
choice = input("\nSelect Stage: ")

# --- Stage 1: Extraction ---
if choice == "1":
    file_path = input("\n[?] Drag and drop the file here: ").strip().replace('"', '')
    if not os.path.exists(file_path):
        print("[-] Error: File not found!")
        exit()

    file_extension = os.path.splitext(file_path)[1].lower()
    print(f"[*] File type detected: {file_extension}")
    
    if file_extension == ".7z":
        with open(file_path, "rb") as f:
            header_data = f.read(32)
            target_hash = binascii.hexlify(header_data).decode()
            print(f"\n[+] Security Header Captured (7z): {target_hash}") 
    elif file_extension == ".rar":
        with open(file_path, "rb") as f:
            header_data = f.read(7)
            target_hash = binascii.hexlify(header_data).decode()
            print(f"\n[+] Security Header (RAR): {target_hash}")   
    if file_extension == ".zip" :
        with open(file_path, "rb") as f:
            header_data = f.read(4) 
            target_hash = binascii.hexlify(header_data).decode()
            print(f"\n[+] Security Header (ZIP): {target_hash}")                     
    else:
        with open(file_path, "rb") as f:
            content = f.read()
            target_hash = hashlib.md5(content).hexdigest()
            print(f"\n[+] MD5 Hash (Full File): {target_hash}")

    # حفظ الهاش على سطح المكتب
    desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'hash.txt')
    with open(desktop_path, "w") as out:
        out.write(target_hash)
    print(f"[+] Done! Hash saved to Desktop as hash.txt") 

    go_next = input("\n[?] Do you want to proceed to Stage 2 (Cracking)? (y/n): ")      
    if go_next.lower() == 'y':
        print(f"\n{YELLOW}[*] Switching to Stage 2...{RESET}")
        choice = "2" # تحويل الاختيار ليدخل في المرحلة التالية مباشرة
    else:
        print(f"\n{GREEN}[+] Agent {agent_name}, mission completed. Goodbye!{RESET}")
        exit()

# --- Stage 2: Cracking --- 
if choice == "2":
    target_file = input("\nEnter the path of the archive to crack (7z/ RAR/ ZIP): ").strip().replace('"', '').replace("'", "")
    wordlist_path = "pass.txt" 
    if not os.path.exists(target_file):
        print("[-] Error: Target file not found!")
    elif not os.path.exists(wordlist_path):
        print(f"[-] Error: '{wordlist_path}' not found! Create it in the project folder.")
    else:
        print(f"\n{YELLOW}[!] Starting Brute-force on: {os.path.basename(target_file)}{RESET}")
        
        try:
            with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as wordlist:
                counter = 0
                found = False
                start_time = time.time()
                for line in wordlist:
                    word = line.strip()
                    if not word: continue
                    counter += 1
                    print(f"[*] Checked: {counter} | Trying: {word}            ", end="\r")
                    try:
                        file_ext = os.path.splitext(target_file)[1].lower()
                        if file_ext == ".7z":
                            with py7zr.SevenZipFile(target_file,mode='r', password=word) as archive: 
                                archive.testzip()
                        elif file_ext == ".rar":
                            with rarfile.RarFile(target_file) as archive: 
                                archive.testrar(password=word)
                        elif file_ext == ".zip" :
                            seven_zip = r"C\Program Files\7-Zip\7z.exe"
                            cmd = [seven_zip, "t", target_file, f"-p{word}", "-y"]
                            result = subprocess.run(cmd, capture_output=True, text=True)
                            if result.returncode != 0:
                                raise Exception("Wrong")
                        print(f"\n\n{GREEN}[+] Success! Password found: {word}{RESET}")
                        end_time = time.time()
                        duration = round(end_time - start_time, 2)
                        print(f"{YELLOW}[*] Time taken: {duration} seconds{RESET}")
                        found = True
                        break
                    except:
                        continue

                if not found:
                    print(f"\n\n{YELLOW}[-] Password not found in the wordlist.{RESET}")
        except Exception as e:
            print(f"\n[-] An error occurred: {e}")