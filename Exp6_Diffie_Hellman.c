#include <stdio.h>

long long powerMod(long long base, long long exponent, long long mod)
{
    long long result = 1;

    while (exponent > 0)
    {
        result = (result * base) % mod;
        exponent--;
    }

    return result;
}

int main()
{
    long long p, g;
    long long privateA, privateB;
    long long publicA, publicB;
    long long secretA, secretB;

    printf("Enter a prime number (p): ");
    scanf("%lld", &p);

    printf("Enter a primitive root (g): ");
    scanf("%lld", &g);

    printf("Enter private key of User A: ");
    scanf("%lld", &privateA);

    printf("Enter private key of User B: ");
    scanf("%lld", &privateB);

    publicA = powerMod(g, privateA, p);
    publicB = powerMod(g, privateB, p);

    printf("\nPublic key of User A = %lld", publicA);
    printf("\nPublic key of User B = %lld", publicB);

    secretA = powerMod(publicB, privateA, p);
    secretB = powerMod(publicA, privateB, p);

    printf("\n\nShared secret key calculated by User A = %lld", secretA);
    printf("\nShared secret key calculated by User B = %lld", secretB);

    if (secretA == secretB)
        printf("\n\nKey Exchange Successful!");
    else
        printf("\n\nKey Exchange Failed!");

    return 0;
}
