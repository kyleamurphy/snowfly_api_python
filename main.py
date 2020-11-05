import CreateTokenPYJWT
import CreateTokenJWCRYPTO
import Users

key = CreateTokenPYJWT.get_private_key()

header = CreateTokenPYJWT.get_header()

claims = CreateTokenPYJWT.get_claims()

token = CreateTokenPYJWT.build_token(key, header, claims)

users = Users.get_users(token, 1, 1)

print("-------- Next Package jwcrypto ---------")

token2 = CreateTokenJWCRYPTO.build_token(header, claims)

users2 = Users.get_users(token2, 2, 1)
