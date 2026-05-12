# Vehicle Crypto Console

A simple Python console app for vehicle registration and hashing operations.

## Input values

- Generate SHA-256 Hash
- Digital Signature
- Register Vehicle: Accept Number Plate, Owner Name, and Model.
- Retrieve Vehicle: Display vehicle details.
- If the number plate is not found, a suitable error message is shown.

## Usage

Run the script from the repository folder:

```bash
python3 "import hashlib.py"
```

## Sample output

```
===== VEHICLE & CRYPTO SYSTEM =====
1. Generate SHA-256 Hash
2. Digital Signature
3. Register Vehicle
4. Retrieve Vehicle
5. Exit
Enter your choice: 3
Enter Number Plate: DL01A2345
Enter Owner Name: SURAJ
Enter Vehicle Model: HERO HONDA
Vehicle registered successfully!

===== VEHICLE & CRYPTO SYSTEM =====
1. Generate SHA-256 Hash
2. Digital Signature
3. Register Vehicle
4. Retrieve Vehicle
5. Exit
Enter your choice: 4
Enter Number Plate to Search: DL01A2345

Vehicle Found
Number Plate: DL01A2345
Owner: SURAJ
Model: HERO HONDA

===== VEHICLE & CRYPTO SYSTEM =====
1. Generate SHA-256 Hash
2. Digital Signature
3. Register Vehicle
4. Retrieve Vehicle
5. Exit
Enter your choice: 4
Enter Number Plate to Search: WB38A4567
Vehicle not found.

===== VEHICLE & CRYPTO SYSTEM =====
1. Generate SHA-256 Hash
2. Digital Signature
3. Register Vehicle
4. Retrieve Vehicle
5. Exit
Enter your choice: Enter text to hash: SHA-256 Hash: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

===== VEHICLE & CRYPTO SYSTEM =====
1. Generate SHA-256 Hash
2. Digital Signature
3. Register Vehicle
4. Retrieve Vehicle
5. Exit
Enter your choice: Exiting application...
```

## Notes

- The file is named `import hashlib.py` in this repo, so the command includes quotes to handle the space.
- Option `1` generates a SHA-256 hash from the entered text.
