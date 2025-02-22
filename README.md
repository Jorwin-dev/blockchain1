# blockchain1
Blockchain Network

## Overview
This project is a **Python-based blockchain network** that implements a **proof-of-work (PoW) consensus mechanism**. It allows nodes to mine blocks, create transactions, and maintain a distributed ledger. The blockchain is built using **Flask** for the API, **SHA-256 cryptographic hashing**, and includes **basic networking functionality** for decentralized consensus.

## Tech Stack
- **Python** – Core development language
- **Flask** – RESTful API to interact with the blockchain
- **Proof-of-Work (PoW)** – Used for mining new blocks
- **SHA-256 Cryptographic Hashing** – Secures blocks
- **Requests & JSON** – Handles transactions and consensus mechanisms

## Features
- **Decentralized blockchain** – Each node maintains a local copy of the ledger.
- **Mining mechanism** – Uses PoW to validate new blocks and append them to the chain.
- **REST API endpoints** – Allows interaction with the blockchain network.
- **Transaction processing** – Users can send transactions to be recorded in the blockchain.
- **Consensus Algorithm** – Implements the **longest chain rule** to resolve conflicts among nodes.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/blockchain-network.git
   cd blockchain-network
   ```
2. Install dependencies:
   ```bash
   pip install flask requests
   ```
3. Run the blockchain node:
   ```bash
   python blockchain.py
   ```

## API Endpoints
### **Mine a new block**
```http
GET /mine
```
- Runs the **Proof-of-Work algorithm**, generates a new block, and appends it to the blockchain.

### **Get the full blockchain**
```http
GET /chain
```
- Returns the entire blockchain in JSON format.

### **Create a new transaction**
```http
POST /transactions/new
Content-Type: application/json
{
    "sender": "A",
    "recipient": "B",
    "amount": 10
}
```
- Adds a new transaction to the list of pending transactions.

### **Register a new node**
```http
POST /nodes/register
Content-Type: application/json
{
    "nodes": ["http://127.0.0.1:5001"]
}
```
- Registers a new node to the blockchain network.

### **Consensus Algorithm (Resolve conflicts)**
```http
GET /nodes/resolve
```
- Implements the **longest chain rule**, ensuring all nodes in the network agree on the same blockchain.

## Example Code Snippet
```python
import hashlib
import json
from time import time
from flask import Flask, jsonify, request

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash='1', proof=100)
    
    def new_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.current_transactions = []
        self.chain.append(block)
        return block
```

## Future Improvements
- Implement **Proof-of-Stake (PoS)** as an alternative consensus mechanism.
- Add **smart contract functionality** for automation.
- Enhance security with **asymmetric cryptography**.

## Contact
For inquiries or collaborations, reach out via [LinkedIn](https://www.linkedin.com/in/jorwinreyes/) or [GitHub](https://github.com/Jorwin-dev).

