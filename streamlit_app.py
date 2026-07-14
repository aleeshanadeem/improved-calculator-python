import streamlit as st

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Smart Calculator",
    page_icon="🧮",
    layout="centered"
)
with st.sidebar:
    st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;">
        <p style="margin:0;font-size:13px;color:gray;">
            Developed by
        </p>
        <h3 style="margin:5px 0;">
            Aleesha Nadeem
        </h3>
        <p style="margin:0;font-size:18px;color:#ff9800;font-weight:bold;">
             2(AN)K
        </p>
    </div>
    """, unsafe_allow_html=True)

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

