import streamlit as st
st.title("🚜 FarmGrid: Resource Owner Portal")
st.sidebar.markdown("### Role: Resource Owner")
tool = st.text_input("Machine Name (e.g. Tractor, Tiller):")
price = st.number_input("Rental Price per Hour (₹):", min_value=1)
if st.button("List My Equipment"):
    st.success(f"Successfully listed {tool} for ₹{price}/hr!")
