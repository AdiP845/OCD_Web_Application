import streamlit as st
from utils import Query 
import google.generativeai as genai

genai.configure(api_key="AIzaSyDaD4NVLgffhR-cGNGwi3pAF01XcQBuvXY")
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_response(query):
    response = model.generate_content(query)
    return response.text


# Define navigation function
def navigate_to_page(page_name):
    st.session_state["page"] = page_name

# Initialize session state
if "page" not in st.session_state:
    st.session_state["page"] = "Home" 

# Home Page
if st.session_state["page"] == "Home":
    st.title("Home Page")
    st.write("Welcome to the Home Page!")
    st.button("Contamination OCD", use_container_width=True, type='primary', icon="🧼", on_click=navigate_to_page, args=("Contamination OCD",))

# Page Contamination OCD
elif st.session_state["page"] == "Contamination OCD":
    st.title("Contamination OCD")
    st.write("Understanding and addressing Contamination OCD")

     # Triggers checklist
    st.sidebar.title("My Triggers for Contamination OCD")
    triggers = st.sidebar.multiselect(
        "Select your triggers:",
        options=[
            "Public Items (e.g., Doorknobs)",
            "Bodily Fluids (e.g., Blood, Sweat)",
            "Poisons (e.g., cleaning agents)",
            "Drugs",
            "Illness-related items (e.g., Hospitals)",
            "Strongly disgusting substances (e.g., sticky or unknown)"
        ]
        )

     # Fears checklist
    st.sidebar.title("My Fears of Contamination OCD")
    fears = st.sidebar.multiselect(
         "Select your fears:",
         options=[
             "Fear of sickness from germs/viruses",
             "Fear of excessive washing rituals",
             "Fear of spreading germs",
             "Fear of disgust",
             "Fear of avoiding valued items",
             "Fear of being seen as 'dirty'",
             "Fear of becoming 'dirty' or irresponsible"
            ]
        )

     # Join selections
    Triggers = ", ".join(triggers) if triggers else "None"
    Fears = ", ".join(fears) if fears else "None"
    
     # Column layout for buttons
    col1, col2, col3, col4 = st.columns(4)

    query = None  # Initialize query variable

     # Place one button in each column
    with col1:
         if st.button("Acceptance Tools"):
             query = Query("Contamination OCD", Triggers, Fears, "Give me an Acceptance Tool for it.")
    with col2:
         if st.button("Meditation Tips"):
             query = Query("Contamination OCD", Triggers, Fears, "Give me Meditation tips for it.")
    with col3:
         if st.button("Assessment Tools"):
             query = Query("Contamination OCD", Triggers, Fears, "Give me Assessment Tools for it.")
    with col4:
         if st.button("Action Tools"):
             query = Query("Contamination OCD", Triggers, Fears, "Give me Action Tools for it.")

     # Display the result of the query if it exists
    if query:
         query_string = query.create_query()
         with st.spinner("Generating response..."):
             response = generate_response(query_string)
             st.write(response)  # Call the display method to show the formatted message

     # User input field
    user_input = st.text_input("Your Message:", key="user_input", placeholder="Type your message here...")
    if user_input:
        query = query = Query("Contamination OCD", Triggers, Fears, user_input)
        query_string = query.create_query()
        with st.spinner("Generating response..."):
            response = generate_response(query_string)
            st.write(response)


     # Back button
    st.button("Back to Home", use_container_width=True, on_click=navigate_to_page, args=("Home",))
