# 🛡️ Cyber Master Tool

**Advanced Security Analysis & Signature Extraction Tool**

---

## 🚀 Version History (Changelog)

### 🚀 v5.0 (Stable Release) - [Current Version]

- "We have successfully finalized the stable release, consolidating all
  development efforts into a single, high-performance standalone application (.EXE). This version ensures complete stability and a seamless user experience, free from any interface freezing thanks to our multi-threading implementation. Cyber Master v5.0 is now a production-ready tool, serving as a robust foundation for future advanced security features and AI-driven enhancements."

### 🧪 v5.0 (Beta Release) - [Current Development]

- Major Milestone: Transitioned from a command-line script to a Full GUI Application using the Eel framework (HTML/CSS/JS).

- New Architecture: Completely refactored the core logic into a modular structure, separating Python backend functions from the Web frontend.

- Modern Interface: Designed a sleek, responsive Dark Mode UI for a professional user experience.

- Interactive Features: Added a Modal Result System and dynamic status updates (no more messy console logs).

- Portability: Optimized the project for distribution by removing environment-specific folders and adding a universal requirements.txt.

- Improved Logic: Enhanced the signature extraction process to work seamlessly with the new graphical interface.

⚠️ Development Status
v5.0 is currently in Beta. We are actively testing the new GUI for stability and finalizing the integration of all legacy features into the new modular design.

### 🚀 v4.5 (Official Release) - [Current Stable]

- **New Feature**: Added **Auto-Resume** system. The tool now saves progress in `session.txt` and can resume from any line.
- **New Feature**: Integrated **Desktop Notifications**. Get a Windows alert immediately when a password is found.
- **Optimization**: Significant speed improvements for **RAR** and **7z** engines.
- **Stability Update**: **ZIP support removed** in this version to ensure 100% accuracy and prevent false positives.
- **UI Update**: Added real-time "Checked" counter and improved performance timer

## ⚠️ v4.5 Beta - Known Issue

- **ZIP Engine**: Currently using 7-Zip subprocess. Some encryption types may require further debugging.
- **Next Update**: Finalizing ZIP precision logic.

### 🚀 v4.0: The Multi-Format Engine (Latest)

- **New Feature**: Added full support for **RAR** archive cracking.
- **Library**: Integrated `rarfile` library for handling RAR password attempts.
- **Smart Logic**: Automatic detection of file extensions (.7z or .rar) to select the correct cracking engine.
- **UX Update**: Unified Stage 2 input to accept both 7z and RAR files seamlessly.

### T# 🛠 v3.5:he Brute-Force Awakening (Current)

- **New Feature**: Integrated 7z Archive Cracking Engine.
- **Library**: Powered by `py7zr` for high-speed signature matching.
- **Capability**: Can now test thousands of passwords from a `pass.txt` wordlist.
- **UX**: Added real-time "Checked" counter and color-coded results.

### **v3.0 (Current Version)**

- **Intelligent Logic:** Upgraded Stage 1 from basic hashing to **Binary Header Analysis**.
- **7z Support:** Specialized extraction of the first 32 bytes (Security Header) for encrypted archives.
- **Automation:** Automatic file path cleaning and instant export to `hash.txt` on the Desktop.
- **User Flow:** Added interactive prompts to bridge the gap between Stage 1 and Stage 2.

### **v2.0**

- Improved terminal UI with color coding.
- Added support for handling large files without crashing.
- Enhanced agent identification system.

### **v1.0**

- Initial release: Basic MD5 hash calculator for file integrity.

---

## 🛠️ How it works

1. Run the script.
2. Drag and drop your file (7z or any other format).
3. The tool captures the required signature and prepares it for cracking.
