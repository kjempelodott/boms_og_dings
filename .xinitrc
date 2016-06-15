xset -b
xbindkeys
bat_dir=/sys/class/power_supply/BAT0/
batfull=`cat $bat_dir/energy_full`

while true; do

    # Date and time
    date_str=`date "+%A %d. %B %H:%M")`
    # Battery
    bat_str=$((100 * `cat $bat_dir/energy_now` / batfull))
    if [ "$(cat $bat_dir/status)" = "Discharging" ]; then
	bat_str="[BAT] $bat_str% --"
    else
	bat_str="[AC] ($bat_str%) --"
    fi
    # Network
    net_str=
    _IFS=$IFS
    IFS=$'\n'
    for iface_up in `ip -br -4 a | grep UP`
    do
	_tmp=`echo $iface_up | awk '{printf "%s %s", $1, $3 }'`
	net_str="$_tmp -- $net_str"
    done
    IFS=$_IFS

    xsetroot -name "$net_str$bat_str $date_str"
    sleep 10s
    
done&

xautolock -time 5 -locker slock &
exec dwm
