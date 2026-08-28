#!/bin/bash
# Workspace 2 : Brave + Code côte à côté
i3-msg 'workspace "2:Web+Code"'
i3-msg 'exec brave'
sleep 1.2
i3-msg 'split h'
i3-msg 'exec code'
