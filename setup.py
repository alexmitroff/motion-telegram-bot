from setuptools import setup, find_packages

setup(
   name='motion-telegram-bot',
   version='1.4',
   description='Simplified telegram bot',
   author='Aleksei Mitrofanov',
   author_email='alexmitroff@gmail.com',
   packages=find_packages(),
   install_requires=['python-telegram-bot'],
   entry_points={
       'console_scripts': [
           'send-doc = commands.send_doc:send_doc',
           'send-image = commands.send_image:send_image',
           'send-message = commands.send_message:send_message',
           'send-video = commands.send_video:send_video',
           'send-video-preview = commands.send_video_preview:send_video_preview',
           'send-validated-video-preview = commands.send_validated_video_preview:send_validated_video_preview',
       ]
   },
)
