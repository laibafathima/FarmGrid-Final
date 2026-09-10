import streamlit as st

st.set_page_config(page_title="FarmGrid All-In-One", page_icon="🌾", layout="wide")

# Master Navigation Menu in the Sidebar
role = st.sidebar.selectbox("Select Your Portal View", ["Farmer Portal", "Resource Owner Portal", "Admin Dashboard"])

if role == "Farmer Portal":
    st.title("🌾 FarmGrid: Farmer Portal")
    st.write("Welcome to your digital farming assistant!")
    
    crop = st.text_input("Enter Crop Requirement:")
    if st.button("Submit Request"):
        st.success(f"Requested {crop} successfully!")
    st.info("🚜 Available Rentals: John Deere Tractor (₹500/hr)")

elif role == "Resource Owner Portal":
    st.title("🚜 FarmGrid: Resource Owner Portal")
    st.write("Manage and list your agricultural machinery.")
    
    tool = st.text_input("Machine Name (e.g. Tractor, Tiller):")
    price = st.number_input("Rental Price per Hour (₹):", min_value=1)
    if st.button("List My Equipment"):
        st.success(f"Successfully listed {tool} for ₹{price}/hr!")

elif role == "Admin Dashboard":
    st.title("👑 FarmGrid: Admin Dashboard")
    st.write("System metrics and approval logs.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Total Farmers Registered", value="142")
    with col2:
        st.metric(label="Active Machinery Rentals", value="18")
        
    if st.button("Approve Pending Users"):
        st.success("All pending farmer profiles verified!")
