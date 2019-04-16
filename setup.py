from setuptools import setup, find_packages

setup (
    name='WakeGolfTour',
    version='1.1',
    author='misha krul',
    author_email='mkrul@my.waketech.edu',
    url='https://waketech.edu',
    description='WakeGolfTour Project',
    long_description='Wake Golf Tour Project - CSC122 Python Applications',
    long_description_content_type='text/plain',
    packages=find_packages(),
    package_data = {
       '': ['WakeGolfTour.db', 'templates/*',
       'golf_course/templates/golf_course/*',
       'golf_course/static/golf_course/*',
       'golfer/templates/golfer/*',
       'golfer/static/golfer/*',
       'golfer_polls/templates/golfer_polls/*',
       'golfer_polls/static/golfer_polls/*',
       'tournament/templates/tournament/*',
       'tournament/static/tournament/*'],
   },
   scripts=['runWGT.py'],
)
