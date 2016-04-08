xbindkeys
while true; do
    xsetroot -name "$(date "+%A %d. %B %H:%M")"
    sleep 10s
done&
xautolock -time 5 -locker slock &
exec dwm
