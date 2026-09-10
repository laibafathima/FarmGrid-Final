import streamlit as st
st.title("👑 FarmGrid: Admin Dashboard")
st.sidebar.markdown("### Role: Admin")
st.metric(label="Total Farmers Registered", value="142")
st.metric(label="Active Machinery Rentals", value="18")
if st.button("Approve Pending Users"):
    st.success("All pending farmer profiles verified!")
