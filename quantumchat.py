from quantum_encryption import QuantumEncryption
from quantum_communication import QuantumCommunication

# Initialize quantum encryption and communication
quantum_encryption = QuantumEncryption()
quantum_communication = QuantumCommunication()

# Connect to the quantum network
quantum_communication.connect()

while True:
    message = input("Enter your message: ")
    
    # Encrypt the message using quantum encryption
    encrypted_message = quantum_encryption.encrypt(message)
    
    # Transmit the message through quantum communication
    quantum_communication.send(encrypted_message)
    
    # Receive and decrypt incoming messages
    received_message = quantum_communication.receive()
    decrypted_message = quantum_encryption.decrypt(received_message)
    
    print(f"Received: {decrypted_message}")
