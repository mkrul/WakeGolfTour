import webbrowser
import os
import sys

from pkg_resources import working_set
from pkg_resources import Requirement

pkg_name = 'tcwgtsite'

site_path = working_set.find(Requirement.parse(pkg_name)).location + '\\WGT_Website\\'

command = 'python3 ' + site_path + 'manage.py runserver'
os.system(command)

url = 'http://localhost:8000/'
webbrowser.open(url)


