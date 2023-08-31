x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def main():

    p = 7493025776465062819629921475535241674460826792785520881387158343265274170009282504884941039852933109163193651830303308312 # change this
    q = 7493025776465062819629921475535241674460826792785520881387158343265274170009282504884941039852933109163193651830303308312 # change this
    e = 7493025776465062819629921475535241674460826792785520881387158343265274170009282504884941039852933109163193651830303308312 # change this
    ct = put you cipher text here

    # compute n
    n = p * q

    # Compute phi(n)
    phi = (p - 1) * (q - 1)

    # Compute modular inverse of e
    gcd, a, b = egcd(e, phi)
    d = a

    print( "n:  " + str(d) );

    # Decrypt ciphertext
    pt = pow(ct, d, n)
    print( "pt: " + str(pt) )
    f"{pt:x}"
    flag =  bytes.fromhex(f"{pt:x}").decode()
    print( "flag: " + str(flag) )

if __name__ == "__main__":
    main()
