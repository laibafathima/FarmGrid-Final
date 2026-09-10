import streamlit as st
st.title("🌾 FarmGrid: Farmer Portal")
st.sidebar.markdown("### Role: Farmer")
crop = st.text_input("Enter Crop Requirement:")
if st.button("Submit Request"):
    st.success(f"Requested {crop} successfully!")
st.info("🚜 Available Rentals: John Deere Tractor (₹500/hr)")
