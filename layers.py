def application_layer(message):
    return message

def presentation_layer(message, state):
    if state=="client":
       my_return= f"Compressed({message})\n                     Encrypted[Compressed({message})]"
    else:
       my_return = f"Decrypted[Decompressed({message})]\n                     Decompressed[({message})]"
    return my_return

def transport_layer(message, Protocol):
    my_return = f"[ {Protocol} | {message} ] --> Data Segment"
    return my_return

def network_layer(message, IP):
    my_return = f"[ {IP} | 172.20.10.3 | TCP | {message} ] --> Data Packet"
    return my_return

def datalink_layer(message, MAC):
    my_return = f"\n[ {MAC} | 45.34.DF.3A.87.89 | 172.20.10.2 | 172.20.10.3 | TCP | {message} | 10110 ] --> Data Frame"
    return my_return

def physical_layer(state):
    if state == "client":
        print(" 10010110001101010111101", "\n")
        print("                 Ethernet Connection...", "\n")
        print("                 +5V    ______")
        print("                       |      |")
        print("                       |      |")
        print("                 0V____|      |__ \n")
    else:
        print(" Ethernet Connection...", "\n")
        print("                 +5V    ______")
        print("                       |      |")
        print("                       |      |")
        print("                 0V____|      |__\n")
        print("                 10010110001101010111101", "\n")