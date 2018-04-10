#!/usr/bin/env python3

from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
import logging

import argparse
import subprocess
import logging
from systemd.journal import JournalHandler

import os

from pythonosc import dispatcher
from pythonosc import osc_server

last_gpio_value = -1
omx_a = -1
omx_b = -1

class Video_Player:
	def __init__(self, player_id, video_path):
		self.player_id = player_id
		self.video_path = video_path
		self.player = OMXPlayer(video_path, args=['--loop'], dbus_name="org.mpris.MediaPlayer2.player"+player_id)
		sleep(2)
	# 

	def load(self, video_path):
		self.player.hide_video()
		self.video_path = video_path
		self.player.load(video_path)

	def play(self):
		self.player.play()
		self.player.show_video()

	def pause(self):
		self.player.hide_video()
		self.player.pause()

	def stop(self):
		self.player.stop()

def osc_handler(unused_addr, args, value):
	global last_gpio_value
	if value == 1:
		if last_gpio_value != value:
			last_gpio_value = 1
			log.info("1")
			print("1")
			omx_a.play()
	if value == 0:
		if last_gpio_value != value:
			last_gpio_value = 0
			log.info("0")
			print("0")
			omx_a.pause()

def main():
	global omx_a
	global omx_b
	omx_a = Video_Player('a',"/var/lib/samba/usershares/medias/1.mp4")
#	omx_b = Video_Player('b',"/var/lib/samba/usershares/medias/2.mp4")

#	omx_a.pause()
#	omx_b.pause()



if __name__ == '__main__':
	main()



	parser = argparse.ArgumentParser()
	parser.add_argument("--ip",
		default="127.0.0.1", help="The ip to listen on")
	parser.add_argument("--port",
		type=int, default=5005, help="The port to listen on")
	args = parser.parse_args()

	script_path = (os.path.dirname(os.path.abspath(__file__)))
	log = logging.getLogger('demo')
	log.addHandler(JournalHandler())
	log.setLevel(logging.INFO)
	dispatcher = dispatcher.Dispatcher()
	dispatcher.map("/gpio", osc_handler, "gpio")

	server = osc_server.ThreadingOSCUDPServer(
	(args.ip, args.port), dispatcher)
	print("Serving on {}".format(server.server_address))

	try:
		server.serve_forever()
	except KeyboardInterrupt:
		omx_a.player.quit()
		pass
