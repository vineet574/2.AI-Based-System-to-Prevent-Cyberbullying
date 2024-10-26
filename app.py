import streamlit as st

# List of bullying keywords (this is a basic example; it can be expanded)
bullying_keywords = ["stupid", "loser", "hate", "dumb", "idiot", "ugly", "fat", "worthless", "fail", "useless"]

def check_text_for_bullying(text):
    # Check if any bullying keyword is in the user text
    flagged_words = [word for word in bullying_keywords if word in text.lower()]
    if flagged_words:
        return True, flagged_words
    return False, []

# Streamlit UI setup
st.title("AI-Based Cyberbullying Detection System")
st.write("Type a message to check if it contains harmful or bullying language:")

# User input
user_text = st.text_area("Your Message", "")

# Check for bullying keywords
if st.button("Analyze"):
    is_bullying, flagged_words = check_text_for_bullying(user_text)
    if is_bullying:
        st.error(f"Warning: Potential bullying language detected! Flagged words: {', '.join(flagged_words)}")
    else:
        st.success("No bullying language detected. You're good to go!")

