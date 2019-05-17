from Crypto.PublicKey import RSA

class CreateCrypto:
    def __init__(self, path='/opt/reternal'):
        self.path = path
        self.pub_key = '{0}/rsa/pub.pem'.format(self.path)
        self.priv_key = '{0}/rsa/priv.key'.format(self.path)

    def rsa(self):
        key = RSA.generate(2048)
        private_key = key.export_key()
        file_out = open(self.priv_key, "wb")
        file_out.write(private_key)

        public_key = key.publickey().export_key()
        file_out = open(self.pub_key, "wb")
        file_out.write(public_key)

if __name__ == "__main__":
    CreateCrypto().rsa()