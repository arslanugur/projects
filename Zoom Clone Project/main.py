# Simple Zoom Clone
# pip install vidstream

# PART I
# from vidstream import AudioSender, AudioReceiver, ScreenShareClient, CameraClient, StreamingServer
from vidstream import *
import tkinter as tk
import socket
import threading
# import requests

# To find IP address
# cmd --> ipconfig --> IPv4 Address
local_ip_address = socket.gethostbyname(socket.gethostname())
# public_ip_address = requests.get('https://api.ipify.org').text
# server = StreamingServer('192.168.0.207', 9999)
# print(local_ip_address)

server = StreamingServer(local_ip_address, 9999)
receiver = AudioReceiver(local_ip_address, 8888)

# PART III
# Streaming Functions

def start_listening():
  t1 = threading.Thread(target=server.start_server)
  t2 = threading.Thread(target=receiver.start_server)
  t1.start()
  t2.start()

def start_camera_stream():
  camera_client = CameraClient(text_target_ip.get(1.0, 'end-1c'), 7777)
  t3 = threading.Thread(target=camera_client.start_stream)
  t3.start()
  
def start_screen_sharing():
  screen_client = ScreeenShareClient(text_target_ip.get(1.0, 'end-1c'), 7777)
  t4 = threading.Thread(target=screen_client.start_stream)
  t4.start()

def start_audio_stream():
  audio_sender = AudioSender(text_target_ip.get(1.0, 'end-1c'), 6666) # gonna connect 6666
  t5 = threading.Thread(target=audio_sender.start_stream)
  t5.start()  
  
  
  
  
# PART II
# GUI
window.title("I call v0.0.1 Alpha")
window.geometry('300x200')

label_target_ip = tk.Label(window, text="Target IP:")
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

btn_listen = tk.Button(window, text="Start Listening", width=50, command=start_listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text="Start Camera Stream", width=50, command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text="Start Screen Sharing", width=50, command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text="Start Audio Stream", width=50, command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()


# PART IV
# Demonstration
# Connection between two IP



