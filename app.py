import streamlit as st
import streamlit.components.v1 as components

# 1. Cấu hình trang Streamlit (Full màn hình, đặt tiêu đề)
st.set_page_config(
    page_title="Quản lý bán hàng",
    layout="wide",
    initial_sidebar_state="collapsed" # Ẩn thanh bên
)

# 2. CSS để ẩn các thành phần mặc định của Streamlit (Menu, Header, Footer)
# Giúp trang web của bạn trông giống website bình thường nhất có thể
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {
                padding-top: 0rem;
                padding-bottom: 0rem;
                padding-left: 0rem;
                padding-right: 0rem;
            }
            iframe {
                width: 100%;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 3. Đọc nội dung file index.html
try:
    with open("index.html", 'r', encoding='utf-8') as f:
        html_code = f.read()

    # 4. Hiển thị HTML
    # height=1200: Chiều cao khung (bạn có thể chỉnh số này lớn hơn nếu cần)
    # scrolling=True: Cho phép cuộn nếu nội dung dài
    components.html(html_code, height=1200, scrolling=True)

except FileNotFoundError:
    st.error("Không tìm thấy file index.html. Vui lòng kiểm tra lại thư mục.")
