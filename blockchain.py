class Blockchain(object):
    def _init_(self):
        self.chain = []
        self.current_transactions = []
        
    def new_block(self):
        # creates a new Block and adds it to the chain pass

    def new_transactions(self):
        # adds a new transaction to the list of transactions pass

    @staticmethod
    def hash(block):
        # hashes a Block
        pass

    @property
    def last_block(self):
        # returns the last Block in the chain pass