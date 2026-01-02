import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(page_title="Career Recommendation App", layout="centered")

st.title("🎯 Career Advice Recommendation System")
st.write("Get personalized career guidance based on your skills, interests, and experience.")

# --------------------------------------------------
# Expanded Career Dataset
# --------------------------------------------------
career_data = [
    {
        "career": "Data Scientist",
        "skills": ["Python", "Statistics", "Machine Learning", "SQL", "Data Analysis"],
        "interests": ["Data", "AI", "Research"],
        "experience": ["Intermediate", "Advanced"],
        "learn_next": ["Deep Learning", "Big Data", "Data Visualization"],
        "courses": ["Coursera - Data Science", "Kaggle Learn"]
    },
    {
        "career": "AI Engineer",
        "skills": ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch"],
        "interests": ["AI", "Robotics"],
        "experience": ["Advanced"],
        "learn_next": ["MLOps", "Model Deployment", "Reinforcement Learning"],
        "courses": ["DeepLearning.AI", "Fast.ai"]
    },
    {
        "career": "Web Developer",
        "skills": ["HTML", "CSS", "JavaScript", "React", "Node.js"],
        "interests": ["Web", "Design", "UI/UX"],
        "experience": ["Beginner", "Intermediate"],
        "learn_next": ["Next.js", "APIs", "Responsive Design"],
        "courses": ["freeCodeCamp", "MDN Web Docs"]
    },
    {
        "career": "Cybersecurity Analyst",
        "skills": ["Networking", "Linux", "Security", "Python", "Penetration Testing"],
        "interests": ["Security", "Networking", "Ethical Hacking"],
        "experience": ["Intermediate", "Advanced"],
        "learn_next": ["Cloud Security", "Threat Analysis", "Incident Response"],
        "courses": ["TryHackMe", "Cybrary"]
    },
    {
        "career": "Business Analyst",
        "skills": ["Excel", "SQL", "Communication", "Power BI", "Data Analysis"],
        "interests": ["Business", "Data", "Management"],
        "experience": ["Beginner", "Intermediate"],
        "learn_next": ["Stakeholder Management", "Process Optimization"],
        "courses": ["Coursera - Business Analytics"]
    },
    {
        "career": "UI/UX Designer",
        "skills": ["Figma", "Adobe XD", "Wireframing", "Prototyping", "User Research"],
        "interests": ["Design", "Creativity", "User Experience"],
        "experience": ["Beginner", "Intermediate"],
        "learn_next": ["Interaction Design", "Design Systems", "Accessibility"],
        "courses": ["Coursera - UI/UX Design", "Interaction Design Foundation"]
    },
    {
        "career": "Mobile App Developer",
        "skills": ["Flutter", "Kotlin", "Swift", "Java", "APIs"],
        "interests": ["Mobile", "Apps", "Innovation"],
        "experience": ["Intermediate", "Advanced"],
        "learn_next": ["Cross-Platform Development", "App Store Deployment"],
        "courses": ["Udemy - Flutter Development", "Ray Wenderlich Tutorials"]
    },
    {
        "career": "Cloud Engineer",
        "skills": ["AWS", "Azure", "Docker", "Kubernetes", "Python"],
        "interests": ["Cloud", "Infrastructure", "DevOps"],
        "experience": ["Intermediate", "Advanced"],
        "learn_next": ["Terraform", "CI/CD", "Serverless Architecture"],
        "courses": ["AWS Training", "Cloud Academy"]
    },
    {
        "career": "Digital Marketing Specialist",
        "skills": ["SEO", "Content Marketing", "Google Analytics", "Social Media", "Copywriting"],
        "interests": ["Marketing", "Content", "Growth"],
        "experience": ["Beginner", "Intermediate"],
        "learn_next": ["Email Marketing", "Paid Ads", "Marketing Automation"],
        "courses": ["Google Digital Garage", "HubSpot Academy"]
    },
    {
        "career": "Game Developer",
        "skills": ["C++", "Unity", "Unreal Engine", "3D Modeling", "Python"],
        "interests": ["Gaming", "Graphics", "AI"],
        "experience": ["Intermediate", "Advanced"],
        "learn_next": ["Shader Programming", "Game Physics", "VR/AR Development"],
        "courses": ["Unity Learn", "Unreal Online Learning"]
    }
]

df = pd.DataFrame(career_data)

# --------------------------------------------------
# User Inputs
# --------------------------------------------------
st.subheader("🧑‍💼 Tell Us About You")

all_skills = sorted({skill for skills in df["skills"] for skill in skills})
all_interests = sorted({i for interests in df["interests"] for i in interests})

user_skills = st.multiselect("Select your skills:", all_skills)
user_interests = st.multiselect("Select your interests:", all_interests)
experience = st.selectbox(
    "Experience Level:",
    ["Beginner", "Intermediate", "Advanced"]
)

# --------------------------------------------------
# Recommendation Logic (Soft Experience Matching)
# --------------------------------------------------
def recommend_careers(user_skills, user_interests, experience):
    recommendations = []
    experience_levels = ["Beginner", "Intermediate", "Advanced"]

    user_level = experience_levels.index(experience)

    for _, row in df.iterrows():
        skill_match = len(set(user_skills) & set(row["skills"]))
        interest_match = len(set(user_interests) & set(row["interests"]))

        if skill_match == 0 and interest_match == 0:
            continue

        career_min_level = min(
            experience_levels.index(e) for e in row["experience"]
        )

        experience_gap = career_min_level - user_level

        score = skill_match * 2 + interest_match - max(experience_gap, 0)

        readiness = (
            "Ready now ✅"
            if experience_gap <= 0
            else "Skill-up needed 📘"
        )

        recommendations.append({
            "Career": row["career"],
            "Match Score": score,
            "Readiness": readiness,
            "Skills to Learn": ", ".join(row["learn_next"]),
            "Courses": ", ".join(row["courses"])
        })

    return sorted(recommendations, key=lambda x: x["Match Score"], reverse=True)

# --------------------------------------------------
# Show Recommendations
# --------------------------------------------------
if st.button("🔍 Get Career Recommendations"):
    if not user_skills and not user_interests:
        st.warning("Please select at least one skill or interest.")
    else:
        results = recommend_careers(user_skills, user_interests, experience)

        if not results:
            st.info("No strong matches found. Try adding more skills or interests.")
        else:
            st.subheader("🚀 Recommended Career Paths")

            for r in results:
                st.success(
                    f"""
                    **Career:** {r['Career']}  
                    **Match Score:** {r['Match Score']}  
                    **Readiness:** {r['Readiness']}  
                    **Skills to Learn:** {r['Skills to Learn']}  
                    **Courses:** {r['Courses']}
                    """
                )
