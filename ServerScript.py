# -*- coding: utf-8 -*-
"""
Created on Sat May  8 15:25:09 2021

@author: Neel Shah
"""

import asyncio
import threading
import time
import Backend.ServerClass as Server

try:
    from kivy.core.clipboard import Clipboard
except:
    pass


ServerEvent = asyncio.get_event_loop()

ClientConnection = ServerEvent.create_server(Server, '0.0.0.0', 5000)
StartServer = ServerEvent.run_until_complete(ClientConnection)

# Serve requests until Ctrl+C is pressed
#print('Serving on {}'.format(StartServer.sockets[0].getsockname()))
#try:
    #threading.Thread(target=are_you_ok).start()
    #ServerEvent.run_forever()
#except KeyboardInterrupt:
#    pass

StartServer.close()
ServerEvent.run_until_complete(StartServer.wait_closed())
ServerEvent.close()
