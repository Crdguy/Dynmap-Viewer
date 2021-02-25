import requests
import json
import time
#import configparser currently unused
import asyncio

#config = configparser.ConfigParser().read("settings.ini")
config = None
address = "https://apollo.heliosmc.co.uk"
worldname = "world"
lastMessage = None
    
async def update(config, address, worldname, lastMessage):
    
    src = requests.get(address + "/up/world/{}/0".format(worldname)).json()

    #Chat Events
    
    if list(src["updates"])[-1]["type"] == "chat" and list(src["updates"])[-1] != lastMessage:
        
        lastMessage = list(src["updates"])[-1]
        if "~" in lastMessage["playerName"]:
            displayName = lastMessage["playerName"] + " ({})".format(lastMessage["account"])
        else:
            displayName = lastMessage["playerName"]
        print("[{}] [CHAT] >> {} » {}".format(time.strftime("%d/%m/%Y %H:%M:%S",time.gmtime(lastMessage["timestamp"]/1000)), displayName, lastMessage["message"]))

    return lastMessage
    


if __name__ == "__main__":
    while True:
        try:
            lastMessage = asyncio.run(update(config, address, worldname, lastMessage))
        except:
            #I am very lazy
            pass
