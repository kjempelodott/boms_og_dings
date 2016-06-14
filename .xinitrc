xset -b
xbindkeys
bat=/sys/class/power_supply/BAT0/
batfull=`cat $bat/energy_full`

while true; do
    batnow=$((100 * `cat $bat/energy_now` / batfull))
    if [ "$(cat $bat/status)" = "Discharging" ]; then
	xsetroot -name "[BAT] $batnow% -- $(date "+%A %d. %B %H:%M")"
    else
	xsetroot -name "[AC] ($batnow%) -- $(date "+%A %d. %B %H:%M")"
    fi
    sleep 10s
done&

xautolock -time 5 -locker slock &
exec dwm
