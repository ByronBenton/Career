import streamlit as st
import pandas as pd

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
    {
        "career": "Cybersecurity Analyst",
        "skills": ["Networking", "Linux", "Security", "Python", "Penetration Testing"],
        "interests": ["Security", "Networking", "Ethical Hacking"],
        "experience": ["Intermediate", "Advanced"],
        "learn_next": ["Cloud Security", "Threat Analysis", "Incident Response"],
        "courses": [
            {"name": "TryHackMe", "link": "https://tryhackme.com/"},
            {"name": "Cybrary", "link": "https://www.cybrary.it/"}
        ]
    },
    {
        "career": "Business Analyst",
        "skills": ["Excel", "SQL", "Communication", "Power BI", "Data Analysis"],
        "interests": ["Business", "Data", "Management"],
        "experience": ["Beginner", "Intermediate"],
        "learn_next": ["Stakeholder Management", "Process Optimization"],
        "courses": [
            {"name": "Coursera - Business Analytics", "link": "https://www.coursera.org/specializations/business-analytics"}
        ]
    },
    {
        "career": "UI/UX Designer",
        "skills": ["Figma", "Adobe XD", "Wireframing", "Prototyping", "User Research"],
        "interests": ["Design", "Creativity", "User Experience"],
        "experience": ["Beginner", "Intermediate"],
        "learn_next": ["Interaction Design", "Design Systems", "Accessibility"],
        "courses": [
            {"name": "Coursera - UI/UX Design", "link": "https://www.coursera.org/specializations/ui-ux-design"},
            {"name": "Interaction Design Foundation", "link": "https://www.interaction-design.org/"}
        ]
    },
    {
        "career": "Mobile App Developer",
        "skills": ["Flutter", "Kotlin", "Swift", "Java", "APIs"],
        "interests": ["Mobile", "Apps", "Innovation"],
        "experience": ["Intermediate", "Advanced"],
        "learn_next": ["Cross-Platform Development", "App Store Deployment"],
        "courses": [
            {"name": "Udemy - Flutter Development", "link": "https://www.udemy.com/course/flutter-dart-the-complete-flutter-app-development-course/"},
            {"name": "Ray Wenderlich Tutorials", "link": "https://www.raywenderlich.com/"}
        ]
    },
    {
        "career": "Cloud Engineer",
        "skills": ["AWS", "Azure", "Docker", "Kubernetes", "Python"],
        "interests": ["Cloud", "Infrastructure", "DevOps"],
        "experience": ["Intermediate", "Advanced"],
        "learn_next": ["Terraform", "CI/CD", "Serverless Architecture"],
        "courses": [
            {"name": "AWS Training", "link": "https://aws.amazon.com/training/"},
            {"name": "Cloud Academy", "link": "https://cloudacademy.com/"}
        ]
    },
    {
        "career": "Digital Marketing Specialist",
        "skills": ["SEO", "Content Marketing", "Google Analytics", "Social Media", "Copywriting"],
        "interests": ["Marketing", "Content", "Growth"],
        "experience": ["Beginner", "Intermediate"],
        "learn_next": ["Email Marketing", "Paid Ads", "Marketing Automation"],
        "courses": [
            {"name": "Google Digital Garage", "link": "https://learndigital.withgoogle.com/digitalgarage"},
            {"name": "HubSpot Academy", "link": "https://academy.hubspot.com/"}
        ]
    },
    {
        "career": "Game Developer",
        "skills": ["C++", "Unity", "Unreal Engine", "3D Modeling", "Python"],
        "interests": ["Gaming", "Graphics", "AI"],
        "experience": ["Intermediate", "Advanced"],
        "learn_next": ["Shader Programming", "Game Physics", "VR/AR Development"],
        "courses": [
            {"name": "Unity Learn", "link": "https://learn.unity.com/"},
            {"name": "Unreal Online Learning", "link": "https://www.unrealengine.com/en-US/onlinelearning-courses"}
        ]
    }
]

df = pd.DataFrame(career_data)

# --------------------------------------------------
# "More Info" Links
# --------------------------------------------------
more_info_links = {
    "Data Scientist": "https://en.wikipedia.org/wiki/Data_science",
    "AI Engineer": "https://www.coursera.org/articles/artificial-intelligence-career-path",
    "Web Developer": "https://www.linkedin.com/pulse/complete-guide-careers-25-fields-you-can-explore-tech-faisal-tahir-58uie",
    "Cybersecurity Analyst": "https://joinhandshake.com/blog/students/types-of-it-careers/",
    "Business Analyst": "https://joinhandshake.com/blog/students/types-of-it-careers/",
    "UI/UX Designer": "https://careerfoundry.com/en/blog/career-change/which-tech-career-path-is-right-for-me/",
    "Mobile App Developer": "https://www.linkedin.com/pulse/complete-guide-careers-25-fields-you-can-explore-tech-faisal-tahir-58uie",
    "Cloud Engineer": "https://ccitraining.edu/blog/future-proof-entry-level-it-jobs-in-the-age-of-ai/",
    "Digital Marketing Specialist": "https://careerfoundry.com/en/blog/career-change/which-tech-career-path-is-right-for-me/",
    "Game Developer": "https://www.linkedin.com/pulse/complete-guide-careers-25-fields-you-can-explore-tech-faisal-tahir-58uie"
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
            "Courses": row["courses"]
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

            if ready_now:
                st.subheader("✅ Ready Now")
                for r in ready_now:
                    with st.expander(f"**{r['Career']}**"):
                        st.markdown(f"**Match Score:** {r['Match Score']}")
                        st.markdown(f"**Skills to Learn:** {', '.join(r['Skills to Learn'][:3])} 🛠️")
                        course_links = [f"[🔗 {c['name']}]({c['link']})" for c in r['Courses'][:2]]
                        st.markdown("**Courses:** " + ", ".join(course_links))
                        st.markdown(f"[🔍 More Info]({more_info_links.get(r['Career'], '#')})")

            if skill_up:
                st.subheader("📘 Skill-Up Needed")
                for r in skill_up:
                    with st.expander(f"**{r['Career']}**"):
                        st.markdown(f"**Match Score:** {r['Match Score']}")
                        st.markdown(f"**Skills to Learn:** {', '.join(r['Skills to Learn'][:3])} 🛠️")
                        course_links = [f"[🔗 {c['name']}]({c['link']})" for c in r['Courses'][:2]]
                        st.markdown("**Courses:** " + ", ".join(course_links))
                        st.markdown(f"[🔍 More Info]({more_info_links.get(r['Career'], '#')})")

