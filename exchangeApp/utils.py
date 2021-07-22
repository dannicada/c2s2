class DH_Endpoint(object):
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None
        
    def generate_partial_key(self):
        partial_key = self.public_key1**self.private_key
        partial_key = partial_key%self.public_key2
        return partial_key
    
    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r**self.private_key
        full_key = full_key%self.public_key2
        self.full_key = full_key
        return full_key
    
    def encrypt_message(self, message):
        encrypted_message = ""
        key = self.full_key
        for c in message:
            encrypted_message += chr(ord(c)+key)
        return encrypted_message
    
    def decrypt_message(self, encrypted_message):
        decrypted_message = ""
        key = self.full_key
        for c in encrypted_message:
            decrypted_message += chr(ord(c)-key)
        return decrypted_message



def init_DH_endpoints(instance, public_key1, public_key2, private_key1, private_key2):
    sender = DH_Endpoint(public_key1, public_key2, private_key1)
    print('first')
    reciever = DH_Endpoint(public_key1, public_key2, private_key2)
    print('second')

    # generate and store sender's partial key
    sender_partial=sender.generate_partial_key()
    instance.sender_partial_key = sender_partial
    print(sender_partial)

    # generate and store reciever's partial key
    reciever_partial = reciever.generate_partial_key()
    instance.reciever_partial_key = reciever_partial
    print(reciever_partial)

    # generate sender full key
    sender_full_key = sender.generate_full_key(sender_partial)
    print(sender_full_key)

    # generate reciever full key
    reciever_full_key = sender.generate_full_key(sender_partial)
    print(reciever_full_key)

    return


