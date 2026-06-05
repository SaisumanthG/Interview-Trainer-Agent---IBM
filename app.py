
import streamlit as st
from pypdf import PdfReader
from ibm_watsonx_ai.foundation_models import Model
from sympy import python



API_KEY = "4KimgmMVYZaRbPCdry6A7daTES05CGToeTp7T7h866Dz"
PROJECT_ID = "89588250-15c0-48b9-92ff-19e7535f2130"

credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": API_KEY
}

model = Model(
    model_id="meta-llama/llama-3-3-70b-instruct",
    credentials=credentials,
    project_id=PROJECT_ID
)



st.set_page_config(
    page_title="Interview Trainer Agent",
    page_icon="🎯",
    layout="wide"
)



st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0f172a,#1e293b);
}

.main-title{
text-align:center;
font-size:60px;
font-weight:800;
background: linear-gradient(90deg,#60a5fa,#22c55e);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
margin-bottom:10px;
}

.sub-title{
text-align:center;
font-size:20px;
color:#cbd5e1;
margin-bottom:30px;
}

.card{
background:#1e293b;
padding:25px;
border-radius:20px;
border:1px solid #334155;
box-shadow:0px 0px 20px rgba(0,0,0,0.25);
margin-bottom:20px;
}

.footer{
text-align:center;
color:#94a3b8;
margin-top:40px;
}

.metric-card{
background:#111827;
padding:15px;
border-radius:15px;
text-align:center;
color:white;
}

.question-card{
background:#111827;
padding:15px;
border-left:5px solid #22c55e;
border-radius:10px;
margin-top:15px;
color:white;
}

</style>
""", unsafe_allow_html=True)



st.markdown("""
<div class='main-title'>
🎯 Interview Trainer Agent
</div>

<div class='sub-title'>
AI Powered Interview Preparation using IBM Granite Models
</div>
""", unsafe_allow_html=True)



col1,col2,col3 = st.columns(3)

with col1:
    st.metric("AI Model","Granite")

with col2:
    st.metric("Interview Mode","Smart")

with col3:
    st.metric("Question Type","Resume Based")



st.markdown("<div class='card'>", unsafe_allow_html=True)

col1,col2 = st.columns(2)

with col1:
    role = st.selectbox(
        "💼 Select Target Role",
        [
            "Python Developer",
            "Java Developer",
            "Web Developer",
            "Data Analyst",
            "Data Scientist",
            "AI Engineer",
            "Machine Learning Engineer",
            "Frontend Developer",
            "Backend Developer"
        ]
    )

with col2:
    difficulty = st.selectbox(
        "📈 Interview Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF or TXT)",
    type=["pdf","txt"]
)

st.markdown("</div>", unsafe_allow_html=True)



resume_text = ""

if uploaded_file:

    if uploaded_file.name.endswith(".pdf"):

        pdf_reader = PdfReader(uploaded_file)

        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                resume_text += text

    else:
        resume_text = uploaded_file.read().decode("utf-8")

    st.success("✅ Resume uploaded successfully!")

    with st.expander("View Resume"):
        st.write(resume_text[:3000])



generate = st.button(
    "🚀 Generate Personalized Interview Questions",
    use_container_width=True
)




if generate:

    with st.spinner("Generating Interview Questions..."):

        if resume_text.strip():

            prompt = f"""
You are an expert technical interviewer.

Role: {role}

Difficulty: {difficulty}

Candidate Resume:

{resume_text}

TASK:

Generate EXACTLY 10 interview questions.

Question 1-7:
Technical questions based on skills, projects, tools and technologies found in the resume.

Question 8-9:
Project based questions from the resume.

Question 10:
HR or behavioral question.

IMPORTANT:

- Output EXACTLY 10 questions.
- Number each question.
- Do NOT provide answers.
- Do NOT provide explanations.
- Do NOT provide introductions.
- Do NOT stop before Question 10.

Format:

1. Question
2. Question
3. Question
4. Question
5. Question
6. Question
7. Question
8. Question
9. Question
10. Question
"""

        else:

            prompt = f"""
You are an expert technical interviewer.

Role: {role}

Difficulty: {difficulty}

Generate EXACTLY 10 interview questions.

Difficulty Rules:

Beginner:
Easy conceptual questions.

Intermediate:
Practical coding and implementation questions.

Advanced:
Real-world scenario and architecture questions.

IMPORTANT:

- Output EXACTLY 10 questions.
- Number each question.
- Do NOT provide answers.
- Do NOT provide explanations.

Format:

1. Question
2. Question
3. Question
4. Question
5. Question
6. Question
7. Question
8. Question
9. Question
10. Question
"""

        
try:

    if resume_text.strip():

        prompt = f"""
You are a technical interviewer.

Role: {role}

Difficulty: {difficulty}

Resume:

{resume_text}

Generate EXACTLY 5 interview questions.

Rules:
- Questions must come from resume skills.
- Questions must come from projects.
- Questions must match the selected role.
- Return ONLY 5 numbered questions.
- Do not provide answers.

Format:

1. Question
2. Question
3. Question
4. Question
5. Question
"""

    else:

        prompt = f"""
You are a technical interviewer.

Role: {role}

Difficulty: {difficulty}

Generate EXACTLY 5 interview questions.

Beginner:
Basic concepts.

Intermediate:
Practical coding questions.

Advanced:
Real-world scenarios.

Return ONLY 5 numbered questions.

1. Question
2. Question
3. Question
4. Question
5. Question
"""

    response = model.generate_text(prompt)

    st.success("✅ Interview Questions Generated Successfully!")

    st.markdown("## 📋 Generated Questions")

    st.text_area(
        "Interview Questions",
        value=response,
        height=350
    )

except Exception as e:

    st.error(f"Error: {e}")





st.sidebar.title("📌 Features")

st.sidebar.success("Resume Based Questions")
st.sidebar.success("Role Based Questions")
st.sidebar.success("IBM Granite AI")
st.sidebar.success("Personalized Interview Prep")

st.sidebar.markdown("---")

st.sidebar.info("""
Upcoming Features

🎤 Mock Interview

📊 Resume Analysis

⭐ AI Scoring

📈 Performance Dashboard
""")

