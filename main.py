import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

from block import Blockchain
from block import Block
from generate_bitcoin_transactions import (
    generate_bitcoin_transactions_csv,
    generate_pcb_projects_csv,
)


# Generate Transaction Validation Model
def generate_transaction_validator_model():
    # Load bitcoin transactions dataset
    bitcoin_transactions = pd.read_csv("bitcoin_transactions.csv")

    # Preprocess the data and split into features and labels
    features = bitcoin_transactions[["transaction_id"]]
    labels = bitcoin_transactions["validity"]

    # One-hot encode the categorical features
    encoder = OneHotEncoder(sparse=False)
    features_encoded = encoder.fit_transform(features)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        features_encoded, labels, test_size=0.2, random_state=42
    )

    # Initialize and train the logistic regression model
    transaction_validator_model = LogisticRegression()
    transaction_validator_model.fit(X_train, y_train)

    # Save the trained model
    joblib.dump(transaction_validator_model, "transaction_validator_model.pkl")

    print("Transaction Validation Model generated successfully.")


# Generate Component List Generation Model
def generate_component_list_generator_model():
    # Load PCB projects dataset
    pcb_projects = pd.read_csv("pcb_projects.csv")

    # Preprocess the data and split into features and target (component list)
    features = pcb_projects["prompt"].values.reshape(-1, 1)
    component_lists = pcb_projects["component_list"].values

    # Encode the prompt strings into numerical values
    label_encoder = LabelEncoder()
    encoded_features = label_encoder.fit_transform(features.flatten())

    # Create and fit the component list generator model
    component_list_generator_model = RandomForestClassifier()
    component_list_generator_model.fit(encoded_features.reshape(-1, 1), component_lists)

    # Dump the component list generator model to a pickle file
    joblib.dump(component_list_generator_model, "component_list_generator_model.pkl")
    print("Component List Generator Model saved successfully.")


# Generate the machine learning models if they don't exist
try:
    transaction_validator_model = joblib.load("transaction_validator_model.pkl")
    component_list_generator_model = joblib.load("component_list_generator_model.pkl")
except FileNotFoundError:
    generate_transaction_validator_model()
    generate_component_list_generator_model()
    transaction_validator_model = joblib.load("transaction_validator_model.pkl")
    component_list_generator_model = joblib.load("component_list_generator_model.pkl")


# Create a new blockchain instance
blockchain = Blockchain()
generate_bitcoin_transactions_csv(100)
generate_pcb_projects_csv(50)
# Load PCB projects dataset
pcb_projects = pd.read_csv("pcb_projects.csv")

# Iterate over the PCB projects and add them to the blockchain
for _, project in pcb_projects.iterrows():
    prompt = project["prompt"]
    previous_block = blockchain.get_previous_block()
    is_valid = transaction_validator_model.predict([[prompt, previous_block]])[0]

    if is_valid:
        component_list = component_list_generator_model.predict([[prompt]])[0]
        blockchain.add_transaction(prompt, component_list)

# Mine a new block to include the validated transactions
blockchain.mine_block()

# Display the updated blockchain
blockchain.display_chain()
