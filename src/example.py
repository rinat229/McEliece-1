#!/usr/bin/env python3

from McEliece import McEliece
from LDPC import LDPC
from QC_LDPC import QC_LDPC
import numpy as np

n = 500
d_v = 10
d_c = 20

ldpc = LDPC.from_params(n, d_v, d_c)

word = np.random.randint(2, size=ldpc.getG().shape[0])
print("word:", word)

crypto = McEliece.from_linear_code(ldpc, 15)

encrypted = crypto.encrypt(word)
print("encrypted:", encrypted)

decrypted = crypto.decrypt(encrypted)
print("decrypted:", decrypted)

assert (word == decrypted).all()