import streamlit as st
import random
import time

# Page Config for Mobile
st.set_page_config(page_title="To My Girl", page_icon="❤️", layout="centered")

# Custom CSS for the "Soft Warm" Look
st.markdown("""
    <style>
    .stApp {
        background-color: #eea990;
    }
    .love-card {
        background-color: #FFFFFF;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(255, 182, 193, 0.3);
        text-align: center;
        border: 1px solid #FFD1DC;
    }
    .quote-text {
        font-family: 'Georgia', serif;
        color: #5D4037;
        font-size: 24px;
        font-style: italic;
        line-height: 1.6;
    }
    .stButton>button {
        background-color: #f5bd3d;
        color: green;
        border-radius: 25px;
        padding: 10px 25px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #f6e0b5;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# The Message Database 
messages = messages = [
    # --- The Classics & Your Requests ---
    "Do you know you are very hot? Now you do!",
    "Watching you be a mom is one of my favorite things.",
    "You’re the reason our house feels like home.",
    "Ten years down, a lifetime to go.",
    "You are the heartbeat of this family.",
    "Be weird and wild with me.",
    "I love the life we’ve built together.",
    "You and me raving until sunrise in another country.",
    "Thank you for saying 'Yes' ten years ago.",
    "Got a weird feeling we going to be rich as fuck soon.",
     "Love, light and fuck the system.",
     "Everything is gonna work out for us and our family.",
     "Don’t be surprised when life starts going good for you. You deserve it.",
     "No one is you and that is your power.",
     "I l❤️ve fucking you... I mean I fucking l❤️ve you.",
     "Expect good things. Expect Magic. Expect the greatest unfolding for you. Expect positivity to meet you everywhere.",
     "Don’t be afraid to shine. Remember the sun doesn’t give a fuck if it blinds you.",
     "What is coming is better than what is gone.",
     "You are so full of magic you don’t even know.",
     "Actually the grass is greener wherever you stand.",
     "There will be clouds but there will be rainbows too.",
    "Stay happy and full of magic."

    # --- About the Kids & Family ---
    "Our kids are so lucky to have your heart as their guide.",
    "Thank you for loving our family with a love that knows no bounds.",
    "I see so much of your beauty in our children’s smiles.",
    "Thank you for every sleepless night and every packed breakfast.",
    "Our boys are going to grow up to be great men because they have you.",
    "Our family is your greatest masterpiece.",
    "You have entered a chapter where it all goes right."

    # --- Romantic & Emotional ---
    "Thank you for being my peace in a loud world.",
    "You are the poetry I never knew I could write.",
    "Everything good in my life started with you.",
    "Your love is the greatest gift I’ve ever received.",

    # --- Short & Sweet (Haiku Style / Short) ---
    "Ten years of magic.",
    "Home is wherever you are.",
    "You + Me = Everything.",
    "Still crushing on you.",

    # --- Appreciation & Partnership ---
    "Thank you for being my teammate in this crazy life.",
    "I appreciate every little thing you do for us.",
    "You make the hard days easy and the good days unforgettable.",
    "Thank you for believing in me when I didn't believe in myself.",
    "I love the way you think and the way you care.",
    "You are the smartest, strongest person I know.",
    "Thank you for the last almost 10 years.",
    "I love our late-night talks.",
    "You are my favorite person to grow old with.",
    "Life with you is a dream I never want to wake up from.",

    # --- Add 50 more variations of these to reach 100 ---
    "You are stronger than your fears, braver than your doubts, and more beautiful than words can ever say.",
    "Watching you grow, fight, and chase your dreams is one of the greatest privileges of my life.",
    "You are remarkably beautiful.",
    "Thank you for your endless patience.",
    "I love your soul.",
    "You are my North Star.",
    "Your courage, kindness, and love make me proud to call you my wife every day.",
    "I'm so proud to be your husband.",
    "To the moon and back.",
    "You are simply incredible.",
    "You make me a better man.",
    "I love our little tribe.",
    "Whenever life feels heavy, remember you don’t have to carry it alone. I am always here beside you.",
    "Thank you for choosing me.",
    "You are the queen of this house.",
    "I love your laugh.",
    "Cheers to many more years.",
    "You are a blessing.",
    "Even on the days you doubt yourself, remember I see the incredible woman you are.",
    "You are so special to me.",
    "I fell in love with your heart, but I stay in love with your strength every single day.",
    "Your dreams matter to me because you matter to me.",
    "You inspire me every day just by being you.",
    "You are stunning.",
    "I love our family adventures.",
    "No matter how hard the day gets, remember: you are stronger than you think and more loved than you know.",
    "Thank you for being you.",
    "You make life brighter, and I will always be your biggest supporter.",
    "You are the reason I believe beautiful things happen in life.",
    "You are a wonder.",
    "I love you, babe.",
    "Keep shining. The world needs your light.",
    "Happy Birthday to my amazing wife."
]

# State management for the button
if 'current_note' not in st.session_state:
    st.session_state.current_note = messages[0]

st.markdown("<h2 style='text-align: center; color: #D81B60;'>For My Beautiful Wife</h2>", unsafe_allow_html=True)

# The Display Card
st.markdown(f"""
    <div class="love-card">
        <p class="quote-text">"{st.session_state.current_note}"</p>
    </div>
    """, unsafe_allow_html=True)

st.write(" ") # Spacer

# The Interaction
if st.button("✨ Touch me all the time"):
    # Simple "Star" animation feel by clearing and re-running
    with st.spinner("Thinking of a reason..."):
        time.sleep(1.5)
        st.session_state.current_note = random.choice(messages)
        st.rerun()


st.markdown("<p style='text-align: center; color: #ff460f; font-size: 12px;'>Happy Birthday Jule| 10 Years together</p>", unsafe_allow_html=True)







