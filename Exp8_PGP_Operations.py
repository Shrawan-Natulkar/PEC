import subprocess
import os


def run_command(command):
    result = subprocess.run(command)
    if result.returncode == 0:
        print("\nOperation completed successfully.")
    else:
        print("\nOperation failed. Check the command and GnuPG setup.")


while True:
    print("\n--- PGP Operations ---")
    print("1. Check GnuPG")
    print("2. Generate Key Pair")
    print("3. Export Public Key")
    print("4. Import Public Key")
    print("5. Encrypt File")
    print("6. Decrypt File")
    print("7. Sign File")
    print("8. Verify Signature")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        run_command(["gpg", "--version"])

    elif choice == "2":
        run_command(["gpg", "--full-generate-key"])

    elif choice == "3":
        email = input("Enter your email: ")
        filename = input("Output file (e.g. public.asc): ")
        run_command([
            "gpg", "--armor", "--output", filename,
            "--export", email
        ])

    elif choice == "4":
        filename = input("Enter public key file: ")
        run_command(["gpg", "--import", filename])

    elif choice == "5":
        filename = input("Enter file to encrypt: ")
        email = input("Enter recipient email: ")
        output = filename + ".gpg"
        run_command([
            "gpg", "--output", output, "--encrypt",
            "--recipient", email, filename
        ])

    elif choice == "6":
        filename = input("Enter encrypted file: ")
        output = input("Enter decrypted output filename: ")
        run_command([
            "gpg", "--output", output, "--decrypt", filename
        ])

    elif choice == "7":
        filename = input("Enter file to sign: ")
        output = filename + ".sig"
        run_command([
            "gpg", "--detach-sign", "--output", output, filename
        ])

    elif choice == "8":
        signature = input("Enter signature file: ")
        filename = input("Enter original file: ")
        run_command(["gpg", "--verify", signature, filename])

    elif choice == "9":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")
