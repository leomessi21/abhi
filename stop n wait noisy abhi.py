import random
import time

def simulate_noisy_channel(p):
    """
    Simulates a noisy channel by randomly dropping packets with a probability of p.
    Returns True if packet is received and False if packet is lost.
    """
    r = random.random()
    if r < p:
        return False # packet lost
    else:
        return True # packet received

def sender(message, p):
    """
    Implements the sender for the Stop-and-Wait protocol.
    Sends one packet at a time and waits for an acknowledgement before sending the next packet.
    """
    print("Sender: Message to be sent -", message)

    # Divide message into packets of size 1 byte (8 bits)
    packet_size = 8
    num_packets = len(message) // packet_size
    if len(message) % packet_size != 0:
        num_packets += 1
    packets = [message[i*packet_size:(i+1)*packet_size] for i in range(num_packets)]

    # Send each packet one by one and wait for acknowledgement
    for i in range(num_packets):
        packet = packets[i]
        print("Sender: Sending packet", i+1, "-", packet)

        # Wait for acknowledgement
        while True:
            if simulate_noisy_channel(p):
                print("Sender: Packet", i+1, "received by receiver.")
                break
            else:
                print("Sender: Packet", i+1, "lost due to corruption. Resending packet.")

    print("Sender: Message sent.")

def receiver(p):
    """
    Implements the receiver for the Stop-and-Wait protocol.
    Receives one packet at a time and sends an acknowledgement for each packet.
    """
    print("Receiver: Waiting for packets...")

    # Receive each packet one by one and send acknowledgement
    i = 0
    while True:
        if simulate_noisy_channel(p):
            print("Receiver: Packet", i+1, "received.")
            i += 1
            # Send acknowledgement
            time.sleep(1) # simulate processing time
            print("Receiver: Sending acknowledgement for packet", i)
        else:
            print("Receiver: Packet", i+1, "lost due to corruption. Requesting retransmission.")
            # Request retransmission
            time.sleep(1) # simulate processing time
            print("Receiver: Requesting retransmission of packet", i+1)

        # Check if all packets have been received
        if i == 8:
            break

    print("Receiver: All packets received.")

# Example usage
message = "Hello"
p = 0.1 # probability of corruption
sender(message, p)
receiver(p)
