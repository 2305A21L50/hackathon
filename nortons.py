import streamlit as st

def compute_nortons(In, Rn, Rl):
    Il = In * (Rn / (Rn + Rl))  # Load current
    Pn = Il**2 * Rl  # Power delivered to load
    return Il, Pn

st.title("Norton's Theorem")

tab1, tab2 = st.tabs(["Compute", "Explain"])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            In = st.number_input("Enter Norton Current (In)", value=2.0)
            Rn = st.number_input("Enter Norton Resistance (Rn)", value=5.0)
            Rl = st.number_input("Enter Load Resistance (Rl)", value=2.5)

    with col2:
        with st.container(border=True):
            Il, Pn = compute_nortons(In, Rn, Rl)
            st.write("Norton's Theorem Results:")
            st.write(f"Load Current (Il) = {Il:.2f} A")
            st.write(f"Load Power (Pn) = {Pn:.2f} W")

with tab2:
    st.write("Norton's Theorem Equations:")
    st.latex(r'''I_L = I_N \times \frac{R_N}{R_N + R_L}''')
    st.latex(r'''P_N = I_L^2 \times R_L''')