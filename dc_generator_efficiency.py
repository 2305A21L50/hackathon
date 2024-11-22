import streamlit as st


def Gen_Eff(V, CL, IL,Rsh, Ra):
    Ish = V / Rsh
    Ia = 1* IL - Ish
    CUL =( Ish**2) * Rsh +( Ia**2) * Ra
    Eff = ((1* V * IL) / (1* V * IL + CL + CUL))
    return Eff, CUL


st.title("2305A21L50-PS9")
st.text("DC Shunt Generator Efficiency Calculator")

co1,col2=st.columns(2)
with co1:

    V = st.number_input("Enter Voltage (V)", min_value=0.0, step=0.1)
    IL = st.number_input("Enter Full Load Current (IL) in Amps", min_value=0.0, step=0.1)
    Rsh = st.number_input("Enter Shunt Field Resistance (Rsh) in Ohms", min_value=0.0, step=0.1)
    Ra = st.number_input("Enter Armature Resistance (Ra) in Ohms", min_value=0.0, step=0.1)
    CL = st.number_input("Enter Core Losses (CL) in Watts", min_value=0.0, step=0.1)
    cl = st.number_input("(CL) in Watts", min_value=0.0, step=0.1)
    
    cal=st.button("Calculate Efficiency")


with col2:
    if cal:
        Eff, CUL = Gen_Eff(V, CL, IL, Rsh, Ra)
        
        
        st.subheader("Results:")
        st.write(f"Efficiency of the Generator: {Eff * 100:.2f}%")
        st.write(f"Cumulative Losses (CUL): {CUL:.2f} Watts")