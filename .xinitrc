xset -b
xbindkeys
bat_dir=/sys/class/power_supply/BAT0/
batfull=`cat $bat_dir/energy_full`

while true; do

    # Date and time
    date_str=`date "+%A %d. %B %H:%M"`
    # Memory
    mem_str=`free | sed -n 2p | awk '{ printf "%d.2%s", 100*$3/$2, "%" }'`
    mem_str="[MEM] $mem_str"
    # Battery
    bat_str=$((100 * `cat $bat_dir/energy_now` / batfull))
    if [ "$(cat $bat_dir/status)" = "Discharging" ]; then
	bat_str="[BAT] $bat_str%"
    else
	bat_str="[AC] ($bat_str%)"
    fi
    # Network
    net_str=`ip -br -4 a | grep UP | awk '{printf "%s %s -- ", $1, $3 }'`

    xsetroot -name "$net_str$bat_str -- $mem_str -- $date_str"
    sleep 10s
done&

hsetroot -full ~/suckless.org/bkg.png
recent=~/.config/spotify/Users/kjempelodott-user/recently_played.bnk
font=/usr/share/texmf/fonts/opentype/public/tex-gyre/texgyreadventor-regular.otf

img_orig=$(mktemp)
img=$(mktemp)
last=
last_thumb=

while true; do
    if pgrep spotify 2>&1 >/dev/null
    then
	cur=$(strings -20 $recent | grep track | head -1)
	if [[ "$cur" != "$last" ]]
	then
	    url="https://embed.spotify.com/oembed/?url=${cur:1}"
	    json=$(curl -X GET "$url" 2>/dev/null)
	    thumb=$(echo $json | jq -r '.thumbnail_url' | sed 's/cover/640/')
	    if [[ "$thumb" != "$last_thumb" ]]
	    then
		curl -X GET "$thumb" 2>/dev/null > $img_orig
		last_thumb=$thumb
	    fi
	    title=$(echo $json | jq -r '.title')
	    convert $img_orig -brightness-contrast -20x-20 $img
	    convert +append $img $img_orig $img $img
	    convert $img -bordercolor Black -border 0x100 $img
	    convert $img -gravity south -font $font -pointsize 50 -fill White -annotate 0 "$title" $img
	    hsetroot -center $img
	    last=$cur
	fi
	sleep 5
    fi
    sleep 10
done&

xss-lock slock &
xautolock -time 5 -locker slock &
exec dwm
