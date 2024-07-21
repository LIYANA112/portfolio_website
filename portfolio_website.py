import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

col1,col2 = st.columns(2)

with col1:
    st.subheader("Hai :wave:")
    st.title("I am Liyana J")
    st.write("- Passionate")
    st.write("- Proactive fourth-year B.Tech CSE student")
    st.write("- Studying at SCTCE, Trivandrum")

with col2:
    st.image("liy.jpg")

st.title(" ")

persona = """
        You are Liyana AI bot. You help people answer questions about your self (i.e Liyana)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Liyana: 
         
        Liyana J is an fourth year Btech in Computer Science and Engineering(CSE) at Sree Chitra Thirunal College of Engineering(SCTCE),Pappanamcode,Trivandrum.
        liyana also pursuing honors/honours in Machine Learning and Minor Course in Mechatronics,
        coming from Karunagappally,Kollam,completed 12 th standard at Model HSS Kulashekarapuram,Kollam with 99% marks,
        completed 10th standard at HS for Girls,Karunagappally with Full A+ on all subjects.
        Spending time with family and friends is the hobby, about relationship Liyana have commitments so not ready to disclose.
        Liyana has instagram account not public.Btech CGPA is 8.31 and dreams to become an finacially indepedent. liyana's father is Retired Subinspector of Police,
        mother is housewife and a sister is a BDS Graduate working At Sharjah
        
 
        Liyana's Email: liyanajl1102@gmail.com
        Liyana's Linkdin: https://www.linkedin.com/in/liyana-j-95726325a
        Liyana's Github :https://github.com/LIYANA112
        """
st.title("Liyana's AI BOT")
user_question = st.text_input("Ask anything about me")
if st.button("ASK",use_container_width=400):
    prompt = persona + "Here is the question that the user asked: "+ user_question
    response = model.generate_content(prompt)
    st.write(response.text)
    

st.subheader(" ")
st.subheader("My Skills")
st.slider("Programming", 0, 100, 70)
st.slider("Web Development", 0, 100, 80)
st.slider("AI/ML", 0, 100, 75)

st.write("")
st.write("CONTACT")
st.write("Email: liyanajl1102@gmail.com")





#with col2:
    #st.video("https://youtu.be/BFlRmIvqwSA?si=a6qL3krtRgqVIKOZ")