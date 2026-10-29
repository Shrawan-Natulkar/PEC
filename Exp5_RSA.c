#include <stdio.h>
#include <math.h>

int gcd(int a, int b)
{
    while (b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

long long powerMod(long long base, long long exp, long long mod)
{
    long long result = 1;

    while (exp > 0)
    {
        result = (result * base) % mod;
        exp--;
    }

    return result;
}

int main()
{
    int p, q, n, phi;
    int e, d;
    int message, encrypted, decrypted;

    printf("Enter first prime number (p): ");
    scanf("%d", &p);

    printf("Enter second prime number (q): ");
    scanf("%d", &q);

    n = p * q;
    phi = (p - 1) * (q - 1);

    for (e = 2; e < phi; e++)
    {
        if (gcd(e, phi) == 1)
            break;
    }

    d = 2;
    while ((d * e) % phi != 1)
    {
        d++;
    }

    printf("\nPublic Key : (%d, %d)", e, n);
    printf("\nPrivate Key : (%d, %d)", d, n);

    printf("\n\nEnter message (number less than %d): ", n);
    scanf("%d", &message);

    // Encryption: C = M^e mod n
    encrypted = powerMod(message, e, n);
    printf("Encrypted message = %d", encrypted);

    // Decryption: M = C^d mod n
    decrypted = powerMod(encrypted, d, n);
    printf("\nDecrypted message = %d\n", decrypted);

    return 0;
}
