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
    st.title("Your Supportive Companion for Understanding and Managing OCD")
    st.write("Choose your OCD type to discover personalized guidance, support, and strategies for managing your symptoms.")

    col1, col2 = st.columns(2)
    with col1:
        st.button("Contamination OCD", use_container_width=True, type='primary', icon="🧼", on_click=navigate_to_page, args=("Contamination OCD",))
        st.button("Symmetry and Ordering OCD", use_container_width=True, type='primary', icon="🔄", on_click=navigate_to_page, args=("Symmetry and Ordering OCD",))
        st.button("Sexual Orientation OCD", use_container_width=True, type='primary', icon="🏳️‍🌈", on_click=navigate_to_page, args=("Sexual Orientation OCD",))
        st.button("Relationship OCD", use_container_width=True, type='primary', icon="💔", on_click=navigate_to_page, args=("Relationship OCD",))
    with col2:
        st.button("Responsibility or Checking OCD", use_container_width=True, type='primary', icon="✅", on_click=navigate_to_page, args=("Responsibility or Checking OCD",))
        st.button("Harm OCD", use_container_width=True, type='primary', icon="⚠️", on_click=navigate_to_page, args=("Harm OCD",))
        st.button("Pedophile OCD", use_container_width=True, type='primary', icon="🚫", on_click=navigate_to_page, args=("Pedophile OCD",))
        st.button("Hyperawareness OCD", use_container_width=True, type='primary', icon="👁️", on_click=navigate_to_page, args=("Hyperawareness OCD",))

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

        

# Page Symmetry and Ordering OCD
elif st.session_state["page"] == "Symmetry and Ordering OCD":
    st.title("Symmetry and Ordering OCD")
    st.write("Understanding and addressing Symmetry and Ordering OCD")

     # Triggers checklist
    st.sidebar.title("My Triggers for Symmetry and Ordering OCD")
    triggers = st.sidebar.multiselect(
        "Select your triggers:",
        options=[
            "Misaligned Objects (e.g., crooked frames)",
            "Uneven Patterns (e.g., Mismatched Tiles)",
            "Sensory Imbalances (e.g., Uneven Touches)",
            "Disorganized Spaces (e.g., Messy Desks)",
            "Irregular Handwriting or Typing (e.g., Sloppy Letters)",
            "Asymmetrical Clothing (e.g., Untied Shoelaces)",
            "Unequal Sounds (e.g., Uneven Headphone Volume)",
            "Unbalanced Actions (e.g., Shaking One Hand but Not the Other)"
        ]
        )

     # Fears checklist
    st.sidebar.title("My Fears of Symmetry and Ordering OCD")
    fears = st.sidebar.multiselect(
         "Select your fears:",
         options=[
             "Fear of Imperfection",
             "Fear of Bad Outcomes",
             "Fear of Losing Control",
             "Fear of Incompleteness",
             "Fear of Guilt"
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
             query = Query("Symmetry and Ordering OCD", Triggers, Fears, "Give me an Acceptance Tool for it.")
    with col2:
         if st.button("Meditation Tips"):
             query = Query("Symmetry and Ordering OCD", Triggers, Fears, "Give me Meditation tips for it.")
    with col3:
         if st.button("Assessment Tools"):
             query = Query("Symmetry and Ordering OCD", Triggers, Fears, "Give me Assessment Tools for it.")
    with col4:
         if st.button("Action Tools"):
             query = Query("Symmetry and Ordering OCD", Triggers, Fears, "Give me Action Tools for it.")

     # Display the result of the query if it exists
    if query:
         query_string = query.create_query()
         with st.spinner("Generating response..."):
             response = generate_response(query_string)
             st.write(response)  # Call the display method to show the formatted message

     # User input field
    user_input = st.text_input("Your Message:", key="user_input", placeholder="Type your message here...")
    if user_input:
        query = query = Query("Symmetry and Ordering OCD", Triggers, Fears, user_input)
        query_string = query.create_query()
        with st.spinner("Generating response..."):
            response = generate_response(query_string)
            st.write(response)


     # Back button
    st.button("Back to Home", use_container_width=True, on_click=navigate_to_page, args=("Home",))
        

# Page Sexual Orientation OCD
elif st.session_state["page"] == "Sexual Orientation OCD":
    st.title("Sexual Orientation OCD")
    st.write("Understanding and addressing Sexual Orientation OCD")

     # Triggers checklist
    st.sidebar.title("My Triggers for Sexual Orientation OCD")
    triggers = st.sidebar.multiselect(
        "Select your triggers:",
        options=[
            "LGBTQ+ Topics (e.g., News, Social Discussions)",
            "Interactions with Same-Sex Individuals (e.g., Casual Conversations)",
            "Interactions with Opposite-Sex Individuals (e.g., Friendships)",
            "Romantic Intimacy (e.g., Kissing or Holding Hands)",
            "Physical Responses (e.g., Unexpected Arousal)",
            "Past Behaviors (e.g., Childhood Friendships)",
            "Media Representations (e.g., LGBTQ+ Characters in Shows)",
            "Personal Reflections (e.g., Analyzing Memories or Dreams)"
            
            ]
        )

     # Fears checklist
    st.sidebar.title("My Fears of Sexual Orientation OCD")
    fears = st.sidebar.multiselect(
         "Select your fears:",
         options=[
             "Fear of Being the 'Wrong' Orientation(e.g., Not Aligning with Current Identity)",
             "Fear of Discovering a Hidden Orientation (e.g., Suddenly Realizing a Change)",
             "Fear of Losing Authenticity (e.g., Living a False Life)",
             "Fear of Betraying a Partner (e.g., Not Truly Loving Them)",
             "Fear of Social Judgment (e.g., Facing Rejection or Criticism)",
             "Fear of Acting on Intrusive Thoughts (e.g., Engaging in Unwanted Behaviors)",
             "Fear of Permanence (e.g., Not Being Able to Revert an Orientation)",
             "Fear of Misinterpreted Feelings (e.g., Mistaking Platonic for Romantic)"
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
             query = Query("Sexual Orientation OCD", Triggers, Fears, "Give me an Acceptance Tool for it.")
    with col2:
         if st.button("Meditation Tips"):
             query = Query("Sexual Orientation OCD", Triggers, Fears, "Give me Meditation tips for it.")
    with col3:
         if st.button("Assessment Tools"):
             query = Query("Sexual Orientation OCD", Triggers, Fears, "Give me Assessment Tools for it.")
    with col4:
         if st.button("Action Tools"):
             query = Query("Sexual Orientation OCD", Triggers, Fears, "Give me Action Tools for it.")

     # Display the result of the query if it exists
    if query:
         query_string = query.create_query()
         with st.spinner("Generating response..."):
             response = generate_response(query_string)
             st.write(response)  # Call the display method to show the formatted message

     # User input field
    user_input = st.text_input("Your Message:", key="user_input", placeholder="Type your message here...")
    if user_input:
        query = query = Query("Sexual Orientation OCD", Triggers, Fears, user_input)
        query_string = query.create_query()
        with st.spinner("Generating response..."):
            response = generate_response(query_string)
            st.write(response)


     # Back button
    st.button("Back to Home", use_container_width=True, on_click=navigate_to_page, args=("Home",))

# Page of Relationship OCD
elif st.session_state["page"] == "Relationship OCD":
    st.title("Relationship OCD")
    st.write("Understanding and addressing Relationship OCD")

     # Triggers checklist
    st.sidebar.title("My Triggers for Relationship OCD")
    triggers = st.sidebar.multiselect(
        "Select your triggers:",
        options=[
            "Partner's Behavior (e.g., Lack of Affection)",
            "Relationship Milestones (e.g., Anniversaries)",
            "Comparisons (e.g., Observing 'Perfect' Couples)",
            "Self-Doubt (e.g., Questioning Love or Attraction)",
            "External Opinions (e.g., Family Comments",
            "Conflicts (e.g., Arguments)",
            "Media (e.g., Romantic Movies)",
            "Past Relationship Trauma (e.g., Infidelity)",
            "Social Media (e.g., Partner's Activity)",
            "Uncertainty (e.g., Unclear Communication)"
        ]
        )

     # Fears checklist
    st.sidebar.title("My Fears of Relationship OCD")
    fears = st.sidebar.multiselect(
         "Select your fears:",
         options=[
             "Fear of Being with the Wrong Partner",
             "Fear of Not Truly Loving the Partner",
             "Fear of Being Betrayed",
             "Fear of Losing Attraction",
             "Fear of Partner's Flaws",
             "Fear of Incompatibility",
             "Fear of Regret",
             "Fear of Relationship Failure"
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
             query = Query("Relationship OCD", Triggers, Fears, "Give me an Acceptance Tool for it.")
    with col2:
         if st.button("Meditation Tips"):
             query = Query("Relationship OCD", Triggers, Fears, "Give me Meditation tips for it.")
    with col3:
         if st.button("Assessment Tools"):
             query = Query("Relationship OCD", Triggers, Fears, "Give me Assessment Tools for it.")
    with col4:
         if st.button("Action Tools"):
             query = Query("Relationship OCD", Triggers, Fears, "Give me Action Tools for it.")

     # Display the result of the query if it exists
    if query:
         query_string = query.create_query()
         with st.spinner("Generating response..."):
             response = generate_response(query_string)
             st.write(response)  # Call the display method to show the formatted message

     # User input field
    user_input = st.text_input("Your Message:", key="user_input", placeholder="Type your message here...")
    if user_input:
        query = query = Query("Relationship OCD ", Triggers, Fears, user_input)
        query_string = query.create_query()
        with st.spinner("Generating response..."):
            response = generate_response(query_string)
            st.write(response)


     # Back button
    st.button("Back to Home", use_container_width=True, on_click=navigate_to_page, args=("Home",))

# Page Responsibility or Checking OCD
elif st.session_state["page"] == "Responsibility or Checking OCD":
    st.title("Responsibility or Checking OCD")
    st.write("Understanding and addressing Responsibility or Checking OCD")

     # Triggers checklist
    st.sidebar.title("My Triggers for Responsibility or Checking OCD")
    triggers = st.sidebar.multiselect(
        "Select your triggers:",
        options=[
            "Everyday Tasks (e.g., Locking Doors)",
            "Electrical Appliances (e.g., Turning Off Stoves)",
            "Fire Hazards (e.g., Candles Left Burning)",
            "Driving Incidents (e.g., Hitting Someone)",
            "Health Risks (e.g., Leaving Medications Accessible)",
            "Work-Related Mistakes (e.g., Sending Incorrect Emails)",
            "Environmental Harm (e.g., Wasting Water)",
            "Safety Concerns (e.g., Securing Windows)"
        ]
        )

     # Fears checklist
    st.sidebar.title("My Fears of Responsibility or Checking OCD")
    fears = st.sidebar.multiselect(
         "Select your fears:",
         options=[
             "Fear of Causing Harm",
             "Fear of Neglecting Duties",
             "Fear of Injuring Others",
             "Fear of Accidental Death",
             "Fear of Legal Trouble",
             "Fear of Making Critical Errors",
             "Fear of Moral Failure",
             "Fear of Environmental Damage"
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
             query = Query("Responsibility or Checking OCD", Triggers, Fears, "Give me an Acceptance Tool for it.")
    with col2:
         if st.button("Meditation Tips"):
             query = Query("Responsibility or Checking OCD", Triggers, Fears, "Give me Meditation tips for it.")
    with col3:
         if st.button("Assessment Tools"):
             query = Query("Responsibility or Checking OCD", Triggers, Fears, "Give me Assessment Tools for it.")
    with col4:
         if st.button("Action Tools"):
             query = Query("Responsibility or Checking OCD", Triggers, Fears, "Give me Action Tools for it.")

     # Display the result of the query if it exists
    if query:
         query_string = query.create_query()
         with st.spinner("Generating response..."):
             response = generate_response(query_string)
             st.write(response)  # Call the display method to show the formatted message

     # User input field
    user_input = st.text_input("Your Message:", key="user_input", placeholder="Type your message here...")
    if user_input:
        query = query = Query("Responsibility or Checking OCD", Triggers, Fears, user_input)
        query_string = query.create_query()
        with st.spinner("Generating response..."):
            response = generate_response(query_string)
            st.write(response)


     # Back button
    st.button("Back to Home", use_container_width=True, on_click=navigate_to_page, args=("Home",))



# Page for Harm OCD
elif st.session_state["page"] == "Harm OCD":
    st.title("Harm OCD")
    st.write("Understanding and addressing Harm OCD")

     # Triggers checklist
    st.sidebar.title("My Triggers for Harm OCD")
    triggers = st.sidebar.multiselect(
        "Select your triggers:",
        options=[
            "Violent News Stories (e.g., Reports of Murders)",
            "Sharp Objects (e.g., Knives, Scissors)",
            "Physical Proximity to Others (e.g., Standing Near Strangers)",
            "Intrusive Thoughts (e.g., Violent Scenarios)",
            "Media Depicting Violence (e.g., Movies, Video Games)",
            "Accidental Harm Risks (e.g., Driving)",
            "Physical Touch (e.g., Hugging)",
            "Moral Dilemmas (e.g., Ethical Responsibility in Preventing Harm)"
        ]
        )

     # Fears checklist
    st.sidebar.title("My Fears of Harm OCD")
    fears = st.sidebar.multiselect(
         "Select your fears:",
         options=[
             "Fear of Hurting Loved Ones",
             "Fear of Losing Control",
             "Fear of Accidental Harm",
             "Fear of Committing a Crime",
             "Fear of Being Evil or Immoral",
             "Fear of Self-Harm",
             "Fear of Causing Indirect Harm",
             "Fear of Negative Consequences from Intrusive Thoughts"
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
             query = Query("Harm OCD", Triggers, Fears, "Give me an Acceptance Tool for it.")
    with col2:
         if st.button("Meditation Tips"):
             query = Query("Harm OCD", Triggers, Fears, "Give me Meditation tips for it.")
    with col3:
         if st.button("Assessment Tools"):
             query = Query("Harm OCD", Triggers, Fears, "Give me Assessment Tools for it.")
    with col4:
         if st.button("Action Tools"):
             query = Query("Harm OCD", Triggers, Fears, "Give me Action Tools for it.")

     # Display the result of the query if it exists
    if query:
         query_string = query.create_query()
         with st.spinner("Generating response..."):
             response = generate_response(query_string)
             st.write(response)  # Call the display method to show the formatted message

     # User input field
    user_input = st.text_input("Your Message:", key="user_input", placeholder="Type your message here...")
    if user_input:
        query = query = Query("Harm OCD", Triggers, Fears, user_input)
        query_string = query.create_query()
        with st.spinner("Generating response..."):
            response = generate_response(query_string)
            st.write(response)


     # Back button
    st.button("Back to Home", use_container_width=True, on_click=navigate_to_page, args=("Home",))


# Page for Pedophile OCD
elif st.session_state["page"] == "Pedophile OCD":
    st.title("Pedophile OCD")
    st.write("Understanding and addressing Pedophile OCD")

     # Triggers checklist
    st.sidebar.title("My Triggers for Pedophile OCD")
    triggers = st.sidebar.multiselect(
        "Select your triggers:",
        options=[
            "Being Around Children",
            "Physical Contact (e.g., Hugging)",
            "Intrusive Thoughts (e.g., Sexualized Images Involving Children)",
            "Media Depicting Children",
            "Social Situations (e.g., Being Alone with a Child)",
            "Past Experiences",
            "Moral Concerns",
            "Unintended Physical Reactions"
        ]
        )

     # Fears checklist
    st.sidebar.title("My Fears of Pedophile OCD")
    fears = st.sidebar.multiselect(
         "Select your fears:",
         options=[
             "Fear of Being a Pedophile",
             "Fear of Acting on Intrusive Thoughts",
             "Fear of Losing Control",
             "Fear of Being a Bad Person",
             "Fear of Being Misunderstood",
             "Fear of Guilt or Shame",
             "Fear of Repercussions"
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
             query = Query("Pedophile OCD", Triggers, Fears, "Give me an Acceptance Tool for it.")
    with col2:
         if st.button("Meditation Tips"):
             query = Query("Pedophile OCD", Triggers, Fears, "Give me Meditation tips for it.")
    with col3:
         if st.button("Assessment Tools"):
             query = Query("Pedophile OCD", Triggers, Fears, "Give me Assessment Tools for it.")
    with col4:
         if st.button("Action Tools"):
             query = Query("Pedophile OCD", Triggers, Fears, "Give me Action Tools for it.")

     # Display the result of the query if it exists
    if query:
         query_string = query.create_query()
         with st.spinner("Generating response..."):
             response = generate_response(query_string)
             st.write(response)  # Call the display method to show the formatted message

     # User input field
    user_input = st.text_input("Your Message:", key="user_input", placeholder="Type your message here...")
    if user_input:
        query = query = Query("Pedophile OCD", Triggers, Fears, user_input)
        query_string = query.create_query()
        with st.spinner("Generating response..."):
            response = generate_response(query_string)
            st.write(response)


     # Back button
    st.button("Back to Home", use_container_width=True, on_click=navigate_to_page, args=("Home",))

# Page of Hyperawareness OCD
elif st.session_state["page"] == "Hyperawareness OCD":
    st.title("Hyperawareness OCD")
    st.write("Understanding and addressing Hyperawareness OCD")

     # Triggers checklist
    st.sidebar.title("My Triggers for Hyperawareness OCD")
    triggers = st.sidebar.multiselect(
        "Select your triggers:",
        options=[
            "Being in Social Situations (e.g., Interacting Friends)",
            "Physical Sensations (e.g., Feeling Heartbeat)",
            "Internal Thoughts",
            "Feeling Discomfort or Pain",
            "Exposure to Stress or Anxiety",
            "Self-Perception (e.g., Worrying About How Others See You)",
            "Specific Actions or Behaviors (e.g., Chewing)",
            "Unintended Physical Reactions",
            "Environmental Stimuli (e.g., Loud Noises)"
        ]
        )

     # Fears checklist
    st.sidebar.title("My Fears of Hyperawareness OCD")
    fears = st.sidebar.multiselect(
         "Select your fears:",
         options=[
             "Fear of Losing Control",
             "Fear of Embarrassment",
             "Fear of Acting Strangely",
             "Fear of Being Constantly Aware",
             "Fear of Anxiety Escalating",
             "Fear of Not Being Able to Stop the Awareness",
             "Fear of Negative Reactions from Others",
             "Fear of Losing Connection with Reality"
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
             query = Query("Hyperawareness OCD", Triggers, Fears, "Give me an Acceptance Tool for it.")
    with col2:
         if st.button("Meditation Tips"):
             query = Query("Hyperawareness OCD", Triggers, Fears, "Give me Meditation tips for it.")
    with col3:
         if st.button("Assessment Tools"):
             query = Query("Hyperawareness OCD", Triggers, Fears, "Give me Assessment Tools for it.")
    with col4:
         if st.button("Action Tools"):
             query = Query("Hyperawareness OCD", Triggers, Fears, "Give me Action Tools for it.")

     # Display the result of the query if it exists
    if query:
         query_string = query.create_query()
         with st.spinner("Generating response..."):
             response = generate_response(query_string)
             st.write(response)  # Call the display method to show the formatted message

     # User input field
    user_input = st.text_input("Your Message:", key="user_input", placeholder="Type your message here...")
    if user_input:
        query = query = Query("Hyperawareness OCD", Triggers, Fears, user_input)
        query_string = query.create_query()
        with st.spinner("Generating response..."):
            response = generate_response(query_string)
            st.write(response)


     # Back button
    st.button("Back to Home", use_container_width=True, on_click=navigate_to_page, args=("Home",))

