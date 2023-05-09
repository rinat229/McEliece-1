#!/usr/bin/env python3

from McEliece import McEliece
from LDPC import LDPC
from QC_LDPC import QC_LDPC
import numpy as np

n = 1000
d_v = 20
d_c = 25

ldpc = LDPC.from_params(n, d_v, d_c)

word = np.random.randint(2, size=ldpc.getG().shape[0])
print("word:", word)

crypto = McEliece.from_linear_code(ldpc, 21)

encrypted = crypto.encrypt(word)
print("encrypted:", encrypted)

decrypted = crypto.decrypt(encrypted)
print("decrypted:", decrypted)

assert (word == decrypted).all()