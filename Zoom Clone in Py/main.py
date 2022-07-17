# Simple Zoom Clone
# pip install vidstream

# PART I
# from vidstream import AudioSender, AudioReceiver, ScreenShareClient, CameraClient, StreamingServer
from vidstream import *
import tkinter as tk
import socket
import threading
import requests

# To find IP address
# cmd --> ipconfig --> IPv4 Address
local_ip_address = socket.gethostbyname(socket.gethostname())
# public_ip_address = requests.get('https://api.ipify.org').text
# server = StreamingServer('192.168.0.207', 9999)
# print(local_ip_address)


# PART II
# GUI
window.title("I call v0.0.1 Alpha")
window.geometry('300x200')

label_target_ip = tk.Label(window, text="Target IP:")
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

btn_listen = tk.Button(window, text="Start Listening", width=50)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text="Start Camera Stream", width=50)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text="Start Screen Sharing", width=50)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text="Start Audio Stream", width=50)
btn_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()


# PART III
# Streaming Funtions









