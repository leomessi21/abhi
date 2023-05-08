# Simplex Protocol Implementation

def sender(data, window_size):
    print("Sending data using Simplex Protocol...")
    seq_num = 0
    while seq_num < len(data):
        # Send the next window of data
        window = data[seq_num:seq_num+window_size]
        print("Sending window: ", window)
        # Wait for acknowledgment from the receiver
        ack = input("Enter 'ACK' to acknowledge receipt of data: ")
        if ack == "ACK":
            print("Acknowledgment received.")

            # Move the sequence number forward
            seq_num += window_size
        else:
            print("Error: Acknowledgment not received. Resending window...")

def receiver():
    print("Waiting for data...")
    data_received = ""
    while True:
        # Receive a window of data from the sender
        window = input("Enter the window of data received: ")
        data_received += window

        # Send an acknowledgment to the sender
        ack = "ACK"
        print("Sending acknowledgment: ", ack)

        # Check if all data has been received
        if len(data_received) == len(data):
            print("All data received.")
            break

# Example usage
data = "Hello, world!"
window_size = 5

sender(data, window_size)
receiver()
