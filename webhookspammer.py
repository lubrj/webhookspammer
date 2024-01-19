from dhooks import Webhook
import time

webhooks = []
count=1
anzahl=1
webhooknuber = 0

print("""
                                                                                        _     _                 _                                                  
 __      _| |__ | |__   ___   ___ | | _____ _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
 \ \ /\ / / '_ \| '_ \ / _ \ / _ \| |/ / __| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
  \ V  V /| |_) | | | | (_) | (_) |   <\__ \ |_) | (_| | | | | | | | | | | |  __/ |   
   \_/\_/ |_.__/|_| |_|\___/ \___/|_|\_\___/ .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                           |_|                                        
                                                                                                         
                                    Made by LUBRJ
""")

webhookcounts = int(input("how many webhooks: "))

while webhookcounts>=anzahl:
  webhooks.append(Webhook(input("webhook"+str(anzahl)+": ")))
  anzahl=anzahl+1


massage = input("massage: ")
times = int(input("how many massages: "))

while times>=count:
    webhooks[webhooknuber].send(massage)
    print("Sent.")
    count=count+1
    webhooknuber=webhooknuber+1
    if webhooknuber==webhookcounts:
       webhooknuber=0
