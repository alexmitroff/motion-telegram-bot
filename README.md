# Motion Telegram bot

Simple telegram bot wrapper for sending images and video to chosen chat. Created to work with Motion output.
Powered by [python telegram bot](https://github.com/python-telegram-bot/python-telegram-bot).


## Commands
### install
```bash
sudo snap install motion-telegram-bot
```
### motion-telegram-bot.send-image
Simply sends an image if it exists.
```bash
motion-telegram-bot.send-image -i /home/user/test_image.jpg -b $BOT_AUTH -c $CHANNEL_ID
```
### motion-telegram-bot.send-video
Simply sends a video if it exists. (h264 | mp4 / mov) < 50Mb
```bash
motion-telegram-bot.send-video -i /home/user/test_video.mov -b $BOT_AUTH -c $CHANNEL_ID
```
### motion-telegram-bot.send-video-preview
Sends a video preview image if it exists.
```bash
# video:   /home/user/test_video.mp4
# preview: /home/user/test_video.jpg
motion-telegram-bot.send-video-preview -i /home/user/test_video.mp4 -b $BOT_AUTH -c $CHANNEL_ID
```
### motion-telegram-bot.send-validated-video-preview
Sends a video preview image if it exists and video size is greater than **-m** value.
```bash
motion-telegram-bot.send-validated-video-preview -i /home/user/test_video.mp4 -b $BOT_AUTH -c $CHANNEL_ID -m 25
```


## Flags
```
  -i INPUT, --input INPUT
                        Something you want to sent to telegram chat.This could
                        be a text, path to image or path to video
  -b BOT, --bot BOT     Telegram bot auth token
  -c CHAT, --chat CHAT  Telegram chat id
  -m MINIMAL, --minimal MINIMAL
                        A minimal file size.Used to filter important videos
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
