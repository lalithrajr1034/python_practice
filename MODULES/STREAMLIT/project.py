import streamlit as st
from datetime import datetime

# --- Hide Streamlit branding ---
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact", "Live Clock"])

# --- Home Page ---
if page == "Home":
    st.markdown("<h1 style='text-align: center; color: #2E86C1;'> Welcome to My Lab</h1>", unsafe_allow_html=True)

    st.markdown("---")
    st.write("""
    **this is my basic streamlit website""")


    st.markdown("---")
    st.image(
        "https://media.licdn.com/dms/image/v2/D5603AQG17mPPWYdE_g/profile-displayphoto-shrink_400_400/B56ZbPtuKUHUAg-/0/1747241592441?e=1756944000&v=beta&t=kgH17t0v9OAfxh4oeeQiLNuH8ZuWqXp4nJCK4mB3PK8",
        use_column_width=56,
        use_container_width=10
    )

# --- About Page ---
elif page == "About":
    st.title(" About Lalith Raj")
    st.write("""
    Hello! I'm **Lalith Raj**, a passionate AI & ML 
    
    Studying at MIT Mysore – CSE with AI specialization  
    
    
    Believe in practical skills over marks — portfolio > CGPA  

    
    """)

# --- Contact Page ---
elif page == "Contact":
    st.title(" Contact Lalith Raj")
    st.write("Fill in the form below to get in touch directly:")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send")

        if submit:
            if name and email and message:
                st.success(f"Thanks {name}, your message has been sent to Lalith Raj!")
            else:
                st.warning(" Please complete all fields before submitting.")

# --- Dynamic Feature Page: Live Clock ---
elif page == "Live Clock":
    st.title(" Real-Time Clock")
    st.write("This clock updates every time you refresh the page.")

    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%A, %d %B %Y")

    st.markdown(f"###  Time: `{current_time}`")
    st.markdown(f"###  Date: `{current_date}`")

    st.info("Note: Live auto-refresh requires full app rerun (coming soon in future updates).")

# --- Footer ---
st.markdown(
    "<hr><p style='text-align: center; color: grey;'>© 2025 Lalith Raj. All rights reserved.</p>",
    unsafe_allow_html=True
)
