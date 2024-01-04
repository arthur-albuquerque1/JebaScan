#!/bin/python3

from visual import visual
from scan import portScan
import socket

#visualeffects
visual.lines()
visual.opening()
visual.lines()

#mode selection
print('\n|0|: Unico endereço\n|1|: Lista de endereços')
mode = int(input('Selecione o modo: '))
if mode == 0:
	visual.lines()
	target = socket.gethostbyname(input('Digite o endereço do alvo: '))
	port1 = int(input('Digite a primeira porta TCP: '))
	port2 = int(input('Digite a ultima porta TCP: '))
	visual.banner(target)
	portScan.scan(target, port1, port2)		
elif mode == 1:
	visual.lines()
	filename = input('Digite o nome do arquivo de texto: ')
	with open(filename) as archive:
		ip_list = archive.read().splitlines()
	port1 = int(input('Digite a primeira porta TCP: '))
	port2 = int(input('Digite a ultima porta TCP: '))
	for ip in ip_list:
		target = ip
		visual.banner(target)
		portScan.scan(target, port1, port2)
	
else:
	print('Modo invalido')
