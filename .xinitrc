xset -b
xbindkeys
bat=/sys/class/power_supply/BAT0/
batfull=`cat /sys/class/power_supply/BAT0/energy_full`
while true; do
    if [ "$(cat $bat/status)" = "Discharging" ]; then
	bat100=$((100 * `cat /sys/class/power_supply/BAT0/energy_now`))
	xsetroot -name "bat=$((bat100/batfull))%  $(date "+%A %d. %B %H:%M")"
    else
	xsetroot -name "$(date "+%A %d. %B %H:%M")"
    fi
    sleep 10s
done&
xautolock -time 5 -locker slock &
exec dwm
