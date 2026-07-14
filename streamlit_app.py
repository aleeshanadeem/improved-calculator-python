import streamlit as st

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Smart Calculator",
    page_icon="🧮",
    layout="centered"
)



# ----------------------------
# Title
# ----------------------------
st.title("🧮 Smart Calculator")

st.caption("Fast • Accurate • Modern")

st.divider()

# ----------------------------
# Inputs
# ----------------------------
num1 = st.number_input("First Number", value=0.0)

operator = st.selectbox(
    "Choose Operator",
    ["+", "-", "*", "/", "//", "%", "**"]
)

num2 = st.number_input("Second Number", value=0.0)

# ----------------------------
# Button
# ----------------------------
if st.button("🚀 Calculate"):

    valid = True

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("❌ Division by zero is not allowed.")
            valid = False

    elif operator == "//":
        if num2 != 0:
            result = num1 // num2
        else:
            st.error("❌ Division by zero is not allowed.")
            valid = False

    elif operator == "%":
        if num2 != 0:
            result = num1 % num2
        else:
            st.error("❌ Division by zero is not allowed.")
            valid = False

    elif operator == "**":
        result = num1 ** num2

    else:
        st.error("❌ Invalid Operator")
        valid = False

    if valid:

        st.success(f"### {num1} {operator} {num2} = {result}")

        if result > 0:
            st.success("🟢 Positive Result")

        elif result < 0:
            st.warning("🟠 Negative Result")

        else:
            st.info("⚪ Zero Result")

# ----------------------------
# Footer
# ----------------------------
st.divider()

st.markdown(
"""
<div class="footer">
<b>Aleesha Nadeem | 2(AN)K</b>
</div>
""",
unsafe_allow_html=True
)
