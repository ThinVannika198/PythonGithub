import streamlit as st
import pandas as pd
import os

# --- DATABASE LOGIC ---
# This function saves your lists into a permanent CSV file



# 2. Print Function
if st.sidebar.button("🖨️ Print Invoice/Inventory"):
    # This triggers the browser's print window
    st.components.v1.html("<script>window.print();</script>", height=0)

# 3. Help/About
with st.sidebar.expander("About this App"):
    st.write("This is a Cloud Inventory System built for local business management.")

st.sidebar.markdown("---")
def save_data():
    df = pd.DataFrame({
        "Item": st.session_state.stuffs, 
        "Price": st.session_state.prices
    })
    df.to_csv("inventory_data.csv", index=False)

# This block loads the data from the CSV when the app first starts
if 'stuffs' not in st.session_state:
    if os.path.exists("inventory_data.csv"):
        df = pd.read_csv("inventory_data.csv")
        st.session_state.stuffs = df["Item"].tolist()
        st.session_state.prices = df["Price"].tolist()
    else:
        st.session_state.stuffs = []
        st.session_state.prices = []

# --- UI CONFIG ---
st.set_page_config(page_title="Cloud Inventory", layout="wide")
st.title("🌐 Inventory Website")

# --- SIDEBAR ---
menu = ["Input Data", "View Inventory", "Update/Delete", "Checkout"]
choice = st.sidebar.selectbox("Navigation", menu)

st.sidebar.markdown("---")
search_query = st.sidebar.text_input("🔍 Search Items")

if search_query:
    st.sidebar.subheader("Results")
    for s, p in zip(st.session_state.stuffs, st.session_state.prices):
        if search_query.lower() in s.lower():
            st.sidebar.write(f"✅ {s}: ${p:.2f}")

# --- PAGE 1: INPUT ---
if choice == "Input Data":
    st.header("➕ Add New Inventory")
    with st.form("input_form", clear_on_submit=True):
        new_stuff = st.text_input("Item Name")
        new_price = st.number_input("Price", min_value=0.0, step=0.01)
        submit = st.form_submit_button("Add to System")
        
        if submit and new_stuff:
            st.session_state.stuffs.append(new_stuff)
            st.session_state.prices.append(new_price)
            save_data()  # Save to CSV
            st.success(f"'{new_stuff}' has been saved to the database!")

# --- PAGE 2: VIEW ---
elif choice == "View Inventory":
    st.header("📋 Current Stock")
    if not st.session_state.stuffs:
        st.info("Inventory is empty.")
    else:
        data = {"Item Name": st.session_state.stuffs, "Price ($)": st.session_state.prices}
        st.table(data)

# --- PAGE 3: UPDATE/DELETE ---
elif choice == "Update/Delete":
    st.header("⚙️ Manage Items")
    if not st.session_state.stuffs:
        st.info("Nothing to manage.")
    else:
        selected_item = st.selectbox("Select item", st.session_state.stuffs)
        idx = st.session_state.stuffs.index(selected_item)
        
        col1, col2 = st.columns(2)
        with col1:
            new_name = st.text_input("Edit Name", value=st.session_state.stuffs[idx])
            new_pr = st.number_input("Edit Price", value=st.session_state.prices[idx])
            if st.button("Update"):
                st.session_state.stuffs[idx] = new_name
                st.session_state.prices[idx] = new_pr
                save_data() # Save to CSV
                st.rerun()
        
        with col2:
            st.write("---")
            if st.button("🗑️ Delete Item", type="primary"):
                st.session_state.stuffs.pop(idx)
                st.session_state.prices.pop(idx)
                save_data() # Save to CSV
                st.rerun()

# --- PAGE 4: CHECKOUT ---
elif choice == "Checkout":
    st.header("💳 Checkout Counter")
    if not st.session_state.stuffs:
        st.warning("Empty.")
    else:
        total = sum(st.session_state.prices)
        for s, p in zip(st.session_state.stuffs, st.session_state.prices):
            st.write(f"**{s}** : ${p:.2f}")
        
        st.divider()
        st.subheader(f"Total: ${total:.2f}")
        
        if st.button("Clear Inventory (Sale Complete)"):
            st.session_state.stuffs = []
            st.session_state.prices = []
            save_data() # Save the empty lists to CSV
            st.balloons()
            st.rerun()