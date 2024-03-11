import streamlit as st
import pdfplumber as plumber
import docx2txt

def main():
    menu = ["Dropfiles", "About"]
    
    choice = st.sidebar.selectbox("Menu", menu)
    
    match choice:
        case "Dropfiles":
            st.subheader("Dropfiles")
            # st.radio("Select file type:", ["txt", "docx", "pdf"])
            
            raw_text_file = st.file_uploader('Upload File', type=['txt', 'docx', 'pdf'])
            
            if raw_text_file is not None:
                file_details = {"Filename": raw_text_file.name, "FileType": raw_text_file.type, "FileSize": raw_text_file.size}
                st.write(file_details)
                
                match file_details["FileType"]:
                    case "text/plain":
                        try:
                            raw_text = str(raw_text_file.read(), "utf-8")
                            st.info("Text from file:")
                            st.write(raw_text)
                        except:
                            st.warning("TXT file fetching problem..")
                    case "application/pdf":
                        try:
                            pdf_file = plumber.open(raw_text_file)
                            p0 = pdf_file.pages[0]
                            raw_text = p0.extract_text()
                            st.info("Text from pdf file")
                            st.write(raw_text)
                        except:
                            st.warning("PDF file fetching problem..")
                    case "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                        try:
                            raw_text = docx2txt.process(raw_text_file)
                            st.info("Text from docx file")
                            st.write(raw_text)
                        except:
                            pass
        
        case "About":
            st.subheader("Advanced File Uploading")
            st.markdown(
                f"""
                # File Uploader App made with Streamlit
                
                Copyright @ bakudas\n
                For more information drop me a line\n
                bakudas@vacaro.com     
                """)

if __name__ == '__main__':
    main()