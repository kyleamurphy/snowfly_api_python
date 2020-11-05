import random
import time
import jwt
import config

# Obviously this code can be more concise, I left it this way so that debugging would be a little easier.


def get_private_key():
    # open up the key to read
    f = open(config.keyfile_path_name, "r")
    # place the key contents into a variable for later
    private_key = f.read()
    return private_key


def get_header():
    header = dict(kid=config.kid, alg="RS256")
    return header


def get_claims():
    # Randomly generate an Identifier. I suggest expanding this to fit your needs.
    jti = random.randrange(10)
    # the issued_at claim is just the time the token was generated in a unix timestamp
    iat = int(time.time())
    # the expiration claim is the time at which this token will become invalid. I suggest keeping short token life-times
    # If you need long-living tokens I would suggest restricting the scope of the token by declaring the scopes for
    # which the token will be valid. you can do this by adding an additional 'scopes' claim and refer to the available
    # scopes in the documentation.
    exp = int(time.time() + (3 * 60))
    claims = dict(jti=jti, iss=config.iss, sub=config.sub, eid=config.eid, cid=config.cid, iat=iat, exp=exp)
    return claims


def build_token(key, header, claims):
    # This will build the token by base 64ing the header and body, and will then attach the signature.
    encoded = str(jwt.encode(claims, key, algorithm='RS256', headers=header))

    # For some reason when I make the token a string it appends a couple of leading character and a trailing character.
    # There is probably a better way to do this
    encoded = encoded.strip("b'")
    encoded = encoded.strip("'")
    return encoded
