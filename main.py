from block import Blockchain
from block import Block
from transaction import transaction
from component import component
# Load the saved machine learning models
transaction()
component()
transaction_validator_model = load_model('transaction_validator_model.pkl')
component_list_generator_model = load_model('component_list_generator_model.pkl')

# Create a new blockchain instance
blockchain = Blockchain()

# Load historical Bitcoin transactions dataset
bitcoin_transactions = pd.read_csv('bitcoin_transactions.csv')

# Iterate over the transactions and add them to the blockchain
for _, transaction in bitcoin_transactions.iterrows():
    prompt = transaction['prompt']
    previous_block = blockchain.get_previous_block()
    components = transaction['components']
    is_valid = validate_transaction(prompt, components, previous_block)
    
    if is_valid:
        component_list = generate_component_list(prompt)
        blockchain.add_transaction(prompt, component_list)
        
# Mine a new block to include the validated transactions
blockchain.mine_block()

# Display the updated blockchain
blockchain.display_chain()
