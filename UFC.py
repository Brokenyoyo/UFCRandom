import streamlit as st
import random
import time

restaurants = [
    "Yuliana's Mexican Food",
    "Taco Bell",
    "Popeyes",
    "Wingstop",
    "Barros Pizza",
    "Jack in the Box",
    "In-N-Out Burger",
    "Moku Hawaiian Grill"
]

st.set_page_config(page_title="Fast Food Roulette 🍔🌮", layout="centered")

st.title("🍔🌮 Fast Food Roulette 🌮🍔")
st.markdown("When the group is hangry and nobody wants to decide.")

if st.button("🎲 SPIN THE WHEEL!", type="primary", use_container_width=True, help="May the odds be ever in your flavor"):
    with st.spinner("Consulting the drive-thru oracle..."):
        time.sleep(1.4)

    winner = random.choice(restaurants)

    st.success("**The food gods have spoken:**")
    st.header(f"🍟 **{winner.upper()}** 🍟", anchor=False)

    comments = {
        "Yuliana's Mexican Food": "Carne asada fries and horchata loading... 🌯🥤",
        "Taco Bell": "Live más. Crunchwrap supremacy activated.",
        "Popeyes": "Blackened ranch + biscuit combo = life choices.",
        "Wingstop": "Louisiana rub or atomic? Commit to the heat level.",
        "Barros Pizza": "That cheese pull is illegal in 17 states 🍕",
        "Jack in the Box": "Curly fries and tacos at 3 a.m. — iconic.",
        "In-N-Out Burger": "Double-Double Animal Style. No notes. 🍔✨",
        "Moku Hawaiian Grill": "Loco moco + mac salad = happiness achieved 🏝️🍲"
    }

    st.info(comments.get(winner, "Enjoy your meal!"))

    st.balloons()

st.markdown("---")
st.caption("Made for quick group decisions • Share this page!")