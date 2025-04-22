import streamlit as st
import re
import time
import random
import string

st.set_page_config(
    page_title="Password Strength Checker", 
    page_icon="🔒", 
    layout="centered",
    initial_sidebar_state="collapsed"
)


st.markdown("""
<style>
.main {
    text-align: center;
}

div[data-baseweb="input"] {
    width: 80% !important;
    margin: auto;
    transition: all 0.3s ease;
}

.stButton {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}

.stButton button {
    width: 50%;
    background-color: #4CAF50;
    color: white;
    font-size: 18px;
    border: none;
    border-radius: 25px;
    padding: 10px 24px;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.stButton button:hover {
    background-color: #45a049;
    transform: translateY(-2px);
    box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
}

.stButton button:active {
    transform: translateY(0);
}

/* Progress bar animation */
.stProgress > div > div > div {
    background-color: #4CAF50;
    transition: width 0.5s ease-in-out;
}
</style>
""", unsafe_allow_html=True)





def check_password_strength(password):
    if not password:
        st.warning("Please Enter A Password First!")
        return
    
    score = 0
    feedback = []
    suggestions = []
    
    length = len(password)
    if length >= 12:
        score += 2
        feedback.append("✅ Password Length Is Excellent (12+ Characters)")
    elif length >= 8:
        score += 1
        feedback.append("⚠️ Password Length Is Good But Could Be Longer (8+ Characters)")
        suggestions.append("Consider Making Your Password Longer (12+ Characters Recommended)")
    else:
        feedback.append("❌ Password Is Too Short (Minimum 8 Characters Required)")
        suggestions.append("Increase Password Length To At Least 12 Characters")
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*(),.?\":{}|<>" for c in password)
    
    if has_upper and has_lower:
        score += 1
        feedback.append("✅ Contains Both Uppercase And Lowercase Letters")
    else:
        feedback.append("❌ Should Contain Both Uppercase And Lowercase Letters")
        suggestions.append("Mix Uppercase And Lowercase Letters In Your Password")
    
    if has_number:
        score += 1
        feedback.append("✅ Contains At Least One Number")
    else:
        feedback.append("❌ Should Contain At Least One Number")
        suggestions.append("Add Numbers To Your Password")
    
    if has_special:
        score += 1
        feedback.append("✅ Contains At Least One Special Character")
    else:
        feedback.append("❌ Should Contain At Least One Special Character")
        suggestions.append("Add Special Characters (!@#$%^&*, Etc.) To Your Password")
    
    strength_percentage = min(score * 25, 100)
    
    st.markdown(f'<div class="password-meter"><div class="password-meter-bar" style="width: {strength_percentage}%;"></div></div>', unsafe_allow_html=True)
    
    if strength_percentage >= 75:
        st.success("## ✅ Excellent! Your Password Is Very Strong")
        st.balloons()
    elif strength_percentage >= 50:
        st.warning("## ⚠️ Good, But Could Be Stronger")
    else:
        st.error("## ❌ Weak Password")
    
    with st.expander("🔍 Detailed Analysis", expanded=True):
        for item in feedback:
            st.write(item)
        if suggestions:
            st.markdown("### 💡 Suggestions For Improvement:")
            for suggestion in suggestions:
                st.write(f"- {suggestion}")

def main():
    st.title("🔐 Password Strength Checker")
    st.markdown("Enter Your Password Below To Check Its Security Level And Get Improvement Suggestions")
    
    password = st.text_input(
        "Enter your password:",
        type="password",
        help="A Strong Password Should Be Long, Complex, And Unique"
    )
    
    if st.button("Check Password Strength"):
        with st.spinner("Analyzing Your Password..."):
            time.sleep(0.5)
            check_password_strength(password)
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 14px;">
    Created with Streamlit | 🔒 Keep your accounts secure
    </div>
    """, unsafe_allow_html=True)


st.markdown("<div class='footer'>Created By Abdul Rehman</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
