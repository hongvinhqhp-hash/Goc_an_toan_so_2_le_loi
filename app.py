import streamlit as st
import pandas as pd
from datetime import datetime
import os

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Góc An Toàn - THPT số 2 Lê Lợi", page_icon="🛡️", layout="centered")

# --- TRANG TRÍ GIAO DIỆN BẰNG CSS (UI/UX) ---
st.markdown("""
<style>
    /* Nền ứng dụng */
    .stApp { background-color: #F0F8FF; }
    
    /* Tiêu đề chính (H1) - Cực to và đậm */
    h1 {
        font-size: 42px !important; 
        font-weight: 900 !important; 
        color: #1E3A8A !important; 
        text-transform: uppercase;
        text-align: center;
        text-shadow: 2px 2px 4px #cccccc;
    }
    
    /* Tiêu đề phụ (H2, H3) - To và nét căng */
    h2, h3 { 
        font-size: 28px !important; 
        font-weight: 900 !important; 
        color: #0056b3 !important; 
    }
    
    /* TOÀN BỘ CHỮ VĂN BẢN (Đoạn văn, danh sách, nhãn dán) - TO VÀ ĐẬM HƠN */
    p, li, span, label, div.stMarkdown {
        font-size: 20px !important; 
        font-weight: 700 !important; 
        color: #111111 !important; 
        line-height: 1.6 !important; 
    }
    
    /* Nút bấm GỬI BÁO CÁO - Phóng to và nhấn mạnh */
    .stButton>button {
        background-color: #FF4B4B; 
        color: white !important;
        font-weight: 900 !important; 
        font-size: 22px !important; 
        border-radius: 12px; 
        border: none;
        padding: 15px 30px; 
        transition: all 0.3s ease; 
    }
    .stButton>button:hover {
        background-color: #cc0000;
        box-shadow: 0px 6px 15px rgba(0,0,0,0.3);
        transform: scale(1.05); 
    }
    
    /* Hộp thông báo màu sắc */
    .stAlert {
        border-radius: 10px !important;
        border-left: 6px solid !important;
    }
</style>
""", unsafe_allow_html=True)

# Mật khẩu dùng chung cho toàn bộ giáo viên trường THPT số 2 Lê Lợi
MAT_KHAU_CHUNG = "so2leloi2026"

# --- HÀM XỬ LÝ DỮ LIỆU ---
def luu_bao_cao(phan_loai, noi_dung):
    thoi_gian = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df_new = pd.DataFrame({"Thời gian": [thoi_gian], "Phân loại": [phan_loai], "Nội dung": [noi_dung]})
    
    if not os.path.isfile("baocao_sos.csv"):
        df_new.to_csv("baocao_sos.csv", index=False, encoding='utf-8-sig')
    else:
        df_new.to_csv("baocao_sos.csv", mode='a', header=False, index=False, encoding='utf-8-sig')

# --- GIAO DIỆN MENU BÊN TRÁI ---
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
        st.error("**Bạo lực Thể chất**")
        st.write("- Đánh đập, xô xát.\n- Trấn lột, phá hoại đồ dùng cá nhân.")
        
    with col2:
        st.warning("**Bạo lực Tinh thần**")
        st.write("- Tẩy chay, cô lập.\n- Lan truyền tin đồn ác ý.")
        
    with col3:
        st.info("**Bạo lực Không gian mạng**")
        st.write("- Nhắn tin đe dọa.\n- Bêu rếu hình ảnh riêng tư.")

    st.markdown("### 2. Quy trình ứng phó an toàn")
    st.write("1. **Giữ bình tĩnh:** Tuyệt đối không dùng bạo lực để giải quyết bạo lực.")
    st.write("2. **Tìm sự giúp đỡ:** Rời khỏi hiện trường và tìm đến nơi an toàn.")
    st.write("3. **Sử dụng quyền trợ giúp:** Truy cập ngay vào mục 'Gửi Báo cáo SOS' hoặc liên hệ Hotline trong 'Mạng lưới Hỗ trợ'.")

# --- PHÂN HỆ 2: GỬI BÁO CÁO SOS ---
elif menu == "🚨 Gửi Báo cáo SOS":
    st.title("🚨 Báo cáo Ẩn danh")
    st.markdown("*Mọi thông tin gửi đi đều được bảo mật tuyệt đối. Hãy để các thầy cô THPT số 2 Lê Lợi giúp đỡ bạn.*")
    
    phan_loai = st.selectbox("Vấn đề cần báo cáo:", [
        "Bạo lực học đường (Thể chất/Tinh thần)", 
        "Bạo lực không gian mạng",
        "Áp lực tâm lý/Học tập", 
        "An ninh ngoài cổng trường", 
        "Vấn đề khác"
    ])
    noi_dung = st.text_area("Mô tả chi tiết (Địa điểm, thời gian, người liên quan...):", height=150)
    
    if st.button("GỬI BÁO CÁO KHẨN CẤP", use_container_width=True):
        if noi_dung.strip() == "":
            st.warning("Vui lòng nhập mô tả sự việc!")
        else:
            luu_bao_cao(phan_loai, noi_dung)
            st.success("✅ Báo cáo đã được gửi an toàn. Thầy cô sẽ tiếp nhận và hỗ trợ ngay!")

# --- PHÂN HỆ 3: MẠNG LƯỚI HỖ TRỢ ---
elif menu == "🤝 Mạng lưới Hỗ trợ":
    st.title("🤝 MẠNG LƯỚI HỖ TRỢ")
    st.markdown("### Đừng ngần ngại liên hệ khi cần sự giúp đỡ. THPT số 2 Lê Lợi luôn đồng hành cùng bạn!")
    
    # Nhóm 1: Nhà trường
    st.subheader("🏫 Lực lượng trong nhà trường")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**👨‍🏫 Ban Giám thị**\n\n- Hotline: 0233.xxx.xxxx\n- Địa điểm: Phòng trực (Tầng 1)")
    with col2:
        st.info("**🚩 Đoàn Thanh niên**\n\n- Bí thư Đoàn: 09xx.xxx.xxx\n- Địa điểm: Văn phòng Đoàn")
        
    # Nhóm 2: Gia đình
    st.subheader("👨‍👩‍👧‍👦 Lực lượng từ phía Gia đình")
    st.success("**🏆 Ban đại diện Cha mẹ học sinh Trường THPT số 2 Lê Lợi**\n\n"
               "- Trưởng ban: Bác [Điền Tên] - SĐT: 09xx.xxx.xxx\n\n"
               "- Đại diện cho toàn thể phụ huynh, sẵn sàng can thiệp và phối hợp cùng nhà trường trong các vụ việc khẩn cấp.")

    # Nhóm 3: Cộng đồng
    st.subheader("🏘️ Lực lượng hỗ trợ tại Cộng đồng")
    col3, col4 = st.columns(2)
    with col3:
        st.warning("**👮 Công an xã Nam Gianh**\n\n- SĐT trực ban: [Điền số điện thoại]\n- Hotline khẩn cấp: 113")
    with col4:
        st.error("**🆘 Tổng đài Quốc gia 111**\n\n- Hotline: 111 (Miễn phí 24/7)")

# --- PHÂN HỆ 4: KÊNH QUẢN LÝ (DÀNH CHO GV) ---
elif menu == "👨‍🏫 Kênh Quản lý (Dành cho GV)":
    st.title("👨‍🏫 Bảng Quản Lý")
    st.markdown("Dành cho Ban giám hiệu và Giáo viên trường THPT số 2 Lê Lợi.")
    
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
                st.warning("Hiện tại chưa có báo cáo nào được gửi.")
        else:
            st.error("Mã truy cập không chính xác!")