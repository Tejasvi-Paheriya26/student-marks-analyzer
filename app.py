import streamlit as st
import pandas as pd

# Title
st.title("📊 Student Marks Analyzer with Visualization")

# Input fields
name = st.text_input("Enter Student Name")

m1 = st.number_input("Marks for Subject 1", min_value=0, max_value=100)
m2 = st.number_input("Marks for Subject 2", min_value=0, max_value=100)
m3 = st.number_input("Marks for Subject 3", min_value=0, max_value=100)

# Button to calculate results
if st.button("Calculate"):
    # Calculate total and average
    total = m1 + m2 + m3
    average = total / 3

    # Determine grade
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "Fail"

    # Display results
    st.subheader("📋 Results")
    st.write(f"**Student Name:** {name}")
    st.write(f"**Total Marks:** {total}")
    st.write(f"**Average Marks:** {average:.2f}")
    st.write(f"**Grade:** {grade}")

    # Prepare data for visualization
    data = {
        "Subjects": ["Subject 1", "Subject 2", "Subject 3"],
        "Marks": [m1, m2, m3]
    }
    df = pd.DataFrame(data).set_index("Subjects")

    # Visualizations
    st.subheader("📊 Marks Comparison (Bar Chart)")
    st.bar_chart(df)

    st.subheader("📈 Marks Trend (Line Chart)")
    st.line_chart(df)

    st.subheader("📑 Marks Table")
    st.dataframe(df)