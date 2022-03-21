#!/usr/bin/python3

import random
import string

password = []
for i in range(4):
    password.append(''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(5)))

print ('-'.join(password))
