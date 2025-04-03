import streamlit as st

# App title and introduction
st.title("Growth Mindset Challenge Quiz")
st.write("This quiz will tell you whether your mindset is Growth or Fixed. Choose your answers honestly!")

# Get user's name
naam = st.text_input("What is your name?")

# Quiz questions
st.subheader("Start the Quiz")
score = 0  # To track the score

# Question 1
q1 = st.radio(
    "Question 1: If you fail at something, what do you think?",
    ("A) I can never be good at this.", "B) This is an opportunity to learn.")
)
if q1 == "B) This is an opportunity to learn.":
    score += 1

# Question 2
q2 = st.radio(
    "Question 2: When faced with a difficult task, what do you do?",
    ("A) Give up because it’s not my thing.", "B) Try and find new ways to solve it.")
)
if q2 == "B) Try and find new ways to solve it.":
    score += 1

# Question 3
q3 = st.radio(
    "Question 3: How do you feel when you see others succeed?",
    ("A) Jealous or feel inferior.", "B) Inspired and motivated to learn.")
)
if q3 == "B) Inspired and motivated to learn.":
    score += 1

# Button to show results
if st.button("Show My Result"):
    if naam:
        st.write(f"Hello, {naam}! Your quiz is complete. Let’s see your result...")
        if score == 3:
            st.success("Your mindset is fully **Growth Mindset**! You’re ready to learn and grow—amazing job!")
        elif score == 2:
            st.success("Your mindset leans mostly toward **Growth Mindset**. With a little effort, you can improve even more!")
        elif score == 1:
            st.warning("Your mindset is a mix of **Fixed** and **Growth**. See every challenge as a chance to grow!")
        else:
            st.warning("Your mindset is currently **Fixed Mindset**. Don’t worry, small steps can lead you to a Growth Mindset!")
    else:
        st.error("Please enter your name first!")

# Growth Mindset tip
st.write("**Tip:** A Growth Mindset means seeing every difficulty as a chance to learn. Keep trying!")