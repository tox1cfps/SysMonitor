"""Real-time monitoring helper functions."""

import os
import time

import psutil


def monitor_tempo_real():
    while True:
        os.system("cls")

        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage("C:")

        print("------ SYS MONITOR ------\n")

        print(f"CPU: {cpu}%")
        print(f"RAM: {mem.percent}%")
        print(f"DISCO: {disk.percent}%")

        net = psutil.net_io_counters()

        print(f"\nUpload total: {net.bytes_sent / (1024**2):.2f} MB")
        print(f"Download total: {net.bytes_recv / (1024**2):.2f} MB")

        print("\nPressione CTRL+C para sair")

        time.sleep(1)
