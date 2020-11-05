from jwcrypto import jwt, jwk
import config


def get_key():
    # This package need you to open the PEM file with additional permissions
    return open(config.keyfile_path_name, "rb")


def build_token(header, claims):
    # Get the opened key
    key = get_key()
    # initialize the key from the pem file
    key = jwk.JWK.from_pem(key.read())
    # build the token
    token = jwt.JWT(header=header, claims=claims)
    # sign the token with the key
    token.make_signed_token(key)
    # serialize it
    encoded = token.serialize()

    # For some reason when I make the token a string it appends a couple of leading character and a trailing character.
    # There is probably a better way to do this
    encoded = encoded.strip("b'")
    encoded = encoded.strip("'")
    return encoded
