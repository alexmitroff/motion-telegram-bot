from setuptools import setup, find_packages

setup(
   name='pogost-telegram-bot',
   version='0.1',
   description='Simplified telegram bot',
   author='Aleksei Mitrofanov',
   author_email='alexmitroff@gmail.com',
   packages=find_packages(),
   install_requires=['python-telegram-bot'],
   entry_points={
       'console_scripts': [
           'send-image = commands.send_image:send_image',
           'send-video = commands.send_video:send_video',
       ]
   },
)