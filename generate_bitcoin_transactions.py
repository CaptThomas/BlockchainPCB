import pandas as pd
import random
import string
import csv


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
    project_data = [
        {
            "prompt": "Temperature Controller",
            "component_list": "Temperature Sensor, Microcontroller, Heater, Display",
        },
        {
            "prompt": "LED Matrix Display",
            "component_list": "LED Matrix, Driver IC, Microcontroller, Power Supply",
        },
        {
            "prompt": "Motion Detection System",
            "component_list": "PIR Sensor, Microcontroller, Relay Module, Alarm",
        },
        {
            "prompt": "Smart Home Automation",
            "component_list": "Smart Hub, Sensors, Actuators, Communication Modules",
        },
        {
            "prompt": "GPS Tracking Device",
            "component_list": "GPS Module, Microcontroller, GSM Module, Power Management",
        },
        {
            "prompt": "Robot Arm",
            "component_list": "Servo Motors, Controller, Sensors, Gripper",
        },
        {
            "prompt": "Wireless Weather Station",
            "component_list": "Weather Sensors, Microcontroller, Wireless Transceiver, Display",
        },
        {
            "prompt": "Audio Amplifier",
            "component_list": "Audio IC, Power Amplifier, Capacitors, Speakers",
        },
        {
            "prompt": "Smart Irrigation System",
            "component_list": "Soil Moisture Sensor, Water Pump, Microcontroller, Valve",
        },
        {
            "prompt": "RFID Access Control",
            "component_list": "RFID Reader, Microcontroller, Electric Lock, Keypad",
        },
        {
            "prompt": "Home Security System",
            "component_list": "Security Cameras, Motion Sensors, Control Panel, Sirens",
        },
        {
            "prompt": "Smart Lighting System",
            "component_list": "LED Bulbs, Wireless Dimmer Switches, Gateway, Mobile App",
        },
        {
            "prompt": "Drone with Camera",
            "component_list": "Quadcopter Frame, Flight Controller, Camera, LiPo Battery",
        },
        {
            "prompt": "Biometric Attendance System",
            "component_list": "Fingerprint Scanner, Microcontroller, LCD Display, Ethernet Module",
        },
        {
            "prompt": "Solar Power Tracker",
            "component_list": "Solar Panels, Microcontroller, Motorized Actuators, Light Sensor",
        },
        # Add more project data as needed
    ]

    with open("pcb_projects.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["prompt", "component_list"])
        writer.writeheader()

        for i in range(num_projects):
            project = project_data[i % len(project_data)]
            writer.writerow(project)


# Generate bitcoin_transactions.csv with 100 transactions
generate_bitcoin_transactions_csv(100)

# Generate pcb_projects.csv with 50 projects
generate_pcb_projects_csv(50)
