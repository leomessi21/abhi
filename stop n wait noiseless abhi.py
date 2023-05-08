import time

# Sender function
def sender(message):
    print("Sender: Message to be sent -", message)

    # Divide the message into packets of size 1 byte (8 bits)
    packet_size = 8
    num_packets = len(message) // packet_size
    if len(message) % packet_size != 0:
        num_packets += 1
    packets = [message[i:i+packet_size] for i in range(0, len(message), packet_size)]

    # Send each packet one by one and wait for acknowledgement
    for i, packet in enumerate(packets):
        print("Sender: Sending packet", i+1, "-", packet)
        time.sleep(1)

        # Wait for acknowledgement
        ack = False
        while not ack:
            print("Sender: Waiting for acknowledgement of packet", i+1)
            time.sleep(1)

            # If acknowledgement is received, move on to the next packet
            if receiver(packet):
                print("Sender: Packet", i+1, "acknowledged by receiver.")
                ack = True

    print("Sender: Message sent.")

    # Send an empty packet to signal end of transmission
    print("Sender: Sending empty packet to signal end of transmission.")
    time.sleep(1)
    while not receiver(''):
        print("Sender: Waiting for acknowledgement of end of transmission.")
        time.sleep(1)
    print("Sender: End of transmission acknowledged by receiver.")

# Receiver function
def receiver(packet):
    # If packet is empty, acknowledge end of transmission
    if not packet:
        return True

    print("Receiver: Waiting for packets...")

    # Wait for packet to arrive
    time.sleep(1)
    print("Receiver: Packet received -", packet)

    # Send acknowledgement
    time.sleep(1)
    print("Receiver: Acknowledging receipt of packet.")
    return True

# Main function
def main():
    # Call the sender function with the message to be sent
    sender("Hello world!")

if __name__ == '__main__':
    main()
