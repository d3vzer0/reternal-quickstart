import random
import string

class Random:
    def create(size):
        random_result = ''.join([random.choice(
                                string.ascii_letters + string.digits)
                                for n in range(size)])
        return random_result