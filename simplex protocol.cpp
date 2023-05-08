#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

using namespace std;

// Function to simulate a noisy channel
bool is_corrupted(float p) {
    float r = static_cast<float>(rand()) / static_cast<float>(RAND_MAX);
    return (r < p);
}

// Sender function
void sender(string message, float p) {
    cout << "Sender: Message to be sent - " << message << endl;

    // Divide the message into packets of size 1 byte (8 bits)
    int packet_size = 8;
    int num_packets = message.length() / packet_size;
    if (message.length() % packet_size != 0) {
        num_packets++;
    }
    string packets[num_packets];
    for (int i = 0; i < num_packets; i++) {
        packets[i] = message.substr(i * packet_size, packet_size);
    }

    // Send each packet one by one
    for (int i = 0; i < num_packets; i++) {
        cout << "Sender: Sending packet " << i+1 << " - " << packets[i] << endl;

        // Simulate a noisy channel
        if (is_corrupted(p)) {
            cout << "Sender: Packet " << i+1 << " lost due to corruption." << endl;
        }
        else {
            cout << "Sender: Packet " << i+1 << " received by receiver." << endl;
        }
    }

    cout << "Sender: Message sent." << endl;
}

// Receiver function
void receiver(float p) {
    cout << "Receiver: Waiting for packets..." << endl;

    // Wait for packets to arrive one by one
    int i = 0;
    while (true) {
        // Simulate a noisy channel
        if (is_corrupted(p)) {
            cout << "Receiver: Packet " << i+1 << " lost due to corruption." << endl;
        }
        else {
            cout << "Receiver: Packet " << i+1 << " received." << endl;
            i++;
        }

        // Check if all packets have been received
        if (i == 8) {
            break;
        }
    }

    cout << "Receiver: All packets received." << endl;
}

// Main function
int main() {
    // Set random seed for the random number generator
    srand(time(NULL));

    // Set probability of corruption for the noisy channel
    float p = 0.1;

    // Call the sender and receiver functions with the message to be sent
    sender("Hello", p);
    receiver(p);

    return 0;
}

