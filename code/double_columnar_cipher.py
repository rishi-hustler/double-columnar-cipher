import math
# BY RISHI HUSTLER

def get_key_order(key):
    """
    Returns column order based on alphabetical order of the key
    """
    return sorted(list(enumerate(key.lower())), key=lambda x: x[1])


def single_columnar_encrypt(text, key):
    """
    Perform single columnar transposition encryption
    """
    text = text.replace(" ", "")
    key_len = len(key)
    rows = math.ceil(len(text) / key_len)

    matrix = [['X'] * key_len for _ in range(rows)]

    index = 0
    for r in range(rows):
        for c in range(key_len):
            if index < len(text):
                matrix[r][c] = text[index]
                index += 1

    key_order = get_key_order(key)

    cipher = ""
    for col_index, _ in key_order:
        for r in range(rows):
            cipher += matrix[r][col_index]

    return cipher


def single_columnar_decrypt(text, key):
    """
    Perform single columnar transposition decryption
    """
    key_len = len(key)
    rows = math.ceil(len(text) / key_len)

    matrix = [[''] * key_len for _ in range(rows)]
    key_order = get_key_order(key)

    index = 0
    for col_index, _ in key_order:
        for r in range(rows):
            if index < len(text):
                matrix[r][col_index] = text[index]
                index += 1

    plaintext = ""
    for r in range(rows):
        for c in range(key_len):
            plaintext += matrix[r][c]

    return plaintext.rstrip('X')


def double_columnar_encrypt(plaintext, key1, key2):
    """
    Apply columnar transposition twice
    """
    first_pass = single_columnar_encrypt(plaintext, key1)
    second_pass = single_columnar_encrypt(first_pass, key2)
    return second_pass


def double_columnar_decrypt(ciphertext, key1, key2):
    """
    Reverse double columnar transposition
    """
    first_pass = single_columnar_decrypt(ciphertext, key2)
    second_pass = single_columnar_decrypt(first_pass, key1)
    return second_pass


def display_menu():
    print("\n======== DOUBLE COLUMNAR TRANSPOSITION CIPHER ========")
    print("1. Encrypt text")
    print("2. Decrypt text")
    print("3. Exit")
    print("====================================================")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            plaintext = input("\nEnter plaintext: ")
            key1 = input("Enter first key: ")
            key2 = input("Enter second key: ")

            if not key1.isalpha() or not key2.isalpha():
                print("Keys must contain only alphabetic characters.")
                continue

            encrypted_text = double_columnar_encrypt(plaintext, key1, key2)
            print("Encrypted text:", encrypted_text)

        elif choice == "2":
            ciphertext = input("\nEnter ciphertext: ")
            key1 = input("Enter first key: ")
            key2 = input("Enter second key: ")

            if not key1.isalpha() or not key2.isalpha():
                print("Keys must contain only alphabetic characters.")
                continue

            decrypted_text = double_columnar_decrypt(ciphertext, key1, key2)
            print("Decrypted text:", decrypted_text)

        elif choice == "3":
            print("\nExiting Double Columnar Cipher program.")
            break

        else:
            print("Invalid choice. Please select between 1-3.")


if __name__ == "__main__":
    main()
