import hashlib
import datetime


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

    def __str__(self):
        return f"Block #{self.index} [Timestamp: {self.timestamp}, Data: {self.data}, Nonce: {self.nonce}, Hash: {self.hash}]"


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")

    def get_previous_block(self):
        return self.chain[-1]

    def add_block(self, data):
        index = len(self.chain)
        previous_hash = self.get_previous_block().hash
        block = Block(index, datetime.datetime.now(), data, previous_hash)
        block.mine_block(self.difficulty)
        self.chain.append(block)

    def is_valid_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def display_chain(self):
        for block in self.chain:
            print(block)


# Example usage
blockchain = Blockchain()
blockchain.add_block("Transaction 1")
blockchain.add_block("Transaction 2")
blockchain.display_chain()
