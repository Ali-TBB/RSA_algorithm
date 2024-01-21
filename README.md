# RSA Decryption Function

This is a simple Python script that demonstrates RSA decryption for a given set of encrypted ASCII codes. The script includes functions for ASCII code encryption and decryption using a specific RSA public key.

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Example](#example)
- [License](#license)

## Overview

RSA (Rivest-Shamir-Adleman) is a widely used public-key cryptosystem that enables secure communication over an insecure channel. This script focuses on the decryption part, showcasing how to decrypt a message encrypted with a specific RSA public key.

The main functions in the script include:
- `encrypt_ascii_codes`: Simulates ASCII code encryption using a specified RSA public key.
- `decrypt_message`: Decrypts an encrypted message based on ASCII codes using the provided RSA public key.

## Usage

To use this script, follow these steps:

1. Clone the repository to your local machine.
2. Run the script using a Python interpreter.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Ali-TBB/RSA_algorithm.git
    ```

2. Navigate to the project directory:

    ```bash
    cd RSA_algorithm
    ```

## Example

```python
# Import the decryption functions
from rsa_decryption import encrypt_ascii_codes, decrypt_message

# Encrypted message to be decrypted
encrypted_message = [1730, 815, 1476, 1476, 1226, 1297, 8, 502, 1226, 1520, 1476, 2303, 900]

# Decrypt the message using the ASCII codes and print the result
decrypt_message(encrypt_ascii_codes(), encrypted_message)
