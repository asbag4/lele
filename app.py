import streamlit as st

st.title("Counter App")
if "count" not in st.session_state:
    st.session_state.count = 0
st.header(st.session_state.count)

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("➕ increase"):
        st.session_state.count += 1
with col2:
    if st.button("➖ Decrease"):
        st.session_state.count -= 1
with col2:
    if st.button("🔄 Reset"):
        st.session_state.count = 0
