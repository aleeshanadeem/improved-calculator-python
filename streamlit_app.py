import streamlit as st

st.set_page_config(
    page_title="Smart Calculator",
    page_icon="🧮",
    layout="centered"
)

st.markdown("""
<style>

.main{
    background-color:#0f172a;
}

.title{
text-align:center;
font-size:45px;
font-weight:bold;
color:#00E5FF;
}

.subtitle{
text-align:center;
font-size:18px;
color:white;
}

.footer{
text-align:center;
font-size:16px;
color:gray;
margin-top:40px;
}

.result{
background:#1e293b;
padding:20px;
border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">🧮 Smart Calculator</p>', unsafe_allow_html=True)

st.markdown(
"""
<p class="subtitle">
Developed by <b>Aleesha Nadeem</b><br>
🚀 <b>2(AN)K</b>
</p>
""",
unsafe_allow_html=True
)

st.divider()

num1 = st.number_input("First Number", value=0.0)

operator = st.selectbox(
    "Operator",
    ["+", "-", "*", "/", "//", "%", "**"]
)

num2 = st.number_input("Second Number", value=0.0)

if st.button("🚀 Calculate", use_container_width=True):

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

    if valid:

        st.success(f"{num1} {operator} {num2} = {result}")

        if result > 0:
            st.info("🟢 Positive Result")

        elif result < 0:
            st.warning("🟠 Negative Result")

        else:
            st.error("⚪ Zero Result")

st.divider()

st.markdown(
"""
<div class="footer">

Made with ❤️ using Streamlit

<b>Aleesha Nadeem | 2(AN)K</b>

</div>
""",
unsafe_allow_html=True
)
