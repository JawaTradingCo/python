# -*- coding: utf-8 -*-
"""
Chat Room Demo for Miniboa.
"""

import logging
import math, random
from miniboa import TelnetServer

IDLE_TIMEOUT = 300
CLIENT_LIST = []
SERVER_RUN = True

tempNames = {"mary":0,"veronica":0,"susan":0,"bambi":0,"michelle":0,"tina":0,"lucy":0,"julia":0,"lacy":0,"pamela":0,"angie":0,"debbie":0,"barbara":0,"hillary":0,"gina":0,"kelly":0,"rachel":0,"maddie":0}
assignedNames = {}


def on_connect(client):
    """
    Sample on_connect function.
    Handles new connections.
    """
    logging.info("Opened connection to {}".format(client.addrport()))
  
    CLIENT_LIST.append(client)
    newName = ""
    isSet = 0;
    while not newName:
    	newName = random.choice(tempNames.keys())
    	exec("isSet = tempNames['"+ newName +"']")
    	if isSet == 1:
    		newName = ""


    

	assignedNames[client.addrport()] = newName
	exec("tempNames['"+ assignedNames[client.addrport()] +"'] = 1")
    client.send("Welcome to the Chat Server.\n")
    client.send("You will be known as "+newName.title()+".\n")
    logging.info("Opened connection to {}".format(assignedNames[client.addrport()].title()))
    broadcast("{} joins the conversation.\n".format(assignedNames[client.addrport()].title()))
 

def on_disconnect(client):
    """
    Sample on_disconnect function.
    Handles lost connections.
    """
    logging.info("Lost connection to {}".format(client.addrport()))
    CLIENT_LIST.remove(client)
    broadcast("{} leaves the conversation.\n".format(assignedNames[client.addrport()].title()))
    exec("tempNames['"+ assignedNames[client.addrport()] +"'] = 0")


def kick_idle():
    """
    Looks for idle clients and disconnects them by setting active to False.
    """
    # Who hasn't been typing?
    for client in CLIENT_LIST:
        if client.idle() > IDLE_TIMEOUT:
            logging.info("Kicking idle lobby client from {}".format(assignedNames[client.addrport()].title()))
            exec("tempNames['"+ assignedNames[client.addrport()] +"'] = 0")
            client.active = False


def process_clients():
    """
    Check each client, if client.cmd_ready == True then there is a line of
    input available via client.get_command().
    """
    for client in CLIENT_LIST:
        if client.active and client.cmd_ready:
            # If the client sends input echo it to the chat room
            chat(client)


def broadcast(msg):
    """
    Send msg to every client.
    """
    for client in CLIENT_LIST:
        client.send(msg)


def chat(client):
    """
    Echo whatever client types to everyone.
    """
    global SERVER_RUN
    msg = client.get_command()
    logging.info("{} says '{}'".format(assignedNames[client.addrport()].title(), msg))

    for guest in CLIENT_LIST:
        if guest != client:
            guest.send("{} says '{}'\n".format(assignedNames[client.addrport()].title(), msg))
            # guest.send("{} says '{}'\n".format(client.addrport(), msg))
        else:
            guest.send("You say '{}'\n".format(msg))

    cmd = msg.lower()
    # bye = disconnect
    if cmd == 'bye':
        client.active = False
    # shutdown == stop the server
    elif cmd == 'shutdown':
        SERVER_RUN = False


if __name__ == '__main__':

    # Simple chat server to demonstrate connection handling via the
    # async and telnet modules.

    logging.basicConfig(level=logging.DEBUG)

    # Create a telnet server with a port, address,
    # a function to call with new connections
    # and one to call with lost connections.

    telnet_server = TelnetServer(
        port=5000,
        address='192.168.1.14',
        on_connect=on_connect,
        on_disconnect=on_disconnect,
        timeout=.05
        )

    logging.info("Listening for connections on"
                 " port {}. CTRL-C to break.".format(telnet_server.port))

    # Server Loop
    while SERVER_RUN:
        telnet_server.poll()        # Send, Recv, and look for new connections
        kick_idle()                 # Check for idle clients
        process_clients()           # Check for client input

    logging.info("Server shutdown.")

