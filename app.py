import streamlit as st

def main():
    menu = ["Dropfiles", "About"]
    
    choice = st.sidebar.selectbox("Menu", menu)
    
    match choice:
        case "Dropfiles":
            st.subheader("Dropfiles")
            st.radio("Select file type:", ["txt", "docx", "pdf"])
            
            raw_text_file = st.file_uploader("Upload File:", type=['txt'])
            if raw_text_file is not None:
                try:
                    raw_text = str(raw_text_file.read(), "utf-8")
                    st.info("Text from file:")
                    st.write(raw_text)
                except:
                    st.warning("TXT file fetching problem..")
        
        case "About":
            st.subheader("Advanced File Uploading")

if __name__ == '__main__':
    main()