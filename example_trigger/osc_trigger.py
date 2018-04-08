"""
osc server that launch script when osc value changed
intended to be use to triger a video playback with omxplayer on a raspberry pi
"""
import argparse
import subprocess
import logging
from systemd.journal import JournalHandler

import os

from pythonosc import dispatcher
from pythonosc import osc_server

last_gpio_value = -1
script_path= -1

def gpio_handler(unused_addr, args, value):
	global last_gpio_value
	global script_path
	if value == 1:
		if last_gpio_value != value:
			last_gpio_value = 1
			log.info("1")
			subprocess.call([sh_path_1])
#			subprocess.call(['./1.sh'])
	if value == 0:
		if last_gpio_value != value:
			last_gpio_value = 0
			log.info("0")
			subprocess.call([sh_path_0])
#			subprocess.call(['./0.sh'])


if __name__ == "__main__":
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
	log.info(script_path)
	sh_path_0 = os.path.join(script_path, "0.sh")
	sh_path_1 = os.path.join(script_path, "1.sh")
	print(sh_path_0)
	dispatcher = dispatcher.Dispatcher()
	dispatcher.map("/gpio", gpio_handler, "gpio")

	server = osc_server.ThreadingOSCUDPServer(
	(args.ip, args.port), dispatcher)
	print("Serving on {}".format(server.server_address))
	server.serve_forever()
