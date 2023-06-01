import pandas as pd
import random
import string

def generate_bitcoin_transactions_csv(num_transactions):
    prompts = []
    previous_hashes = []
    components = []
    validity = []

    for _ in range(num_transactions):
        prompt = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        previous_hash = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        component_list = random.sample(range(100), k=random.randint(1, 10))
        valid = random.choice([True, False])

        prompts.append(prompt)
        previous_hashes.append(previous_hash)
        components.append(component_list)
        validity.append(valid)

    data = {
        'prompt': prompts,
        'previous_block_hash': previous_hashes,
        'components': components,
        'validity': validity
    }

    df = pd.DataFrame(data)
    df.to_csv('bitcoin_transactions.csv', index=False)
    print("bitcoin_transactions.csv generated successfully.")


# Generate bitcoin_transactions.csv with 100 transactions
generate_bitcoin_transactions_csv(100)
