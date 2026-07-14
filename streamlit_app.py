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
# Custom CSS
# ----------------------------
st.markdown("""
<style>

h1{
    text-align:center;
    color:#00E5FF;
    font-size:50px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}

.stButton>button{
    width:100%;
    height:55px;
    border-radius:10px;
    font-size:22px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:

    st.title("👩‍💻 Developer")

    st.markdown("## Aleesha Nadeem")

    st.markdown("### 🚀 2(AN)K")

    st.divider()

    st.info(
        """
        **Smart Calculator**

        Built with ❤️ using Python & Streamlit.
        """
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
Made with ❤️ using Streamlit<br><br>
<b>Aleesha Nadeem | 2(AN)K</b>
</div>
""",
unsafe_allow_html=True
)
