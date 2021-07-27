from Crypto.Cipher import AES
import base64
# from Crypto import Random
# iv = Random.new().read(16)

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

    def pad(self, input):
        number_of_bytes_to_pad = AES.block_size - len(input) % AES.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_key = input + padding_str
        return padded_key

    def unpad(self, padded_input):
        last_character = padded_input[len(padded_input) - 1:]
        bytes_to_remove = ord(last_character)
        return padded_input[:-bytes_to_remove]
    
    def encrypt_message(self, message):
        key = self.pad(str(self.full_key))
        message = self.pad(message)
        cipher = AES.new(key,AES.MODE_ECB)

        #encode the message text
        encrypted_message = base64.b64encode(cipher.encrypt(message))
        #print the encoded message
        print("the encrypted message is\n", encrypted_message)
        return encrypted_message
        # encrypted_message = ""
        # key = self.full_key
        # for c in message:
        #     encrypted_message += chr(ord(c)+key)
        # return encrypted_message
    
    def decrypt_message(self, encrypted_message):
        key = self.pad(str(self.full_key))
        cipher = AES.new(key,AES.MODE_ECB)
        decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
        decrypted_message = self.unpad(decrypted_message)
        #print the decode

        print ("Original message after decryptionis \n",decrypted_message)
        # decrypted_message = ""
        # key = self.full_key
        # for c in encrypted_message:
        #     decrypted_message += chr(ord(c)-key)
        return decrypted_message



def init_DH_endpoints(instance, public_key1, public_key2, private_key1, private_key2, message):
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
    #encrypt message
    encrypted_message = sender.encrypt_message(message)
    instance.encrypted_message = encrypted_message

    decrypted_message = sender.decrypt_message(encrypted_message)

    return


