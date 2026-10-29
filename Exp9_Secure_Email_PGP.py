import subprocess
import os


def run_command(command):
    try:
        subprocess.run(command, check=True)
        print("Operation completed successfully.")
    except subprocess.CalledProcessError:
        print("Operation failed. Check the key, email, or file.")


while True:
    print("\n--- Secure Email Using PGP ---")
    print("1. Create Email Message")
    print("2. Encrypt Email")
    print("3. Decrypt Email")
    print("4. Sign Email")
    print("5. Verify Signature")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        message = input("Enter your email message: ")
        with open("email.txt", "w") as file:
            file.write(message)
        print("Email message saved in email.txt")

    elif choice == "2":
        recipient = input("Enter recipient email: ")
        run_command([
            "gpg", "--armor", "--output", "email_encrypted.asc",
            "--encrypt", "--recipient", recipient, "email.txt"
        ])

    elif choice == "3":
        run_command([
            "gpg", "--output", "email_decrypted.txt",
            "--decrypt", "email_encrypted.asc"
        ])
        if os.path.exists("email_decrypted.txt"):
            with open("email_decrypted.txt", "r") as file:
                print("Decrypted message:", file.read())

    elif choice == "4":
        run_command([
            "gpg", "--armor", "--output", "email_signature.asc",
            "--detach-sign", "email.txt"
        ])

    elif choice == "5":
        run_command([
            "gpg", "--verify", "email_signature.asc", "email.txt"
        ])

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
