# Word Encryption with Custom Mapping

This project implements a simple word encryption system that allows users to create and decrypt words using a custom character-to-code mapping.

## Features

- **Create Hash**: Encrypts a word provided by the user using a character mapping.
- **Crack Hash**: Decrypts an encrypted word using the reverse mapping.

## Technologies Used

- Python
- `random` library
- `string` library
- `json` library
- `termcolor` library

## How It Works

1. **Custom Mapping**: The script generates unique 3-character codes that are mapped to letters, digits, and spaces. This mapping is saved in a JSON file (`mappings.json`) for future use.

2. **Encryption**: When a word is entered, each character is replaced with its corresponding 3-character code from the mapping.

3. **Decryption**: The encrypted word can be decrypted by reversing the process, using the reverse mapping stored in the JSON file.

## Setup and Usage

1. **Clone the repository**:
    ```bash
    git clone https://github.com/MatheusMrq/HashCracker.git
    cd HashCracker
    ```

2. **Install required libraries**:
    ```bash
    pip install termcolor
    ```

3. **Run the script**:
    ```bash
    python hashcracker
    ```

4. **Choose an option**:
    - `[1] Create Hash`: Encrypt a word.
    - `[2] Crack Hash`: Decrypt an encrypted word.

5. **Follow the on-screen instructions** to either encrypt or decrypt a word.

## Example

### Encrypting a Word
"Create Hash" selected! Type your word to encrypt: hello Encrypted word: X3g9k1


### Decrypting a Word
"Crack Hash" selected! Type the encrypted word to decrypt: X3g9k1 Decrypted word: hello


## Customization

- **Change Code Length**: You can modify the `code_length` parameter in the `generate_unique_codes` function to change the length of the codes used for encryption.
- **Add More Characters**: To support more characters in the encryption, adjust the `all_characters` string in the `load_mapping` function and increase the `count` parameter in `generate_unique_codes`.

## License

This project is FREE.
