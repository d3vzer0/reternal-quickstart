import random
import string

class Random:
    def __init__(self, size):
        self.size = int(size)

    def create(self):
        random_result = ''.join([random.choice(
            string.ascii_letters + string.digits)
                for n in range(self.size)])
        return random_result