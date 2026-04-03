import eel
import hashlib
import os
import py7zr
import binascii
import rarfile
import time
import tkinter as tk
from tkinter import filedialog
from plyer import notification

# إعداد المجلد الخاص بالواجهة
eel.init('web')

def send_alert(pwd):
    notification.notify(
        title="Cyber Master Tool",
        message=f"Success! Password found: {pwd}",
        timeout=10
    )

@eel.expose
def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file_path = filedialog.askopenfilename()
    root.destroy()
    return file_path

@eel.expose
def process_request(file_path, mode, wordlist_path=None):
    if not os.path.exists(file_path):
        return "Error: File not found!"

    # --- وضع استخراج الهاش (Hash Analyze) ---
    if mode == 'extract':
        file_extension = os.path.splitext(file_path)[1].lower()
        try:
            if file_extension == ".7z":
                with open(file_path, "rb") as f:
                    header_data = f.read(32)
                    target_hash = binascii.hexlify(header_data).decode()
            elif file_extension == ".rar":
                with open(file_path, "rb") as f:
                    header_data = f.read(7)
                    target_hash = binascii.hexlify(header_data).decode()
            elif file_extension == ".zip":
                with open(file_path, "rb") as f:
                    header_data = f.read(4)
                    target_hash = binascii.hexlify(header_data).decode()
            else:
                with open(file_path, "rb") as f:
                    content = f.read()
                    target_hash = hashlib.md5(content).hexdigest()

            # حفظ الهاش على سطح المكتب كما في سكربتك الأصلي
            desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'hash.txt')
            with open(desktop_path, "w") as out:
                out.write(target_hash)
            
            return f"Captured: {target_hash[:20]}... (Saved to Desktop)"
        except Exception as e:
            return f"Error during extraction: {str(e)}"

    # --- وضع كسر التشفير (Integrity Test / Crack) ---
    elif mode == 'crack':
        if not wordlist_path or not os.path.exists(wordlist_path):
            return "Error: Valid Wordlist path is required!"
        
        file_ext = os.path.splitext(file_path)[1].lower()
        if file_ext == ".zip":
            return "ZIP support is currently in development."

        found = False
        try:
            with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as wordlist:
                for line in wordlist:
                    word = line.strip()
                    if not word: continue
                    
                    try:
                        if file_ext == ".7z":
                            with py7zr.SevenZipFile(file_path, mode='r', password=word) as archive:
                                archive.testzip()
                        elif file_ext == ".rar":
                            with rarfile.RarFile(file_path) as archive:
                                archive.testrar(password=word)
                        
                        found = True
                        send_alert(word)
                        return f"SUCCESS! Password found: {word}"
                    except:
                        continue
            
            if not found:
                return "Process Finished: Password not found in wordlist."
        except Exception as e:
            return f"Error during crack: {str(e)}"

    return "Unknown Mode"

if __name__ == '__main__':
    # تشغيل البرنامج
    eel.start('index.html', size=(900, 750))