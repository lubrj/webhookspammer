from dhooks import Webhook
import time

webhooks = []
count=1
anzahl=1
webhooknuber = 0

print("""
                                                                                                 
  ____   ______        __   _     _                 _    _____         _            
 |  _ \ / ___\ \      / /__| |__ | |__   ___   ___ | | _|_   _|__  ___| |_ ___ _ __ 
 | | | | |    \ \ /\ / / _ \ '_ \| '_ \ / _ \ / _ \| |/ / | |/ _ \/ __| __/ _ \ '__|
 | |_| | |___  \ V  V /  __/ |_) | | | | (_) | (_) |   <  | |  __/\__ \ ||  __/ |   
 |____/ \____|  \_/\_/ \___|_.__/|_| |_|\___/ \___/|_|\_\ |_|\___||___/\__\___|_|   
                                                                                                         
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
