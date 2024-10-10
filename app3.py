import streamlit as st
import uuid

# Dummy function to simulate token generation
def generate_token():
    return str(uuid.uuid4())

# Dummy function to create a session (returns session id)
def create_session():
    return str(uuid.uuid4())

# Function to upload files (emulates email extraction process)
def upload_emails(uploaded_file):
    if uploaded_file is not None:
        file_content = uploaded_file.getvalue().decode("utf-8")
        # Here we emulate the extraction of data from the uploaded email text
        st.write("Uploaded Email Text:")
        st.write(file_content)
        return file_content
    return None

# Function to ask static question (emulates AI model generating response)
def ask_static_prompt(extracted_text):
    # Static prompt question example
    static_response = f"Static response based on extracted data: {extracted_text[:100]}..."
    return static_response

# Function to ask dynamic prompt
def ask_dynamic_prompt(extracted_text, dynamic_prompt):
    # Dynamic response example based on the user input
    dynamic_response = f"Dynamic response to '{dynamic_prompt}' based on extracted data: {extracted_text[:100]}..."
    return dynamic_response

# Dummy function to teardown the session
def teardown_session(session_id):
    st.write(f"Session {session_id} is now closed.")

# Streamlit app
st.title("Dummy Microservice - Email Processing with Dynamic Prompts")

# Token Generation
if 'token' not in st.session_state:
    st.session_state['token'] = generate_token()
    st.session_state['session_id'] = None
    st.session_state['extracted_data'] = None
    st.session_state['static_response'] = None
    st.session_state['dynamic_responses'] = []

st.write(f"Generated Token: {st.session_state['token']}")

# Generate the session ID even if the file hasn't been uploaded yet
if st.session_state['session_id'] is None:
    st.session_state['session_id'] = create_session()

# Show the session ID before file upload
st.write(f"Session ID: {st.session_state['session_id']}")

# Start the session when a file is uploaded
uploaded_file = st.file_uploader("Upload Email Text File")

if uploaded_file and st.session_state['extracted_data'] is None:
    st.session_state['extracted_data'] = upload_emails(uploaded_file)
    st.session_state['static_response'] = ask_static_prompt(st.session_state['extracted_data'])
    st.write(f"Static Prompt Response: {st.session_state['static_response']}")

# Static prompt is done, now allow for dynamic questions
if st.session_state['static_response'] is not None:
    st.subheader("Ask Dynamic Questions")

    dynamic_prompt = st.text_input("Enter a dynamic prompt")

    if st.button("Submit Dynamic Prompt"):
        if dynamic_prompt:
            dynamic_response = ask_dynamic_prompt(st.session_state['extracted_data'], dynamic_prompt)
            st.session_state['dynamic_responses'].append(dynamic_response)
            st.write(f"Dynamic Prompt Response: {dynamic_response}")

# Display all dynamic responses so far
if st.session_state['dynamic_responses']:
    st.subheader("Dynamic Responses So Far:")
    for i, response in enumerate(st.session_state['dynamic_responses']):
        st.write(f"Dynamic Response {i+1}: {response}")

# Option to close the session if the user is satisfied
if st.session_state['static_response'] is not None:
    if st.button("I'm satisfied, close the session"):
        teardown_session(st.session_state['session_id'])
        # Reset session state
        st.session_state['session_id'] = None
        st.session_state['extracted_data'] = None
        st.session_state['static_response'] = None
        st.session_state['dynamic_responses'] = []
        st.write("Session closed. Thank you!")
