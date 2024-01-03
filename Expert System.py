import streamlit as st

def one_piece_expert_system(problem):
    rules = [
        {"problem": "Luffy is in trouble", "solution": "Summon the crew and prepare for an adventure!"},
        {"problem": "Zoro lost his way", "solution": "Look for three directions and wait for Zoro to find his way back."},
        {"problem": "Nami needs help", "solution": "Assist Nami with navigation or any weather-related issues."},
        {"problem": "Sanji is cooking", "solution": "Wait eagerly for Sanji's delicious meal."},
    ]

    for rule in rules:
        if problem.lower() in rule['problem'].lower():
            return rule['solution']

    return "No solution found."

st.title("One Piece Expert System")

problem = st.text_input("Enter your problem")

if not problem:
    st.warning("Please enter a problem.")
else:
    solution = one_piece_expert_system(problem)

    st.subheader("Solution:")
    st.write(solution)

    # Add images/icons based on the selected problem
    if "Luffy" in problem:
        sst.image("download (1).jpeg", caption="Luffy", use_column_width=True)
    elif "Zoro" in problem:
        st.image("download.jpeg", caption="Zoro", use_column_width=True)
    elif "Nami" in problem:
        st.image("download (3).jpeg", caption="Nami", use_column_width=True)
    elif "Sanji" in problem:
        st.image("download (2).jpeg", caption="Sanji", use_column_width=True)




