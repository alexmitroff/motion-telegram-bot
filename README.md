# Motion Telegram bot

Simple telegram bot wrapper for sending images and video to chosen chat. Created to work with Motion output.
Powered by [python telegram bot](https://github.com/python-telegram-bot/python-telegram-bot).


## Commands
### motion-telegram-bot.send-image
Simply sends an image if it exists.
```bash
motion-telegram-bot.send-image -f /home/user/test_image.jpg -b $BOT_AUTH -c $CHANNEL_ID
```
### motion-telegram-bot.send-video
Simply sends a video if it exists. (h264 | mp4 / mov) < 50Mb
```bash
motion-telegram-bot.send-video -f /home/user/test_video.mov -b $BOT_AUTH -c $CHANNEL_ID
```
### motion-telegram-bot.send-video-preview
Sends a video preview image if it exists.
```bash
# video:   /home/user/test_video.mp4
# preview: /home/user/test_video.jpg
motion-telegram-bot.send-video-preview -f /home/user/test_video.mp4 -b $BOT_AUTH -c $CHANNEL_ID
```
### motion-telegram-bot.send-validated-video-preview
Sends a video preview image if it exists and video size is greater than **-m** value.
```bash
motion-telegram-bot.send-validated-video-preview -f /home/user/test_video.mp4 -b $BOT_AUTH -c $CHANNEL_ID -m 25
```


## Flags
```
  -h, --help            Show this help message and exit
  -f FILE, --file FILE  A path to video or image
  -b BOT, --bot BOT     Telegram auth token
  -c CHAT, --chat CHAT  Telegram channel id
  -m MINIMAL, --minimal MINIMAL
                        Validation property: minimal file size in Mb (default 10Mb)
```

## Build a snap

```bash
## To build snap you will need KVM
sudo apt install cpu-checker
sudo kvm-ok
## If not OK and virtualization enabled in BIOS
sudo apt install -y qemu qemu-kvm libvirt-daemon libvirt-clients bridge-utils virt-manager

sudo snap install snapcraft --classic
sudo snap install multipass
multipass launch --name foo

git clone https://github.com/alexmitroff/motion-telegram-bot.git
cd motion-telegram-bot
snapcraft
sudo snap install motion-telegram-bot_X.X_amd64.snap --dangerous
```
