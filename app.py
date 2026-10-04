import streamlit as st
from bank import Bank   # put the class above in bank.py

bank = Bank()
Bank.load()

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Select Action",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Show Details",
        "Update Details",
        "Delete Account"
    ]
)

# -----------------------------------
if menu == "Create Account":
    st.subheader("Create New Account")

    name = st.text_input("Name")

    age = st.number_input("Age", min_value=0)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create Account"):
        success, result = bank.create_account(name, age, email, int(pin))
        if success:
            st.success("Account created successfully 🎉")
            st.json(result)
        else:
            st.error(result)

# -----------------------------------
elif menu == "Deposit Money":
    st.subheader("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1, max_value=10000)

    if st.button("Deposit"):
        user = bank.authenticate(acc, int(pin))
        if not user:
            st.error("Invalid credentials")
        else:
            user['balance'] += amount
            Bank.save()
            st.success("Amount deposited successfully")
            st.write("New Balance:", user['balance'])

# -----------------------------------
elif menu == "Withdraw Money":
    st.subheader("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        user = bank.authenticate(acc, int(pin))
        if not user:
            st.error("Invalid credentials")
        elif amount > user['balance']:
            st.error("Insufficient balance")
        else:
            user['balance'] -= amount
            Bank.save()
            st.success("Withdrawal successful")
            st.write("Remaining Balance:", user['balance'])

# -----------------------------------
elif menu == "Show Details":
    st.subheader("Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        user = bank.authenticate(acc, int(pin))
        if not user:
            st.error("Invalid credentials")
        else:
            st.json(user)

# -----------------------------------
elif menu == "Update Details":
    st.subheader("Update Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    user = bank.authenticate(acc, int(pin))
    if user:
        name = st.text_input("New Name", user['name'])
        email = st.text_input("New Email", user['email'])
        new_pin = st.text_input("New PIN", value=str(user['pin']))

        if st.button("Update"):
            user['name'] = name
            user['email'] = email
            user['pin'] = int(new_pin)
            Bank.save()
            st.success("Details updated successfully")

# -----------------------------------
elif menu == "Delete Account":
    st.subheader("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        user = bank.authenticate(acc, int(pin))
        if not user:
            st.error("Invalid credentials")
        else:
            Bank.data.remove(user)
            Bank.save()
            st.success("Account deleted successfully")
            
#  to run code, type this in terminal
# cd bank_management
# streamlit run app.py
