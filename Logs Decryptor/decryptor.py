from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def decryption(private_key, data):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_data = cipher.decrypt(data)
    
    return decrypted_data

data = b'\x0c\xedf*\xf4{\x84\xb2\xbb&\x07\x1c8\x1f\xc4\xf34>\xb4t\xe0O\xe2\xe0\x8b\xab&\x81)\xd8U\xf4\x0f\xf9E\xf3\xa1\xcf\xdb@\xcb|\x01\x9fhj\xd5M\x93\xeeXOV\t\xc6\xac\xf3\xf5\x97X\x10\xa0\x97\x8aD\x08a\xc2\x02\x07\xa5\xab\x1c\xee\xd1\x8bM\x82\x0ffT\xaf\xa4\x0b\xba\xa0\xda\x84\x8b\x03\xe7\xb7\xf7sT+\x89n&\xb7\xba,\xd30\xe43\xdf(\x9fi_{!\xf7\xa8.\x89\xa7\xfbO\x9d\x82\x14\xff\'J:\xc7v&,\x1c\xda\xaf(<\x14\xcf\xd3sG\x12\xc3\xde\\\x81\xc5\x89\xd5\x13\xa3\xb5\x1b\xde8\xe1g1"\xb2i\xecr\n\xa794\xb7\xb9O\xc9\x13\xbfB\x81\xa8)\x00\x16\xbe\x10\xb1\xea\xa8\x7f\xdb\x9f\xd9b\x8biDh\xb3&%F\x1f"\xfa\xc3\x83\x0cB\xcb\xf1\xa20PT\xc2\xaay\xd8\xd9\xc3\xd9\x05\xd6\x865\xc5\x0c\x87z\xd3\xbd\xf1\xe6\xc7?=\xbb/\xcf\x95\x90`\xbe%Zm\xbf\xd9.\x1b1y\x1a1}m\xcdYZ\xd8'


key = """-----BEGIN RSA PRIVATE KEY-----
\nMIIEowIBAAKCAQEAseI0Lcsp/XCteq+F5Qqq6n6MGcwc9r7FBfnYw9eprIJGvWaa\nnmiRte7JQhMh1STTOG9Eo0/q30hw6vufm2EAF1JbLizs4catWSd8INbhG7W8eFBY\nOuCqRELqviSJLlt4cXABn6UAuVqYbUKUXQk1P/B+vJ3TLRE/0IVo1Fp9R2dLPIC0\nvM5wV6xzhNfpqQfTnCvCVxwkK7ze4j1iVGjv/alp4Jfx3FAuGkHlm0abiaKQietf\n/beIExszjWwckPoWAs8qeuKDANg8l8l1NHyCgFnnmmNfDsF/aOVKX/9An3j2un5e\n8uhwx8VgVrhU8UqVsz0HoxBCOkaoTOqLCbS93wIDAQABAoIBAEMbwCywk2hSXJhG\n5MAqnJ133XoUB69M/D6LaixETfZPdcmZjmaJs8ML0XC0kBR93pPRYncsPMM87KCy\nCh5P431o7A5JE5r/3cEfRNSMzIMsNmy7fvXDcWjsR+wxE3HiP1eodmxYjyPeWlgK\nALfys9yp6d5VumgrtEQCOLC4bMAFRJGh7hi4rVf8xRjJUKyF1AAoCepqGfOU2vWZ\noALUmCiyTmOLvUAD8Avo/W/XgGsgub8u8VaP7liRwEKjqZZiF734LMzjPuokr8Mk\nLPmd+m6o+QM9HT3VGLEZVuvL3UT6gEOkSXraTm4V8Q2BvECRZ5wvKdxR66VFIBkO\nm0a+C/UCgYEAthvl4TaeOIV62/25eoevrpIZK4CmGPHo3k7zuvqVa8PDVzJA7h30\nutRIb9gf0baUZoHGqC69vtdwqBYeZIC5ILhO127LdSWZBUiKKODQmlO3XDaHqieB\n+JFMlqR0Kho1H3hCw8qofV9OwXjocXJL4p+/Btf4b4D43PrCRH394aMCgYEA+g9o\nGWG5OmB33+r9g35HDMEDf1L1ao3hKsTOKhO6Vd9+A2usdsZn1Uluri2qMIkpauAU\n2aFPtJJK88o4VItoo5NnxaP+ntiYYaI8bHaDd+3lLoRKiDCOjzDT7BKyLeA5FepD\ni+Irl3rzslp48/NmN83w3FYykB594UpaeAOYjpUCgYEAhKw6hCOIjeEhKxjkglJM\nOcCSudDWMaI8Z4nZo8VgCszqiaJBD7mfTGXQCDvKoryDzVKK6ohzEJBgsPS8W7g0\nJ5RfTDCZ5dTocKLylOmE0IphMbtAh0SVOgSRacaSIwJI5Y52BbKlogFHnUh6//un\nMYn0YAYEJygtJsFBuyiXSEUCgYApCkZHhCZmUlbaRTL+VcdLbJIqX28v4cFGx64e\nccZvOZLw9McFZ2K7OqYTqCL6fEhz5fsGDNeMB0aN5G6CUa8GybaKVXQAlgPMYlgQ\nZRMGp+CpVcT1vSJoldbyM89SgC5eTmhvmNsWrXM5nmejghsQpZgWUX9S7+4w/4cB\nk3WCUQKBgEO9hPOMz1JaINSRuKQvfHTTO2DuHbKzT6n3Z6z6xk1Xgc/EvB9N7e99\n61g/ZY0Cdyp6qb6D9ISBb/bTVW0UqUfNmo+UnQHptPA8z1rD4Y6dd1pdblNejen3\nm4Ve1029yzDgNT5PVm14I4iV1u/GPb97DF0l1BoZxm2q4pHW+eNa\n-----END RSA PRIVATE KEY-----""".encode()

decrypted_text = decryption(key.decode("utf-8"), data)
print(decrypted_text.decode())
