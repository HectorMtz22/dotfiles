#!/bin/sh

# systray battery icon
cbatticon -u 5 &
# systray volume
volumeicon &
feh --bg-scale ~/Pictures/wallpaper.jpg &

# New config for Gnome Keyring
#eval $(/usr/bin/gnome-keyring-daemon --start --components=pkcs11,secrets,ssh)
#export SSH_AUTH_SOCK
#export GPG_AGENT_INFO
