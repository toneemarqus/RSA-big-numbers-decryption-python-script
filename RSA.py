x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def main():

    p = p from debug.txt
    q = q from debug.txt
    e = e from debug.txt
    ct = c from output.txt

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
