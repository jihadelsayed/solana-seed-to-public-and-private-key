import solana
from solders.keypair import Keypair
from solders.pubkey import Pubkey
import json

# Function to get the public key from a Keypair
def get_public_key_from_keypair():
    keypair = Keypair()
    public_key = keypair.pubkey()  # Using the method pubkey() instead of the attribute public_key
    print(f"Public Key: {public_key}")
    return public_key

# Function to derive a public key from a seed phrase
def get_public_key_from_seed(seed_phrase):
    seed = seed_phrase.encode('utf-8')
    keypair = Keypair.from_seed(seed[:32])
    public_key = keypair.pubkey()  # Using the method pubkey() instead of the attribute public_key
    print(f"Derived Public Key: {public_key}")
    return public_key

# Prompt the user for their seed phrase
seed_phrase = input("Please enter your seed phrase: ")

# Get and print public keys
public_key = get_public_key_from_keypair()
derived_public_key = get_public_key_from_seed(seed_phrase)

# Save the derived public key to a JSON file
wallet_json = {
    "pubkey": str(derived_public_key)
}

with open('my-solana-wallet.json', 'w') as json_file:
    json.dump(wallet_json, json_file)

print("Wallet JSON file 'my-solana-wallet.json' created.")
