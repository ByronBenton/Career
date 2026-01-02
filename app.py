import streamlit as st
import pandas as pd
#import plotly.graph_objects as go

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(page_title="Career Recommendation App", layout="centered")

st.title("🎯 Career Advice Recommendation System")
st.write("Get personalized career guidance based on your skills, interests, and experience.")

# --------------------------------------------------
# Career Dataset with working course links
# --------------------------------------------------
career_data = [
    {
        "career": "Data Scientist",
        "skills": ["Python", "Statistics", "Machine Learning", "SQL", "Data Analysis"],
        "interests": ["Data", "AI", "Research"],
        "experience": ["Intermediate", "Advanced"],
        "learn_next": ["Deep Learning", "Big Data", "Data Visualization"],
        "courses": [
            {"name": "Coursera - Data Science", "link": "https://www.coursera.org/specializations/jhu-data-science"},
            {"name": "Kaggle Learn", "link": "https://www.kaggle.com/learn/overview"}
        ]
    },
    {
        "career": "AI Engineer",
        "skills": ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch"],
        "interests": ["AI", "Robotics"],
        "experience": ["Advanced"],
        "learn_next": ["MLOps", "Model Deployment", "Reinforcement Learning"],
        "courses": [
            {"name": "DeepLearning.AI", "link": "https://www.deeplearning.ai/"},
            {"name": "Fast.ai", "link": "https://www.fast.ai/"}
        ]
    },
    {
        "career": "Web Developer",
        "skills": ["HTML", "CSS", "JavaScript", "React", "Node.js"],
        "interests": ["Web", "Design", "UI/UX"],
        "experience": ["Beginner", "Intermediate"],
        "learn_next": ["Next.js", "APIs", "Responsive Design"],
        "courses": [
            {"name": "freeCodeCamp", "link": "https://www.freecodecamp.org/"},
            {"name": "MDN Web Docs", "link": "https://developer.mozilla.org/en-US/docs/Learn"}
        ]
    },
    # ... (other careers omitted for brevity, add all careers from your original dataset)
]

df = pd.DataFrame(career_data)

# --------------------------------------------------
# More Info, Trends, Success Signals, Salary
# --------------------------------------------------
more_info_links = {
    "Data Scientist": "https://en.wikipedia.org/wiki/Data_science",
    "AI Engineer": "https://www.coursera.org/articles/artificial-intelligence-career-path",
    "Web Developer": "https://www.linkedin.com/pulse/complete-guide-careers-25-fields-you-can-explore-tech-faisal-tahir-58uie",
    # ... add all others
}

# Mock trend data
job_trends = {
    "Data Scientist": "Demand for AI & ML skills is growing 15% this year 📈",
    "AI Engineer": "AI Engineer roles requiring Deep Learning are growing 20% 📈",
    "Web Developer": "Web Developer roles are steady ⚖️",
    # ... add more as needed
}

# Mock success signals
success_signals = {
    "Data Scientist": "Users who learned Deep Learning after Python had +80% success rate ✅",
    "AI Engineer": "Users mastering TensorFlow & PyTorch had +75% chance of landing the role ✅",
    "Web Developer": "Learning React & Node.js increased job success by +70% ✅",
}

# Mock salary ranges
salary_ranges = {
    "Data Scientist": " $70k - $120k",
    "AI Engineer": " $80k - $140k",
    "Web Developer": " $50k - $100k",
}

# --------------------------------------------------
# User Inputs
# --------------------------------------------------
st.subheader("🧑‍💼 Tell Us About You")

all_skills = sorted({skill for skills in df["skills"] for skill in skills})
all_interests = sorted({i for interests in df["interests"] for i in interests})

user_skills = st.multiselect("Select your skills:", all_skills, help="Pick skills you are familiar with.")
user_interests = st.multiselect("Select your interests:", all_interests, help="Pick topics you enjoy.")
experience = st.selectbox("Experience Level:", ["Beginner", "Intermediate", "Advanced"], index=0, help="Choose your experience level.")

# --------------------------------------------------
# Recommendation Logic
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

        career_min_level = min(experience_levels.index(e) for e in row["experience"])
        experience_gap = career_min_level - user_level
        score = skill_match * 2 + interest_match - max(experience_gap, 0)

        readiness = "Ready now ✅" if experience_gap <= 0 else "Skill-up needed 📘"

        recommendations.append({
            "Career": row["career"],
            "Match Score": score,
            "Readiness": readiness,
            "Skills to Learn": row["learn_next"],
            "Courses": row["courses"],
            "Required Skills": row["skills"]
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
            ready_now = [r for r in results if r["Readiness"] == "Ready now ✅"]
            skill_up = [r for r in results if r["Readiness"] == "Skill-up needed 📘"]

            def display_career(r):
                with st.expander(f"**{r['Career']}**"):
                    st.markdown(f"**Match Score:** {r['Match Score']}")
                    
                    # Skill gap calculation
                    total_skills = len(r['Required Skills'])
                    user_skill_count = len(set(user_skills) & set(r['Required Skills']))
                    progress = int(user_skill_count / total_skills * 100)
                    st.progress(progress)
                    st.markdown(f"**Skills Acquired:** {user_skill_count}/{total_skills} ({progress}%)")
                    
                    # Trend & Success
                    st.markdown(f"**Trend Insight:** {job_trends.get(r['Career'], 'No trend data available.')}")
                    st.markdown(f"**Success Signal:** {success_signals.get(r['Career'], 'No data available.')}")
                    st.markdown(f"**Salary Range:** {salary_ranges.get(r['Career'], 'N/A')}")
                    
                    # Skills to Learn & Courses
                    st.markdown(f"**Skills to Learn:** {', '.join(r['Skills to Learn'])} 🛠️")
                    course_links = [f"[🔗 {c['name']}]({c['link']})" for c in r['Courses']]
                    st.markdown("**Courses:** " + ", ".join(course_links))
                    st.markdown(f"[🔍 More Info]({more_info_links.get(r['Career'], '#')})")

            if ready_now:
                st.subheader("✅ Ready Now")
                for r in ready_now:
                    display_career(r)

            if skill_up:
                st.subheader("📘 Skill-Up Needed")
                for r in skill_up:
                    display_career(r)

