import streamlit as st
import pandas as pd
from datetime import datetime
import os

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="Góc An Toàn - THPT số 2 Lê Lợi", page_icon="🛡️", layout="centered")

# --- 2. TRANG TRÍ GIAO DIỆN BẰNG CSS TỰ ĐỘNG CO GIÃN (RESPONSIVE) ---
st.markdown("""
<style>
    /* Nền ứng dụng màu xanh nhạt dịu mắt */
    .stApp { background-color: #F0F8FF; }
    
    /* KHU VỰC NỘI DUNG CHÍNH (MAIN) */
    /* Tiêu đề chính (H1) - Tự động co giãn từ 36px đến 50px tùy màn hình */
    .main h1, .block-container h1 {
        font-size: clamp(36px, 5vw, 50px) !important; 
        font-weight: 900 !important; 
        color: #1E3A8A !important; 
        text-transform: uppercase;
        text-align: center;
        text-shadow: 2px 2px 4px #cccccc;
        line-height: 1.3 !important;
        margin-bottom: 25px !important;
        word-wrap: break-word; /* Chống tràn chữ */
    }
    
    /* Tiêu đề phụ (H2, H3) - Tự động co giãn */
    .main h2, .main h3 { 
        font-size: clamp(26px, 4vw, 36px) !important; 
        font-weight: 900 !important; 
        color: #0056b3 !important; 
        margin-top: 25px !important;
        line-height: 1.4 !important;
        word-wrap: break-word;
    }
    
    /* TOÀN BỘ CHỮ VĂN BẢN - To, đậm, sắc nét nhưng an toàn cho khung trang (max 22px) */
    .main p, .main li, .main span, .main label, div.stMarkdown {
        font-size: clamp(18px, 2.5vw, 22px) !important; 
        font-weight: 700 !important; 
        color: #111111 !important; 
        line-height: 1.6 !important; 
    }

    /* KHU VỰC THANH MENU BÊN TRÁI (SIDEBAR) - Kích thước cố định chống vỡ khung */
    [data-testid="stSidebar"] h1 {
        font-size: 26px !important; 
        font-weight: 900 !important;
        text-align: left;
        color: #1E3A8A !important;
    }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label {
        font-size: 18px !important; 
        font-weight: 800 !important;
        color: #000000 !important;
    }

    /* NÚT BẤM (BUTTON) - Vừa vặn, nổi bật, không bị tràn cột */
    .stButton>button {
        background-color: #FF4B4B; 
        color: white !important;
        font-weight: 900 !important; 
        font-size: clamp(20px, 3vw, 26px) !important; 
        border-radius: 12px; 
        border: none;
        padding: 15px 20px; 
        box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
        transition: all 0.3s ease; 
        white-space: normal !important; /* Ép chữ trên nút tự xuống dòng nếu màn hình quá hẹp */
        height: auto !important;
    }
    .stButton>button:hover {
        background-color: #cc0000;
        box-shadow: 0px 6px 15px rgba(0,0,0,0.3);
        transform: scale(1.02); 
    }
    
    /* Hộp thông báo màu sắc (Alerts) */
    .stAlert {
        border-radius: 12px !important;
        border-left: 8px solid !important; 
    }
    
    /* Fix bảng dữ liệu không bị tràn ngang */
    [data-testid="stDataFrame"] {
        max-width: 100% !important;
        overflow-x: auto;
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
        st.info("**🚩 Đoàn Thanh niên**\n\n- Bí thư Đoàn: 09xx.xxx.xxxx\n- Văn phòng Đoàn")
        
    st.subheader("👨‍👩‍👧‍👦 Lực lượng Gia đình")
    st.success("**🏆 Ban đại diện Cha mẹ học sinh Trường THPT số 2 Lê Lợi**\n\n"
               "- Trưởng ban: Bác [Điền Tên] - SĐT: 09xx.xxx.xxxx\n\n"
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
                    label="📥 TẢI TỆP BÁO CÁO VỀ MÁY",
                    data=csv,
                    file_name="BaoCao_AnToan_THPT_So2_LeLoi.csv",
                    mime='text/csv',
                    use_container_width=True
                )
            except FileNotFoundError:
                st.warning("Hệ thống hiện chưa có báo cáo nào.")
        else:
            st.error("Mã truy cập không chính xác!")