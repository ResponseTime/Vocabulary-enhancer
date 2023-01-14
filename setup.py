import os
import shutil
if __name__ == '__main__':
    if not os.path.isfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\main.py"):
        shutil.copy2(
            "C:\\Users\\callr\\Vocabulary Enhancer\\main.py", "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
        shutil.copy2(
            "C:\\Users\\callr\\Vocabulary Enhancer\\.env", "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup")
    else:
        print("Setup already done")
