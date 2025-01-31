import os
import random
import string
import json
from termcolor import colored

def generate_unique_codes(length=3, count=63):
    """Generate unique random codes of a specified length."""
    codes = set()
    while len(codes) < count:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        codes.add(code)
    return list(codes)

def create_hash(word, mapping):
    """Encrypt the word using the provided mapping."""
    result = ""
    for letter in word:
        result += mapping.get(letter, letter) 
    return result

def crack_hash(encrypted_word, reverse_mapping, code_length=3):
    """Decrypt the encrypted word using the reverse mapping."""
    result = ""
    i = 0
    while i < len(encrypted_word):
        segment = encrypted_word[i:i+code_length]
        result += reverse_mapping.get(segment, segment)
        i += code_length
    return result

def load_mapping(file_path):
    """Load mapping from a file or create a new one if it does not exist."""
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        all_characters = string.ascii_letters + string.digits + ' ' 
        unique_codes = generate_unique_codes(length=3, count=63)  
        mapping = dict(zip(all_characters, unique_codes))
        reverse_mapping = {v: k for k, v in mapping.items()}
        with open(file_path, 'w') as file:
            json.dump({'mapping': mapping, 'reverse_mapping': reverse_mapping}, file)
        return {'mapping': mapping, 'reverse_mapping': reverse_mapping}


mappings = load_mapping('mappings.json')
mapping = mappings['mapping']
reverse_mapping = mappings['reverse_mapping']

while True:
    os.system('cls' if os.name == 'nt' else 'clear') 
    print(colored('''                                                                                                     
    ██╗  ██╗ █████╗ ███████╗██╗  ██╗      ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗     
    ██║  ██║██╔══██╗██╔════╝██║  ██║     ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    
    ███████║███████║███████╗███████║     ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝    
    ██╔══██║██╔══██║╚════██║██╔══██║     ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗    
    ██║  ██║██║  ██║███████║██║  ██║     ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║    
    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    
    \n    endChuva.github.io/Profile\n''', 'light_cyan'))
    print('―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――\n')
    print('   Choose your option: \n   [1]Create Hash   [2]Crack Hash')
    choseop = int(input('          '))

    if choseop == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('   "Create Hash" selected!\n')
        print('   Type your word to encrypt: ')
        word = input('          ')
        final = create_hash(word, mapping)
        print(f"   Encrypted word: {final}")
        input("\n   Press Enter to continue...")

    elif choseop == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('   "Crack Hash" selected!\n')
        print('   Type the encrypted word to decrypt: ')
        encrypted_word = input('          ')
        original_word = crack_hash(encrypted_word, reverse_mapping, code_length=3)
        print(f"   Decrypted word: {original_word}")
        input("\n   Press Enter to continue...")
