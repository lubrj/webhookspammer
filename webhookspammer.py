from dhooks import Webhook
import os

webhooks = []
count=1
anzahl=1
webhooknuber = 0

os.system("CLS")

print("""
               _     _                 _                                                  
 __      _____| |__ | |__   ___   ___ | | _____ _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
 \ \ /\ / / _ \ '_ \| '_ \ / _ \ / _ \| |/ / __| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
  \ V  V /  __/ |_) | | | | (_) | (_) |   <\__ \ |_) | (_| | | | | | | | | | | |  __/ |   
   \_/\_/ \___|_.__/|_| |_|\___/ \___/|_|\_\___/ .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                               |_|                                        
                                          made by LUBRJ
                                          github: lubrj
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
