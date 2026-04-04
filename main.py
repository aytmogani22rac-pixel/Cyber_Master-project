import eel
import os
import sys
import py7zr
import rarfile
import threading
import tkinter as tk
from tkinter import filedialog
from plyer import notification

# --- إعدادات المسارات للتحويل إلى EXE ---
def get_resource_path(relative_path):
    """ الحصول على المسار المطلق للموارد، يعمل في التطوير وفي الـ EXE """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# إعداد المجلد الخاص بالواجهة
eel.init(get_resource_path('web'))

# إخبار المكتبة بمكان أداة unrar.exe (يجب أن تضع الملف بجانب السكربت)
rarfile.UNRAR_TOOL = get_resource_path("unrar.exe")

def send_alert(pwd):
    try:
        notification.notify(
            title="Cyber Master v5.0",
            message=f"Success! Password found: {pwd}",
            timeout=10
        )
    except:
        pass

@eel.expose
def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file_path = filedialog.askopenfilename()
    root.destroy()
    return file_path

def start_cracking_logic(file_path, wordlist_path):
    """ المنطق الداخلي للكسر يعمل في Thread منفصل لعدم تجميد الواجهة """
    file_ext = os.path.splitext(file_path)[1].lower()
    found = False
    
    try:
        # استخدام encoding utf-8 لضمان قراءة ملفات الباسوردات العربية أو الخاصة
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
                    
                    # في حال النجاح
                    found = True
                    send_alert(word)
                    eel.on_crack_result(f"SUCCESS! Password: {word}") # إرسال النتيجة للواجهة
                    return
                except:
                    continue
        
        if not found:
            eel.on_crack_result("Finished: Password not found.")
            
    except Exception as e:
        eel.on_crack_result(f"Error: {str(e)}")

@eel.expose
def process_request(file_path, mode, wordlist_path=None):
    if not os.path.exists(file_path):
        return "Error: File not found!"

    # وضع الاستخراج (لا يحتاج Threading لأنه سريع)
    if mode == 'extract':
        import binascii
        file_extension = os.path.splitext(file_path)[1].lower()
        try:
            with open(file_path, "rb") as f:
                if file_extension == ".7z":
                    header = f.read(32)
                else:
                    header = f.read(7)
                target_hash = binascii.hexlify(header).decode()
            return f"Signature: {target_hash}"
        except Exception as e:
            return f"Extraction Error: {str(e)}"

    # وضع الكسر (يحتاج Threading لضمان سلاسة الواجهة)
    elif mode == 'crack':
        if not wordlist_path or not os.path.exists(wordlist_path):
            return "Error: Wordlist required!"
        
        # تشغيل الكسر في خلفية البرنامج
        thread = threading.Thread(target=start_cracking_logic, args=(file_path, wordlist_path))
        thread.daemon = True
        thread.start()
        return "Cracking started... please wait."

    return "Unknown Mode"

if __name__ == '__main__':
    # تشغيل Eel مع مراعاة حجم الشاشة التي تفضلها على T480
    try:
        eel.start('index.html', size=(900, 750))
    except (SystemExit, KeyboardInterrupt):
        pass