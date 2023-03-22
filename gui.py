import tkinter as tk
from tkinter import filedialog

# tkinter root 생성
root = tk.Tk()
root.withdraw()

# 파일 선택 dialog 생성
file_path = filedialog.askopenfilename()

# 선택한 파일 경로 출력
print(file_path)

root = tk.Tk()
root.withdraw()

