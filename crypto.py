import hashlib


def hash(msg):
    """
    read file and find the line contains 'X-DSPAM-Confidence: <value>'
    then split the line text with ':' and take the floating point number on it
    finally calculate the sum
    """
    print('MD5 hashing: %s' % msg)
    hash_object = hashlib.md5(msg.encode())
    print(hash_object.hexdigest())


if __name__ == "__main__":
    """
    Main method here,
        read input file from command line
        hash it
    """
    while True:
        print('--------------------------------------------------------------')
        msg = raw_input("Enter Message : ").strip()
        print('--------------------------------------------------------------')
        hash(msg)
