xbindkeys -f .xbindkeysrc
xrdb -merge ~/.Xdefaults
setxkbmap -layout no
xscreensaver &
exec qtile
