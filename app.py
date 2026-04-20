import streamlit as st
import random

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(page_title="Thursday Game Night 💜", layout="centered")

# -----------------------
# CUSTOM STYLE
# -----------------------
st.markdown("""
    <style>
        .main {
            text-align: center;
        }
        h1 {
            color: #ff4b6e;
        }
        .stButton>button {
            background-color: #ff4b6e;
            color: white;
            border-radius: 12px;
            height: 3em;
            width: 100%;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------
# TITLE
# -----------------------
st.title("💜 Reema & Daniel's Thursday Game Night")
st.write("Pick a vibe. Or let fate decide 😉")

# -----------------------
# GAME LIST
# -----------------------
games = [
    "🍳 PlateUp!",
    "🎨 Pictionary",
    "♟ Chess",
    "🎲 Müller",
    "🔵 Chinese Checkers",
    "🎯 Yahtzee",
    "👑 Ludo",
    "🧩 It Takes Two"
]

# -----------------------
# SESSION STATE
# -----------------------
if "votes" not in st.session_state:
    st.session_state.votes = {game: 0 for game in games}

# -----------------------
# VOTING
# -----------------------
st.subheader("🗳 Who's feeling what tonight?")

for game in games:
    col1, col2 = st.columns([3, 1])

    with col1:
        st.write(game)
    with col2:
        if st.button("Vote 👍", key=game):
            st.session_state.votes[game] += 1

# -----------------------
# SHOW VOTES
# -----------------------
st.subheader("📊 Current Mood")
st.bar_chart(st.session_state.votes)

# -----------------------
# RANDOM PICK
# -----------------------
st.subheader("🎲 Chaos Button")

if st.button("Surprise Us 🎲"):
    winner = random.choice(games)
    st.success(f"Tonight, you’re playing: **{winner}** 💥")

# -----------------------
# TOP PICK
# -----------------------
if st.button("Go With The Mood 🏆"):
    max_votes = max(st.session_state.votes.values())
    top_games = [g for g, v in st.session_state.votes.items() if v == max_votes]

    if max_votes == 0:
        st.warning("No votes yet 👀")
    else:
        winner = random.choice(top_games)
        st.success(f"Consensus says: **{winner}** 🏆")

# -----------------------
# RESET
# -----------------------
if st.button("Reset Night 🔄"):
    st.session_state.votes = {game: 0 for game in games}
    st.rerun()

# -----------------------
# FOOTER
# -----------------------
st.markdown("---")
st.caption("Made for cozy chaos 💜")