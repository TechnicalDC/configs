#!/bin/bash

option1="Lock"
option2="Logout"
option3="Reboot"
option4="Power off"

options="$option1\n$option2\n$option3\n$option4"

choice=$(echo -e "$options" | rofi -dmenu -no-show-icons -lines 4 -width 20 -p "power" -theme ~/.config/rofi/themes/Qogir.rasi -xoffset 537 -yoffset -272 )

case $choice in
	$option1)
		mantablockscreen -cc ;;
	$option2)
		bspc quit || i3-msg exit ;;
	$option3)
		systemctl reboot ;;
	$option4)
		systemctl poweroff ;;
esac
