#!/bin/python3

import sys
import socket

class portScan:
	def scan(target, port1, port2):
		try:
			for port in range(port1, port2 + 1):
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.settimeout(0.23)
				
				result = s.connect_ex((target, port))
				if result == 0:
					print(f'A porta {port} esta aberta')
				s.close()
		except KeyboardInterrupt:
			print('\nSaindo do programa')
			sys.exit()
		except socket.gaierror:
			print('\nHostname invalido')
			sys.exit()
		except OS.error:
			print('\nNao foi possivel se conectar ao servidor')
			sys.exit()
			
