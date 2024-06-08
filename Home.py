import streamlit as st
import google.generativeai as genai
import os
# RUN THE FILE
# python -m streamlit run Home.py OR
# streamlit run Home.py

st.set_page_config(page_title="MUS 17 Final Project")

path = os.path.dirname(__file__)
st.title("MUS 17 Final Project - Assisting Rappers using LLMs and Prompt Tuning")

st.write("This project explores using prompt tuning to assist Hip Hop artists in creating rap music. I will be leveraging the Gemini API to fine-tune a large language model (LLM) and employ various techniques, such as Chain of Thought prompting, to guide the model towards completing different creative tasks.")

def explain_task():
        return """
        ### Idea Generation
        Are you stuck for a topic? Let's brainstorm some fresh ideas to get you started!
        You can input a few themes or concepts, and we'll help you generate engaging topics to rap about.
        ### Enhance Writing
        Have you already written some lyrics but feel they need polishing? 
        We can refine your flow and improve your rhyme schemes. Just paste your existing lyrics, and we'll enhance them.
        ### Write from Scratch
        Got a general concept but need some lyrical assistance? 
        We can help you build the foundation of your rap verse from the ground up. Provide your idea, and let's create something amazing together.
        """

st.markdown(explain_task())

st.markdown(
    """
    ### Test The Tool Here!
    """
)

task_type = st.selectbox("Select a task:", ["Select", "Idea Generation", "Enhance Writing", "Write from scratch"])

if task_type == "Idea Generation":
    user_input = st.text_input("Provide some topics that you would like to write about:")
elif task_type == "Enhance Writing":
    user_input = st.text_input("Put your work uptill now:")
elif task_type == "Write from scratch":
    user_input = st.text_input("What's your idea?")
else:
    st.write("Please select one of the options")

clicked = st.button('Generate')
def generate_with_gemini_api(task_type, user_input):
    api_key = "AIzaSyAEuZj8v1gjf5vUGvJ3piVCQqD6xnAks_w"
    if task_type == "Idea Generation":
        prompt = (
            f"You are a creative assistant helping a rapper brainstorm new topics for songs. "
            f"Start by generating three broad themes based on the following input: {user_input}. "
            f"After generating the broad themes, provide two specific topics under each theme. "
            f"Make sure the topics are unique and engaging. "
            f"Format the response in markdown with headings for each theme and bullet points for each specific topic."
        )
    elif task_type == "Enhance Writing":
        prompt = (
            f"You are a skilled lyricist enhancing rap lyrics to improve their flow and rhyme schemes. "
            f"Analyze the following lyrics: {user_input}. "
            f"Identify areas that could be improved in terms of flow and rhyme. "
            f"Rewrite the lyrics with these improvements, ensuring they maintain the original meaning and context. "
            f"Provide the analysis followed by the enhanced lyrics, formatted in markdown."
        )
    elif task_type == "Write from scratch":
        prompt = (
            f"You are a creative writer composing rap lyrics from scratch. "
            f"Based on the following idea: {user_input}, brainstorm an3 verse rap, "
            f"that builds upon this idea. "
            f"Ensure the lines rhyme and maintain a consistent flow. "
            f"Format the response in markdown with each line in a new paragraph."
        )
    else:
        return "Invalid task type."
    genai.configure(api_key=api_key)
    # The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text

# Example function to simulate Gemini API call
def gemini_api_call(task_type, user_input):
    # Simulate an API call with a dummy response
    return f"Simulated response for {task_type} with input: {user_input}"

if clicked:
    st.write("Processing your request...")
        
        # Placeholder for integrating the Gemini API and prompt tuning
    st.write("**Generated Output:**")
    # Call your Gemini API function here

    output = generate_with_gemini_api(task_type, user_input)
    st.markdown(output)