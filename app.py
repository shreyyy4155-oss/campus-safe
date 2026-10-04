import streamlit as st
import sqlite3
connection=sqlite3.connect("campus.db")
cursor=connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS reports(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        incident TEXT,
        location TEXT,
        description TEXT,
        identity TEXT,
        name TEXT,
        contact TEXT,
        status TEXT
)
       """)
connection.commit()
st.title("🛡️ CAMPUS SAFE")
st.caption("your safety,your voice,your campus")
st.divider()
st.header("how may we help you?:")
if "page" not in st.session_state:
    st.session_state.page="home"
if st.session_state.page=="home":
   if st.button("🗣️ANONYMOUS REPORTING"):
      st.session_state.page="reporting"
      st.rerun()
   if st.button("🚨EMERGENCY HELP"):
      st.session_state.page="emergency"
      st.rerun()
   if st.button("📄saved reports"):
      st.session_state.page="reports"
      st.rerun()
elif st.session_state.page=="reporting":
      st.subheader("🗣️ANONYMOUS REPORTING")
      incident=st.selectbox("📄what incident you want to report?:",
      ["bullying","ragging","harassment","theft","suspicious activity"])
      date=st.text_input("🗓️enter the date")
      time=st.text_input("🕐enter the time")
      location=st.text_input("📍where did the incident happen?")
      description=st.text_area("👇🏻describe what happened briefly")
      identity=st.radio("identity status:",["🔐no,keep me anonymous","👤yes,reveal my identity"])
      if identity=="👤yes,reveal my identity":
        name=st.text_input("enter your name:")
        contact=st.text_input("enter email or contact")
      if st.button("submit report"):
        cursor.execute("""
        INSERT INTO reports
        (incident,location,description,identity,name,contact,status)
        VALUES(?,?,?,?,?,?,?)
        """,(
          incident,
          location,
          description,
          identity,
          name if identity=="👤yes,reveal my identity"else"",
          contact if identity=="👤yes,reveal my identity"else"",
          "pending"
        ))
        connection.commit()
        st.success("creport submitted succesfully")
      if st.button("🔙back"):
        st.session_state.page="home"
        st.rerun()
elif st.session_state.page=="emergency":
      st.subheader("🚨EMERGENCY HELP")
      st.write("what kind of help do you need?")
      if st.button("🆘 Personal Safety"):
        describe=st.text_area("let us know what is bothering you")
      if st.button("🏥 Medical Emergency"):
        describe2=st.text_area("how may we help?")
      if st.button("⚠️ Other"):
        describe3=st.text_area("describe your problem to us so you may receive the help asap")
      location=st.text_input("📍enter your current location inside the campus")
      if st.button("send emergency help immediately"):
        st.success("location sent succesfully,we will shortly send our team members to your place")
      if st.button("🔙back"):
        st.session_state.page="home"
        st.rerun()
elif st.session_state.page=="reports":
      st.subheader("📄Saved Reports")
      username=st.text_input("username")
      password=st.text_input("password",type="password")
      st.button("ENTER")
      if username=="shreyashi" and password=="567891234":
        st.success("login sucessful")
        cursor.execute("SELECT * FROM reports")
        reports = cursor.fetchall()
        for report in reports:
           st.write("report id:",report[0])
           st.write("incident:",report[1])
           st.write("location:",report[2])
           st.write("description:",report[3])
           st.write("identity status:",report[4])
           st.write("name:",report[5])
           st.write("contact:",report[6])
           st.write("status:",report[7])
      if st.button("🔙back"):
        st.session_state.page="home"
        st.rerun()
        

