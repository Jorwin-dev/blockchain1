class Blockchain(object):
    def _init_(self):
        self.chain = []
        self.current_transactions = []
        
    def new_block(self):
        # creates a new Block and adds it to the chain pass

    def new_transactions(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient':recipient,
            'amount':amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # hashes a Block
        pass

    @property
    def last_block(self):
        # returns the last Block in the chain pass