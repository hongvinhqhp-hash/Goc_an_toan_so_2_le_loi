import streamlit as st
import pandas as pd
from datetime import datetime
import os

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="Góc An Toàn - THPT số 2 Lê Lợi", page_icon="🛡️", layout="centered")

# --- 2. TRANG TRÍ GIAO DIỆN BẰNG CSS (CHỮ CỰC LỚN Ở MỌI THÀNH PHẦN) ---
st.markdown("""
<style>
    /* Nền ứng dụng màu xanh nhạt dịu mắt */
    .stApp { background-color: #F0F8FF; }
    
    /* KHU VỰC NỘI DUNG CHÍNH (MAIN) */
    /* Tiêu đề chính (H1) - Phóng to 68px, siêu đậm */
    .main h1, .block-container h1 {
        font-size: 68px !important; 
        font-weight: 900 !important; 
        color: #1E3A8A !important; 
        text-transform: uppercase;
        text-align: center;
        text-shadow: 3px 3px 5px #cccccc;
        line-height: 1.3 !important;
        margin-bottom: 35px !important;
    }
    
    /* Tiêu đề phụ (H2, H3) - Phóng to lên 44px, siêu đậm */
    .main h2, .main h3 { 
        font-size: 44px !important; 
        font-weight: 900 !important; 
        color: #0056b3 !important; 
        margin-top: 30px !important;
        line-height: 1.4 !important;
    }
    
    /* TOÀN BỘ CHỮ VĂN BẢN NỘI DUNG (p, li, span, label) - Tăng vọt lên 30px, siêu đậm, đen tuyền */
    .main p, .main li, .main span, .main label, div.stMarkdown {
        font-size: 30px !important; 
        font-weight: 900 !important; 
        color: #000000 !important; 
        line-height: 1.7 !important; 
    }

    /* KHU VỰC THANH MENU BÊN TRÁI (SIDEBAR) */
    /* Tiêu đề "Danh Mục Chính" */
    [data-testid="stSidebar"] h1 {
        font-size: 32px !important; 
        font-weight: 900 !important;
        text-align: left;
        text-shadow: none !important;
        color: #1E3A8A !important;
    }
    
    /* Chữ trong menu - Phóng to 24px, siêu đậm */
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label {
        font-size: 24px !important; 
        font-weight: 900 !important;
        color: #000000 !important;
    }

    /* NÚT BẤM (BUTTON) - SIÊU KHỔNG LỒ, ĐỎ NỔI BẬT VÀ DÀY DẶN */
    .stButton>button {
        background-color: #FF4B4B; 
        color: white !important;
        font-weight: 900 !important; 
        font-size: 32px !important; /* Chữ trong nút tăng lên 32px */
        border-radius: 15px; 
        border: none;
        padding: 25px 40px; /* Nút dày dặn hơn */
        box-shadow: 0px 6px 10px rgba(0,0,0,0.2);
        transition: all 0.3s ease; 
    }
    .stButton>button:hover {
        background-color: #cc0000;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.4);
        transform: scale(1.04); 
    }
    
    /* Hộp thông báo màu sắc (Alerts) */
    .stAlert {
        border-radius: 15px !important;
        border-left: 12px solid !important; /* Viền trái siêu đậm */
    }
</style>
""", unsafe_allow_html=True)

# --- 3. CẤU HÌNH HỆ THỐNG ---
MAT_KHAU_CHUNG = "so2leloi2026"

def luu_bao_cao(phan_loai, noi_dung):
    thoi_gian = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df_new = pd.DataFrame({"Thời gian": [thoi_gian], "Phân loại": [phan_loai], "Nội dung": [noi_dung]})
    
    if not os.path.isfile("baocao_sos.csv"):
        df_new.to_csv("baocao_sos.csv", index=False, encoding='utf-8-sig')
    else:
        df_new.to_csv("baocao_sos.csv", mode='a', header=False, index=False, encoding='utf-8-sig')

# --- 4. ĐIỀU HƯỚNG MENU ---
with st.sidebar:
    st.title("📌 Danh Mục Chính")
    menu = st.radio("Chọn chức năng:", [
        "📖 Cẩm nang Kỹ năng", 
        "🚨 Gửi Báo cáo SOS", 
        "🤝 Mạng lưới Hỗ trợ", 
        "👨‍🏫 Kênh Quản lý (Dành cho GV)"
    ])

# --- PHÂN HỆ 1: CẨM NANG KỸ NĂNG ---
if menu == "📖 Cẩm nang Kỹ năng":
    st.title("🛡️ CẨM NANG AN TOÀN")
    st.subheader("Trường THPT số 2 Lê Lợi - Nói không với bạo lực")
    
    st.success("💡 **Quy tắc ứng phó 3K:** KHÔNG im lặng - KHÔNG cổ vũ - KỊP THỜI báo cáo")

    st.markdown("### 1. Nhận diện các hình thức bạo lực")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.error("**Thể chất**")
        st.write("- Đánh đập, xô xát.\n- Trấn lột đồ dùng.")
    with col2:
        st.warning("**Tinh thần**")
        st.write("- Tẩy chay, cô lập.\n- Lan truyền tin đồn.")
    with col3:
        st.info("**Trên mạng**")
        st.write("- Nhắn tin đe dọa.\n- Bêu rếu hình ảnh.")

    st.markdown("### 2. Quy trình ứng phó an toàn")
    st.write("1. **Giữ bình tĩnh:** Không dùng bạo lực để giải quyết mâu thuẫn.")
    st.write("2. **Tìm sự giúp đỡ:** Rời khỏi hiện trường và báo ngay cho người lớn.")
    st.write("3. **Sử dụng quyền trợ giúp:** Truy cập 'Gửi Báo cáo SOS' hoặc gọi Hotline hỗ trợ.")

# --- PHÂN HỆ 2: GỬI BÁO CÁO SOS ---
elif menu == "🚨 Gửi Báo cáo SOS":
    st.title("🚨 BÁO CÁO ẨN DANH")
    st.markdown("*Thông tin được bảo mật tuyệt đối. Hãy để thầy cô THPT số 2 Lê Lợi đồng hành cùng bạn.*")
    
    phan_loai = st.selectbox("Vấn đề gặp phải:", [
        "Bạo lực học đường (Thể chất/Tinh thần)", 
        "Bạo lực không gian mạng",
        "Áp lực tâm lý/Học tập", 
        "An ninh ngoài cổng trường", 
        "Vấn đề khác"
    ])
    noi_dung = st.text_area("Mô tả sự việc (địa điểm, thời gian, người liên quan...):", height=200)
    
    if st.button("GỬI BÁO CÁO KHẨN CẤP", use_container_width=True):
        if noi_dung.strip() == "":
            st.warning("Bạn vui lòng nhập nội dung mô tả sự việc!")
        else:
            luu_bao_cao(phan_loai, noi_dung)
            st.success("✅ Báo cáo đã được gửi. Thầy cô sẽ tiếp nhận và hỗ trợ bạn ngay lập tức!")

# --- PHÂN HỆ 3: MẠNG LƯỚI HỖ TRỢ ---
elif menu == "🤝 Mạng lưới Hỗ trợ":
    st.title("🤝 MẠNG LƯỚI HỖ TRỢ")
    st.markdown("### Luôn có người sẵn sàng bảo vệ bạn tại THPT số 2 Lê Lợi!")
    
    st.subheader("🏫 Lực lượng trong nhà trường")
    c1, c2 = st.columns(2)
    with c1:
        st.info("**👨‍🏫 Ban Giám thị**\n\n- Hotline: 0233.xxx.xxxx\n- Phòng trực Tầng 1")
    with c2:
        st.info("**🚩 Đoàn Thanh niên**\n\n- Bí thư Đoàn: 09xx.xxx.xxx\n- Văn phòng Đoàn")
        
    st.subheader("👨‍👩‍👧‍👦 Lực lượng Gia đình")
    st.success("**🏆 Ban đại diện Cha mẹ học sinh Trường THPT số 2 Lê Lợi**\n\n"
               "- Trưởng ban: Bác [Điền Tên] - SĐT: 09xx.xxx.xxx\n\n"
               "- Sẵn sàng phối hợp cùng nhà trường xử lý khẩn cấp các vụ việc.")

    st.subheader("🏘️ Lực lượng Cộng đồng")
    c3, c4 = st.columns(2)
    with c3:
        st.warning("**👮 Công an xã Nam Gianh**\n\n- Trực ban: [Điền số điện thoại]\n- Khẩn cấp: 113")
    with c4:
        st.error("**🆘 Tổng đài Quốc gia 111**\n\n- Hotline: 111\n- Miễn phí 24/7")

# --- PHÂN HỆ 4: KÊNH QUẢN LÝ (DÀNH CHO GV) ---
elif menu == "👨‍🏫 Kênh Quản lý (Dành cho GV)":
    st.title("👨‍🏫 BẢNG QUẢN LÝ")
    st.markdown("Kênh dành riêng cho Ban giám hiệu và Giáo viên nhà trường.")
    
    mat_khau_nhap = st.text_input("Nhập mã truy cập nội bộ:", type="password")
    
    if mat_khau_nhap:
        if mat_khau_nhap == MAT_KHAU_CHUNG:
            st.success("Xác thực thành công!")
            try:
                df = pd.read_csv("baocao_sos.csv")
                st.subheader(f"📊 Thống kê báo cáo (Tổng số: {len(df)})")
                st.dataframe(df, use_container_width=True)
                
                csv = df.to_csv(index=False).encode('utf-8-sig')
                st.download_button(
                    label="📥 TẢI TỆP BÁO CÁO VỀ MÁY (CSV)",
                    data=csv,
                    file_name="BaoCao_AnToan_THPT_So2_LeLoi.csv",
                    mime='text/csv',
                    use_container_width=True
                )
            except FileNotFoundError:
                st.warning("Hệ thống hiện chưa có báo cáo nào.")
        else:
            st.error("Mã truy cập không chính xác!")