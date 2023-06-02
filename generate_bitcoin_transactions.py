import pandas as pd
import random
import string


def generate_bitcoin_transactions_csv(num_transactions):
    prompts = []
    validities = []

    for _ in range(num_transactions):
        prompt = "".join(random.choices(string.ascii_letters + string.digits, k=10))
        validity = random.choice([True, False])

        prompts.append(prompt)
        validities.append(validity)

    data = {
        "transaction_id": ["tx{}".format(i + 1) for i in range(num_transactions)],
        "validity": validities,
    }

    df = pd.DataFrame(data)
    df.to_csv("bitcoin_transactions.csv", index=False)
    print("bitcoin_transactions.csv generated successfully.")


def generate_pcb_projects_csv(num_projects):
    project_ids = []
    prompts = []
    components = []

    for i in range(num_projects):
        project_id = "project{}".format(i + 1)
        prompt = "Prompt {}".format(i + 1)
        component_list = [f"Component {j}" for j in range(random.randint(1, 10))]

        project_ids.append(project_id)
        prompts.append(prompt)
        components.append(",".join(component_list))

    data = {"project_id": project_ids, "prompt": prompts, "components": components}

    df = pd.DataFrame(data)
    df.to_csv("pcb_projects.csv", index=False)
    print("pcb_projects.csv generated successfully.")


# Generate bitcoin_transactions.csv with 100 transactions
generate_bitcoin_transactions_csv(100)

# Generate pcb_projects.csv with 50 projects
generate_pcb_projects_csv(50)
