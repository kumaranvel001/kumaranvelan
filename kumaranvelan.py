import openai
import streamlit as st
import google.generativeai as genai
import os
import time

# Set your Google API key here
os.environ['GOOGLE_API_KEY'] = 'AIzaSyA2CtNVWwjQqhix-LGnKVhxoEVsGUFTDNg'
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')

@st.cache_data
def get_chatgpt_response(prompt):
    """Function to get response from the Google Gemini model"""
    if prompt:
        with st.spinner(text='Processing...'):
            # Simulate a delay for content generation (you can adjust this based on response time)
            time.sleep(15)

            # Get the response from the model
            response = model.generate_content(prompt)

            # Extract the generated text
            if response and response.candidates:
                content = response.candidates[0].content.parts[0].text
            else:
                content = "Error generating content."

            return content
    else:
        return "No prompt provided."

# Set up the Streamlit interface
st.title("Code Assistant using ChatGPT")
st.markdown("""
    Ask anything related to coding and get assistance from Google Gemini AI.
    You can ask about Python, debugging, algorithms, etc.
""")

# Text input for the user query
user_query = st.text_area("Enter your coding question or query:")

# Submit button
if st.button("Get Answer"):
    if user_query:
        st.write("ChatGPT is processing your request...")

        # Get the response from the Gemini model
        response = get_chatgpt_response(user_query)

        # Display the answer from Gemini AI
        st.write("**Answer from Gemini AI:**")
        st.write(response)
    else:
        st.write("Please enter a question!")
