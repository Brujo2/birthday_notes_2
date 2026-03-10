import streamlit as st
import random
import time

# Page Config for Mobile
st.set_page_config(page_title="To My Forever", page_icon="❤️", layout="centered")

# Custom CSS for the "Soft Warm" Look
st.markdown("""
    <style>
    .stApp {
        background-color: #FFF5F5;
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
        background-color: #FFB6C1;
        color: white;
        border-radius: 25px;
        padding: 10px 25px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #FF8C94;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# The Message Database (Expand this to 100!)
messages = messages = [
    # --- The Classics & Your Requests ---
    "I know I am very hot.",
    "Watching you be a mom is my favorite thing.",
    "You’re the reason our house feels like home.",
    "I’d choose you again every single time.",
    "Ten years down, a lifetime to go.",
    "You are the heartbeat of this family.",
    "You are my best friend and my greatest adventure.",
    "I love the life we’ve built together.",
    "You still take my breath away, just like day one.",
    "Thank you for saying 'Yes' ten years ago.",

    # --- About the Kids & Family ---
    "Our kids are so lucky to have your heart as their guide.",
    "Thank you for loving [Stepson's Name] with a love that knows no bounds.",
    "The way you handle the chaos of three kids with such grace is a miracle.",
    "I see so much of your beauty in our children’s smiles.",
    "You make parenting look like an art form.",
    "Thank you for every sleepless night and every packed lunch.",
    "Our boys are going to grow up to be great men because they have you.",
    "You are the glue that keeps us all together.",
    "Seeing you with the kids is when I love you the most.",
    "Our family is your greatest masterpiece.",

    # --- Romantic & Emotional ---
    "You are my safe harbor in every storm.",
    "I still get butterflies when I hear your laugh.",
    "My favorite place in the world is right next to you.",
    "You are the most beautiful woman I have ever known.",
    "Thank you for being my peace in a loud world.",
    "I love you more than words could ever capture.",
    "You are the poetry I never knew I could write.",
    "Everything good in my life started with you.",
    "You are my sun, my moon, and all my stars.",
    "Your love is the greatest gift I’ve ever received.",

    # --- Short & Sweet (Haiku Style / Short) ---
    "Ten years of magic / Three kids and a heart so full / You are my always.",
    "Your smile is my home.",
    "Forever isn't long enough.",
    "My soul honors yours.",
    "Home is wherever you are.",
    "You + Me = Everything.",
    "Still crushing on you.",
    "Grace in every step.",
    "Love lives in your hug.",
    "You are my 'once in a lifetime'.",

    # --- Appreciation & Partnership ---
    "Thank you for being my teammate in this crazy life.",
    "I appreciate every little thing you do for us.",
    "You make the hard days easy and the good days unforgettable.",
    "Thank you for believing in me when I didn't believe in myself.",
    "I love the way you think and the way you care.",
    "You are the smartest, strongest person I know.",
    "Thank you for the last 3,650 days of happiness.",
    "I love our late-night talks and our early-morning coffee.",
    "You are my favorite person to grow old with.",
    "Life with you is a dream I never want to wake up from.",

    # --- Add 50 more variations of these to reach 100 ---
    "You’re still the one.",
    "I love our 'us' time.",
    "You are remarkably beautiful.",
    "Thank you for your endless patience.",
    "Our kids have the best mom in the universe.",
    "I love your soul.",
    "You are my North Star.",
    "Thank you for the 10 best years of my life.",
    "You are my world.",
    "I'm so proud to be your husband.",
    "To the moon and back.",
    "You are simply incredible.",
    "My heart is yours forever.",
    "You make me a better man.",
    "I love the way you love us.",
    "You are my favorite view.",
    "Every day is better with you.",
    "You are pure sunshine.",
    "I love our little tribe.",
    "You are my dream come true.",
    "Thank you for choosing me.",
    "You are the queen of this house.",
    "I love your laugh.",
    "You are my everything.",
    "Cheers to 10 more years.",
    "You are a blessing.",
    "I adore you.",
    "You are my soulmate.",
    "I love our life.",
    "You are so special to me.",
    "I cherish you.",
    "You are my light.",
    "I am yours, always.",
    "You are stunning.",
    "I love our family adventures.",
    "You are my heart's desire.",
    "Thank you for being you.",
    "I love you endlessly.",
    "You are my treasure.",
    "I'm so lucky.",
    "You are the best part of my day.",
    "I love you to infinity.",
    "You are my sunshine.",
    "I love you more today than yesterday.",
    "You are my forever love.",
    "I love our home because you're in it.",
    "You are a wonder.",
    "I love you, babe.",
    "You are the love of my life.",
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
if st.button("✨ Give me a love note"):
    # Simple "Star" animation feel by clearing and re-running
    with st.spinner("Thinking of a reason..."):
        time.sleep(0.5)
        st.session_state.current_note = random.choice(messages)
        st.rerun()


st.markdown("<p style='text-align: center; color: #BC8F8F; font-size: 12px;'>Forever Yours | 10 Years</p>", unsafe_allow_html=True)
