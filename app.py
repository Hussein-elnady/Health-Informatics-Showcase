import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Hussein Elnady - Health Informatics Specialist", page_icon=":hospital:", layout="wide")

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottie_url("https://lottie.host/e309a000-9013-4915-b992-942d121af88c/c2E4rvTGpM.json")
img_contact_form = Image.open("images/yt_contact_form.jpg")
img_lottie_animation = Image.open("images/yt_lottie_animation.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Hussein Elnady :wave:")
    st.title ("A Health Informatics Specialist")
    st.write("I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings")
    st.write("[learn more >](https://www.linkedin.com/in/hussein-elnady-94ha)")

# ---- What I Do ---- 
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube channel, I create tutorials for people who:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way."

            If this sounds interesting to you, consider subscribing and turning on notifications, so you don’t miss any content.
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/)")
    
    with right_column:
        st_lottie(lottie_coding, height=500, key="coding")

# ---- My Projects ---- 
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
            In this tutorial, I'll show you exactly how to do it
            """
        )
        st.markdown("[Watch Video...](https://youtube/)")

# ----  Form ---- 
with st.container():
    st.write("---")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("How To Add A Contact Form To Your Streamlit App")
        st.write(
            """
            Want to add a contact form to your Streamlit website?
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
            """
        )
        st.markdown("[Watch Video...](https://youtube/)")

# Experience
st.header("Experience")

st.subheader("Health Informatician")
st.write("Benha - Qalyubia - Egypt")
st.write("General Organization for Teaching Hospitals and Institutes (GOTHI)")
st.write("Feb 2022 - Present")
st.write("- Developing and implementing electronic health record (EHR) systems.")
st.write("- Training and supporting clinical staff on EHR systems.")

# Education
st.header("Education")

st.subheader("Bachelor of Nursing")
st.write("Benha University")
st.write("2012-2016")

st.subheader("Health Informatics & Health Information Management")
st.write("Egyptian Fellowship")
st.write("2021-2024")

# Skills
st.header("Skills")

st.subheader("Technical Skills")
st.write("- Experience with EHR systems and healthcare data analysis software.")
st.write("- Knowledgeable in HL7 FHIR and other healthcare data standards and protocols.")
st.write("- Experience with programming languages like SQL, Python, and R.")
st.write("- Experience with data visualization tools like Power BI.")

st.subheader("Clinical Skills")
st.write("- Knowledge of medical terminology and procedures.")
st.write("- Understanding of healthcare privacy and security regulations.")

st.subheader("Communication and Interpersonal Skills")
st.write("- Ability to work effectively with various stakeholders.")
st.write("- Ability to provide excellent customer service.")

st.subheader("Problem-solving and Analytical Skills")
st.write("- Ability to identify and solve problems.")

st.subheader("Organizational Skills")
st.write("- Ability to manage multiple tasks and projects simultaneously.")

# Experience Details
st.header("Experience Details")

st.subheader("Intensive Care Clinical Nurse Specialist")
st.write("Mar 2020 - Oct 2021")
st.write("Qaha Central Hospital")
st.write("- Provide direct patient care to critically ill patients.")
st.write("- Assess, plan, implement, and evaluate patient care plans.")

st.subheader("Registered Nurse")
st.write("Sep 2016 - Oct 2018")
st.write("Nasser Institute Hospital")
st.write("- Assess patients' needs and develop care plans.")
st.write("- Collaborate with healthcare professionals to ensure comprehensive care.")

# Licenses & Certifications
st.header("Licenses & Certifications")

st.write("- Introduction to Cybersecurity - Cisco")
st.write("- Data Literacy Essentials - SAS")
st.write("- The Non-Technical Skills of Effective Data Scientists - LinkedIn")
st.write("- Introduction to IoT - Cisco")
st.write("- Linear Algebra for Machine Learning and Data Science - DeepLearning.AI")
st.write("- Database Fundamentals - Information Technology Institute (ITI)")
st.write("- Calculus for Machine Learning and Data Science - DeepLearning.AI")
st.write("- Probability & Statistics for Machine Learning & Data Science - DeepLearning.AI")
st.write("- Mathematics for Machine Learning and Data Science - DeepLearning.AI")


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documentation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/hussein_elnady@yahoo.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
