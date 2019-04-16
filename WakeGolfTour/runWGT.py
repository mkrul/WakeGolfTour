import webbrowser
import os
import sys

arg = ''
if len(sys.argv) >= 2:
    arg = sys.argv[1]

url = 'http://localhost:8000/' + arg
webbrowser.open(url)

command = 'python3 manage.py runserver'
os.system(command)


