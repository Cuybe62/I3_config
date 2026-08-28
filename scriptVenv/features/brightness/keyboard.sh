#!/bin/bash

case "$1" in 

"set")
     
    brightnessctl -q --device='smc::kbd_backlight' set "${2}%"
    ;;

"status")
    current=$(brightnessctl --device='smc::kbd_backlight' get) || exit 1
    maximum=$(brightnessctl --device='smc::kbd_backlight' max) || exit 1
    printf '%d\n' "$((current * 100 / maximum))"
    ;;
esac
