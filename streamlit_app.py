import streamlit as st

st.set_page_config(page_title="Improved Calculator", page_icon="🧮")

st.title("🧮 AlgoZee Academy Improved Calculator")

# Inputs
first_number = st.number_input("Enter First Number", value=0.0)

operator = st.selectbox(
    "Select Operator",
    ["+", "-", "*", "/", "//", "%", "**"]
)

second_number = st.number_input("Enter Second Number", value=0.0)

# Button
if st.button("Calculate"):

    valid_result = True

    if operator == "+":
        result = first_number + second_number

    elif operator == "-":
        result = first_number - second_number

    elif operator == "*":
        result = first_number * second_number

    elif operator == "/":
        if second_number != 0:
            result = first_number / second_number
        else:
            st.error("Division by zero is not allowed.")
            valid_result = False

    elif operator == "//":
        if second_number != 0:
            result = first_number // second_number
        else:
            st.error("Division by zero is not allowed.")
            valid_result = False

    elif operator == "%":
        if second_number != 0:
            result = first_number % second_number
        else:
            st.error("Division by zero is not allowed.")
            valid_result = False

    elif operator == "**":
        result = first_number ** second_number

    else:
        st.error("Invalid Operator")
        valid_result = False

    if valid_result:
        st.success(f"{first_number} {operator} {second_number} = {result}")

        if result > 0:
            st.info("🟢 Positive Result")

        elif result < 0:
            st.warning("🟠 Negative Result")

        else:
            st.write("⚪ Zero Result")
