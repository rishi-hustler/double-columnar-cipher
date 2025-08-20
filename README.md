# Double Columnar Transposition Cipher 

## Overview

This project implements a **menu-driven Double Columnar Transposition Cipher** using Python.
The cipher applies the Columnar Transposition technique **twice using two different keys**, significantly increasing complexity compared to the single columnar cipher.

This project is designed to demonstrate **stronger classical cryptographic techniques** and how multiple encryption rounds improve security.

---

## Objectives

* Understand multi-stage transposition ciphers
* Learn how multiple keys improve encryption strength
* Implement layered encryption and decryption logic
* Practice matrix-based cryptographic techniques
* Develop menu-driven cybersecurity programs in Python

---

## Features

* Encrypt plaintext using Double Columnar Transposition
* Decrypt ciphertext using two keys
* Two independent keyword-based keys
* Automatic padding handling
* Menu-driven command-line interface
* Input validation for encryption keys

---

## Technologies Used

* Programming Language: Python 3
* Standard Libraries:

  * `math`

No external dependencies are required.

---

## Project Structure

```
Double-Columnar-Transposition-Cipher/
│
├── double_columnar_cipher.py
├── README.md
└── sample.txt (optional)
```

---

## How Double Columnar Transposition Cipher Works

1. Remove spaces from the plaintext
2. Apply single columnar transposition using the first key
3. Apply columnar transposition again on the result using the second key
4. Use padding characters to fill incomplete matrix cells
5. Reverse the process during decryption using keys in reverse order

---

## How to Run the Program

### Step 1: Verify Python Installation

```
python --version
```

### Step 2: Run the Program

```
python double_columnar_cipher.py
```

---

## Menu Options Explained

1. **Encrypt text**
   Encrypts user-provided plaintext using two keywords sequentially.

2. **Decrypt text**
   Decrypts ciphertext using the same two keywords in reverse order.

3. **Exit**
   Safely terminates the program.

---

## Example

Plaintext:

```
HELLO WORLD
```

Key 1:

```
KEY
```

Key 2:

```
LOCK
```

Ciphertext:

```
LHORLWXEDOXL
```

(Note: Output may vary due to padding.)

---

## Security Analysis

* Double Columnar Transposition is a **symmetric key cipher**
* More resistant to attacks than single columnar transposition
* Preserves letter frequency but disrupts positional patterns
* Still vulnerable to advanced cryptanalysis methods
* Not secure for modern cryptographic needs

---

## Limitations

* Padding characters may remain after decryption
* Manual key management required
* Not suitable for real-world secure communication

---

## Future Enhancements

* Implement triple columnar transposition
* Combine with substitution ciphers for hybrid encryption
* Add brute-force attack demonstration
* Add file-based encryption support
* Integrate with other classical cipher techniques


