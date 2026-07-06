password = input("Enter a password: ")

if len(password) >= 8:
    print("✅ Strong password length")
else:
    print("❌ Password is too short")