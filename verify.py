import streamlit as st
import pandas as pd

# Read CSV files
participants_df = pd.read_csv("participants.csv")
core_df = pd.read_csv("core.csv")
evangelist_df = pd.read_csv("evangelist.csv")
winners_df = pd.read_csv("winners.csv")

# Define a function to verify the certificate ID and retrieve the relevant information
def verify_certificate(cert_id):
    # Check in participants.csv
    if cert_id in participants_df['cert_id'].astype(str).values:
        record = participants_df[participants_df['cert_id'].astype(str) == cert_id].iloc[0]
        return "Participant", record['name'], record.get('team', 'N/A'), None
    
    # Check in core.csv
    elif cert_id in core_df['cert_id'].astype(str).values:
        record = core_df[core_df['cert_id'].astype(str) == cert_id].iloc[0]
        return "Core Team Member", record['name'], record.get('team', 'N/A'), None
    
    # Check in evangelist.csv
    elif cert_id in evangelist_df['cert_id'].astype(str).values:
        record = evangelist_df[evangelist_df['cert_id'].astype(str) == cert_id].iloc[0]
        return "Evangelist", record['name'], record.get('team', 'N/A'), record.get('role', 'N/A')
    
    # Check in winners.csv
    elif cert_id in winners_df['cert_id'].astype(str).values:
        record = winners_df[winners_df['cert_id'].astype(str) == cert_id].iloc[0]
        return "Award Winner", record['name'], record.get('team', 'N/A'), None
    
    # Return None if not found in any CSV
    return None, None, None, None

# Streamlit app
st.title("H4B Certificate Verification Portal")

cert_id = st.text_input("Enter Certificate ID")

if st.button("Verify"):
    if cert_id:
        category, name, team_name, role = verify_certificate(cert_id)
        if category:
            st.success("Certificate Verified ✅")
            st.write(f"Name: {name}")
            if category == "Evangelist":
                st.write(f"Role: {team_name}")
            else:
                st.write(f"Team Name: {team_name}")
            st.write(f"Category: {category}")
            st.write(f"Issued on: 04-08-2024")
            st.write(f"Issued by: Hack4Bengal")
        else:
            st.error("Invalid Certificate ID")
    else:
        st.warning("Please enter a certificate ID")
