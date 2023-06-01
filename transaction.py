import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
def transaction():
    # Load historical Bitcoin transaction data
    bitcoin_transactions = pd.read_csv('bitcoin_transactions.csv')

    # Preprocess the data and split into features and labels
    features = bitcoin_transactions[['prompt', 'previous_block_hash']]
    labels = bitcoin_transactions['validity']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    # Initialize and train the logistic regression model
    transaction_validator_model = LogisticRegression()
    transaction_validator_model.fit(X_train, y_train)

    # Evaluate the model on the testing set
    accuracy = transaction_validator_model.score(X_test, y_test)
    print("Transaction Validation Model Accuracy:", accuracy)

    # Save the trained model for later use in the `validate_transaction()` function
    transaction_validator_model.save('transaction_validator_model.pkl')
