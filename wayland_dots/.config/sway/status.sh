#!/bin/bash

#FOCUSED=`swaymsg -t get_tree | jq -r '.. | (.nodes? // empty)[] | select(.focused==true) | .name'`

TIME=`date +'%H:%M:%S'`
BATUSE=`acpi -b | awk '{ print $4 }'`
COL='\033[0;31m'
RESET='\033[0m'
SPACE="<span foreground='coral'>\U00002588\U00002588</span>"

echo -e "$SPACE" "\U0001F50B" $BATUSE "$SPACE" $TIME

