#!/bin/bash
# Workspace 4 : plusieurs terminaux
i3-msg 'workspace "4:Term"'

# Terminal principal
i3-msg 'exec i3-sensible-terminal'
sleep 1.0

# Terminal à droite
i3-msg 'split h'
i3-msg 'exec i3-sensible-terminal'
sleep 1.0

# Terminal en bas à droite
i3-msg 'focus right'
i3-msg 'split v'
i3-msg 'exec i3-sensible-terminal'
