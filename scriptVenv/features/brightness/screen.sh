#!/bin/bash

case "$1" in 

"set")
    brightnessctl -q set "${2}%"
    ;;
"status")
    brightnessctl -q get
    ;;
esac