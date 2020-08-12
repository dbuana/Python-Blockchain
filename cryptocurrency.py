# Basic blockchain idea, for other file but, did not work out :-p
import hashlib
import datetime

# Here is a simpler idea of a blockchain, similar to the one in the previous file. This one gives more
# of a basic understanding of idea.
class Block:
    # The transaction function
    def __init__(self, previous_block_hash, timestamp, data):
        # The transaction function with its variables
        # A transaction consists of data, time, hexidecimal and etc. However, this plays the role of a tracker.
        self.previous_block_hash = previous_block_hash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.get_hash()
    
    # As a summary, this function will convert transactions into a hexidecimal form, for securing transactions made 
    def get_hash(self):
        hash_convert = (str(self.previous_block_hash)+str(self.data)+str(self.timestamp)).encode()
        # This will be essential to secure transactions
        private_hash = hashlib.sha256(hash_convert).hexdigest().encode()
        public_hash = hashlib.sha256(private_hash).hexdigest() # When public it should be more secure
        return public_hash
