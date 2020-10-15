#!/bin/bash

TIME=`date +'%H:%M:%S'`
BATUSE=`acpi -b | awk -F', ' '{ print $2 }'`
TEMP=`acpi -t | awk '{ print $4 }'`
COL='\033[0;31m'
RESET='\033[0m'
SPACE="<span foreground='coral'>\U00002588\U00002588</span>"
SMILE="<span foreground='yellow'>\U0001F600</span>"

echo -e "$SPACE" "\U0001F321" $TEMP "$SPACE" "\U0001F50B" $BATUSE "$SPACE" $TIME $SMILE

