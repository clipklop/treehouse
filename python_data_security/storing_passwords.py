#


from argon2 import PasswordHasher
from uuid import uuid4
import hashlib


string = b'Misha'
string2 = b'Mischa'
test = b'Misha'
plain_string = 'Misha'

# compromised
hl_md5 = hashlib.md5(string).hexdigest()
hl_md52 = hashlib.md5(string2).hexdigest()

hl_sha256 = hashlib.sha256(string).hexdigest()


# non-compromised yet...
hl_shake = hashlib.shake_128(string).hexdigest(32)


# add some salt to our dish
salt = uuid4()
hl_saltshake = hashlib.shake_128(salt.bytes+string).hexdigest(32) + \
    ':' + salt.hex
hl_saltshake_compare = hashlib.shake_128(salt.bytes+test).hexdigest(32) + \
    ':' + salt.hex


# argon that won some competition
ph = PasswordHasher().hash(plain_string)


# print(hl_md5)
# print(hl_sha256)
# print(hl_shake)
print(salt.hex)
print(hl_saltshake)
print(hl_saltshake == hl_saltshake_compare)
print(ph)
