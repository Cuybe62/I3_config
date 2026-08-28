#!/bin/bash
# Workspace 3 : Brave à gauche, Brave + terminal à droite
i3-msg 'workspace "3:Web+Term"'

# Brave à gauche
i3-msg 'exec brave'
sleep 1.2

# Deuxième Brave à droite
i3-msg 'split h'
i3-msg 'exec brave --new-window'
sleep 1.2

# Terminal en bas à droite
i3-msg 'focus right'
i3-msg 'split v'
i3-msg 'exec i3-sensible-terminal'

