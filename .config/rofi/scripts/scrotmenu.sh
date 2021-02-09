#!/bin/bash

option1="Entire screen"
option2="Focused window"
option3="Select area"

options="$option1\n$option2\n$option3"

choice=$(echo -e "$options" | rofi -dmenu -no-show-icons -no-sidebar-mode -lines 3 -width 20 -p "scrot" -theme ~/.config/rofi/themes/Qogir.rasi)

case $choice in
	$option1)
		scrot -e 'mv $f ~/Pictures/Scrot/' ;;
	$option2)
		scrot -u -e 'mv $f ~/Pictures/Scrot/' ;;
	$option3)
		scrot -s -e 'mv $f ~/Pictures/Scrot/' ;;
esac
