import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="Financial Consultant Dashboard")
st.title("Financial Consultant Job Profile Report")

# --- DATA ---
data = [
    # Personal
    ["Personal", "Communication Skills", 10, 60, None, 40, 90, 9, "Appearance ★★☆"],
    ["Personal", "Critical Thinking", 5, None, 60, 40, 70, 4, "Attitude ★★☆"],
    ["Personal", "Attention to Detail", 5, None, 80, 20, 60, 3, ""],
    ["Personal", "Time Management", 5, 80, 20, None, 30, 2, ""],
    ["Personal", "Ethical Judgment", 3, None, None, 100, 85, 3, ""],
    ["Personal", "Ownership", 2, None, 20, 80, 60, 1, ""],

    # Business
    ["Business", "Financial Planning", 10, None, 60, 40, 50, 5, "Presentation ★★☆"],
    ["Business", "Budgeting & Cost Control", 5, None, 60, 40, 70, 4, "English speaking ★★☆"],
    ["Business", "Reporting & Compliance", 5, None, 80, 20, 60, 3, ""],
    ["Business", "Decision-Making", 5, 80, None, 20, 30, 2, ""],
    ["Business", "Stakeholder Communication", 5, 50, None, 50, 60, 3, ""],

    # Technical
    ["Technical", "Oracle Financials Navigation", 5, None, 60, 40, 80, 4, "Anxious ★★☆"],
    ["Technical", "Chart of Accounts Configuration", 5, None, 60, 40, 100, 5, ""],
    ["Technical", "General Ledger Management", 5, None, 80, 20, 99, 5, ""],
    ["Technical", "Receivables/Payables Setup", 5, None, 80, 20, 99, 5, ""],
    ["Technical", "Security and Auditing", 5, None, 50, 50, 80, 4, ""],
    ["Technical", "Reporting Customization", 5, None, 80, 20, 85, 4, ""],
    ["Technical", "Budget Module Configuration", 2, None, 80, 20, 80, 2, ""],
    ["Technical", "Ledger Integration", 3, None, 80, 20, 70, 2, ""],
    ["Technical", "Error Resolution & Logs", 3, None, 90, 10, 65, 2, ""],
    ["Technical", "Costing Methods Application", 2, None, 90, 10, 90, 2, ""]
]

columns = ["Category", "Skill", "Weight %", "System", "Assignment", "Human", "Grade", "Skill %", "TA"]
df = pd.DataFrame(data, columns=columns)
df["Weighted %"] = (df["Weight %"] * df["Skill %"] / 100).round(0)

# --- SECTION DISPLAY ---
def display_section(title, df_section, target):
    st.markdown(f"### {title} ({target}%)")
    achieved = int(df_section["Weighted %"].sum())
    st.markdown(f"**Achieved: {achieved}%**")

    st.dataframe(df_section.set_index("Skill")[
        ["Weight %", "System", "Assignment", "Human", "Grade", "Skill %", "TA"]
    ])

    fig = px.bar(
        df_section,
        y="Skill",
        x="Skill %",
        orientation='h',
        text="Skill %",
        title=f"{title} - Skill %",
        labels={"Skill %": "Score %"},
        color="Category"
    )
    fig.update_layout(yaxis=dict(categoryorder='total ascending'))
    st.plotly_chart(fig, use_container_width=True)

# --- MAIN LAYOUT ---
tabs = st.tabs(["Personal Skills", "Business Skills", "Technical Skills"])

with tabs[0]:
    display_section("Personal and Attitude Skills", df[df.Category == "Personal"], 30)

with tabs[1]:
    display_section("Business Skills", df[df.Category == "Business"], 30)

with tabs[2]:
    display_section("Technical Skills", df[df.Category == "Technical"], 40)

# --- TOTAL ---
total = int(df["Weighted %"].sum())
st.markdown("### Total Skill Percentage")
st.markdown(f"**Target: 100% — Achieved: {total}%**")
