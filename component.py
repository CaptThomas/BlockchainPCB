import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
def component():
    # Load historical Bitcoin transaction data
    bitcoin_transactions = pd.read_csv('bitcoin_transactions.csv')

    # Preprocess the data and split into features and target (component list)
    features = bitcoin_transactions['prompt']
    target = bitcoin_transactions['component_list']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Initialize and train the random forest classifier model
    component_list_generator_model = RandomForestClassifier()
    component_list_generator_model.fit(X_train, y_train)

    # Evaluate the model on the testing set
    accuracy = component_list_generator_model.score(X_test, y_test)
    print("Component List Generation Model Accuracy:", accuracy)

    # Save the trained model for later use in the `generate_component_list()` function
    component_list_generator_model.save('component_list_generator_model.pkl')
