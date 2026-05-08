import hashlib


vehicles = {}


def generate_sha256_hash():
    text = input("Enter text to hash: ").strip()
    if not text:
        print("Text cannot be empty.")
        return
    hash_object = hashlib.sha256(text.encode())
    print(f"SHA-256 Hash: {hash_object.hexdigest()}")


def digital_signature_system():
    # Placeholder for digital signature functionality
    print("Digital Signature System - Placeholder")
    message = input("Enter message to sign: ").strip()
    if not message:
        print("Message cannot be empty.")
        return
    signature = hashlib.sha256(message.encode()).hexdigest()
    print(f"Simulated Signature: {signature}")


def register_vehicle():
    number_plate = input("Enter Number Plate: ").strip().upper()
    if not number_plate:
        print("Number plate cannot be empty.")
        return

    if number_plate in vehicles:
        print("This number plate is already registered.")
        return

    owner = input("Enter Owner Name: ").strip()
    model = input("Enter Vehicle Model: ").strip()

    if not owner or not model:
        print("Owner name and model cannot be empty.")
        return

    vehicles[number_plate] = {
        "owner": owner,
        "model": model,
    }

    print("Vehicle registered successfully!")


def retrieve_vehicle():
    number_plate = input("Enter Number Plate to Search: ").strip().upper()

    if number_plate in vehicles:
        vehicle = vehicles[number_plate]

        print("\nVehicle Found")
        print(f"Number Plate: {number_plate}")
        print(f"Owner: {vehicle['owner']}")
        print(f"Model: {vehicle['model']}")

    else:
        print("Vehicle not found.")


def display_menu():
    print("\n===== VEHICLE & CRYPTO SYSTEM =====")
    print("1. Generate SHA-256 Hash")
    print("2. Digital Signature")
    print("3. Register Vehicle")
    print("4. Retrieve Vehicle")
    print("5. Exit")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            generate_sha256_hash()

        elif choice == "2":
            digital_signature_system()

        elif choice == "3":
            register_vehicle()

        elif choice == "4":
            retrieve_vehicle()

        elif choice == "5":
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()