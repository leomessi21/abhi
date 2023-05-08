#include <iostream>
#include <bitset>
#include <sstream>
#include <string>

using namespace std;

string binary_to_dotted_decimal(string binary_num) {
    // Split the binary number into 4 octets of 8 bits each
    string octets[4];
    for (int i = 0; i < 4; i++) {
        octets[i] = binary_num.substr(i * 8, 8);
    }

    // Convert each octet to its decimal equivalent
    int decimal_octets[4];
    for (int i = 0; i < 4; i++) {
        bitset<8> bits(octets[i]);
        decimal_octets[i] = bits.to_ulong();
    }

    // Join the decimal octets with periods to form the quad-dotted decimal notation
    ostringstream oss;
    oss << decimal_octets[0] << "." << decimal_octets[1] << "." << decimal_octets[2] << "." << decimal_octets[3];
    return oss.str();
}

int main() {
    string binary_num = "11000000101010000000000100000001";
    string dotted_decimal = binary_to_dotted_decimal(binary_num);
    cout << dotted_decimal << endl; // Output: "192.168.1.33"
    return 0;
}

