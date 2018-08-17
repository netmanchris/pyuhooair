
import hashlib



class UhooAuth():

    def __init__(self, email, password):
        self.email = email
        salt1 = b'154f7c2e9bd94d5d90aa382ae199206a4048c9ce931c78680b0942355ca918b1'
        salt2 = b'@uhooinc.com'
        new_hash = hashlib.sha256()
        new_hash.update(salt1+bytes(password, 'utf-8')+salt2)
        self.hexdigest = new_hash.hexdigest()
