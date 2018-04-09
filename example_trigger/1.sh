#!/bin/bash
OMXPLAYER_DBUS_ADDR="/tmp/omxplayerdbus.${USER:-root}"
OMXPLAYER_DBUS_PID="/tmp/omxplayerdbus.${USER:-root}.pid"
export DBUS_SESSION_BUS_ADDRESS=`cat $OMXPLAYER_DBUS_ADDR`
export DBUS_SESSION_BUS_PID=`cat $OMXPLAYER_DBUS_PID`

## unmute
#dbus-send --print-reply=literal --session --dest=org.mpris.MediaPlayer2.omxplayer /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Unmute
## wait ...
sleep 0.2
##play
dbus-send --print-reply=literal --session --dest=org.mpris.MediaPlayer2.omxplayer /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Play
##unhide
dbus-send --print-reply=literal --session --dest=org.mpris.MediaPlayer2.omxplayer /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Action int32:29 >/dev/null

