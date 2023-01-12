""" 
# Validate the Transaction
if st.sidebar.button('Validate Transaction'):
    if raw_tx.is_valid():
        st.success('This is a valid transaction!', icon="✅")
    else:
        st.warning('This is NOT a valid transaction!', icon="⚠️")
"""
