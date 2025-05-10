import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Koya",
    page_icon="📈",
    layout="wide"
)

# Image file paths
logo = "koya.png"  # Replace with your actual logo file

# Header with logo + title
col1, col2 = st.columns([1, 4])
with col1:
    st.image(logo, use_container_width=True)
with col2:
    st.markdown("""
    <div style='font-size: 38px; color: white;'>
        <br><br>
        <h1 style="color:white;">Koya</h1>
        <h3 style="color:#cccccc;">You trade, we handle the rest.</h3>
        <p>A structure designed to reveal and grow the <strong>best traders on Involio</strong>.</p>
    </div>
    """, unsafe_allow_html=True)

# Problem section
st.header("🕵️ The Problem")
st.markdown("""
- No personal branding  
- No strategy  
- No support  
➡️ **Most good traders remain invisible.**

They stagnate or leave the platform.

**Being good is no longer enough.**

> Creating consistent, professional content requires expertise.  
> That’s not your job. That’s ours.
""")

# Vision section
st.header("🌟 Our Vision")
st.markdown("""
To ensure top traders are no longer overlooked — by giving them structure, visibility, and long-term credibility.

- Identify real talent  
- Centralize and amplify their value  
- Let them focus purely on trading  
""")

# Why now?
st.header("⏱ Why now?")
st.markdown("""
- Involio is growing — but **disorganized**
- No real brand, no team, no structure
- Everyone plays solo

We’re stepping in while the space is still wide open.
""")

# What we offer
st.header("🎯 What We Offer")
st.markdown("""
- 🧱 A stable framework  
- 📊 A structured account ready to perform  
- 🧑‍💻 Two portfolio types under your name  
- 👥 Shared visibility without losing your identity  
- 💰 Increased revenue potential  

**You publish directly via Koya’s account.**

- **Standard**: Free (monetization coming soon)  
- **VIP**: Subscription-based access to your signals  

> Involio will pay for all copied trades — even in non-VIP portfolios.
""")

# What you gain
st.header("📈 What You Gain")
st.markdown("""
- 🧠 Less mental load  
- 🧭 A serious image aligned with your strategy  
- 🔁 Visibility that brings clients and income  

> Your work is seen, understood, and promoted.  
> We build a strong brand with you — not around you.

**Your performance becomes true financial leverage.**
""")

# Team section
st.header("👥 Meet the Team")
st.markdown("""
- **Helios Bringuet** – Strategy & Project Management  
- **Thomas Chen** – Marketing & Project Management  
- **Zoé Charrier** – Branding & Content Management
""")

# Footer
st.write("---")
st.markdown("© 2025 Koya. All rights reserved.")
