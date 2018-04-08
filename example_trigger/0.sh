#!/bin/bash
OMXDBUS=/usr/local/bin/omx_dbus_ctl

$OMXDBUS hidevideo
$OMXDBUS setposition 0

STRING_IS_PAUSED="$($OMXDBUS status | grep Paused:)"
if [ "$STRING_IS_PAUSED" = "Paused: false" ]; then
PLAYING=1
else
PLAYING=0
fi

if [ "$PLAYING" == "1" ];then
$OMXDBUS pause
else
echo "already paused"
fi

$OMXDBUS setposition 0


