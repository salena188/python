# Menu Driven Program for Repository Links

while True:
    print("\n----- Repository Menu -----")
    print("1. BMI Calculator")
    print("2. Taxation System")
    print("3. Currency COnverter")
    print("4. Remittance")
    print("5. Lagani Kosh")
    print("6. Invalid")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        print("BMI Calculator link: https://github.com/bidhyabhattarai/BMI_calculator")

    elif choice == 2:
        print("Taxation System link: https://github.com/Anujakhatri/Taxation-system-nepal")

    elif choice == 3:
        print("Currency COnverter link: https://github.com/sneharitas/currency_converter")

    elif choice == 4:
        print("Remittance link: https://github.com/binisha77/nepal_remittance_calculator")

    elif choice == 5:
        print("Lagani Kosh link: https://github.com/kopiladevkota/nepal_lagani_kosh")

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please select 1-6.")