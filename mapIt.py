import webbrowser
import requests
import pyperclip
import sys


if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()


# 美国 新冠肺炎 感染 总人数
webbrowser.open("https://www.baidu.com/s?wd=" + address)