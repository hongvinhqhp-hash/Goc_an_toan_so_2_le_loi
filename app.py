import streamlit as st
import pandas as pd
from datetime import datetime
import os

# --- CẤU HÌNH TRANG WEB ---
st.set_page_config(page_title="Góc An Toàn Học Đường", page_icon="🛡️", layout="centered")

# --- CÁC HÀM XỬ LÝ DỮ LIỆU ---
FILE_DATA = "baocao_sos.csv"

def luu_bao_cao(loai_van_de, noi_dung):
    """Hàm lưu báo cáo ẩn danh vào file CSV"""
    thoi_gian = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    du_lieu_moi = pd.DataFrame([{
        "Thời gian": thoi_gian, 
        "Loại vấn đề": loai_van_de, 
        "Nội dung": noi_dung,
        "Trạng thái": "Chưa xử lý"
    }])
    
    if not os.path.exists(FILE_DATA):
        du_lieu_moi.to_csv(FILE_DATA, index=False)
    else:
        du_lieu_moi.to_csv(FILE_DATA, mode='a', header=False, index=False)

def doc_bao_cao():
    """Hàm đọc dữ liệu báo cáo để giáo viên quản lý"""
    if os.path.exists(FILE_DATA):
        return pd.read_csv(FILE_DATA)
    return pd.DataFrame(columns=["Thời gian", "Loại vấn đề", "Nội dung", "Trạng thái"])

# --- XÂY DỰNG GIAO DIỆN CHÍNH ---
st.title("🛡️ GÓC AN TOÀN HỌC ĐƯỜNG")
st.markdown("### Xây dựng tình bạn đẹp - Nói không với bạo lực")

# Tạo Menu thanh bên (Sidebar)
menu = st.sidebar.selectbox(
    "CHỌN CHỨC NĂNG",
    ["📖 Cẩm nang Kỹ năng", "🚨 Gửi Báo cáo SOS", "🤝 Mạng lưới Hỗ trợ", "👨‍🏫 Kênh Quản lý (Dành cho GV)"]
)

# --- MODULE 1: CẨM NANG KỸ NĂNG ---
if menu == "📖 Cẩm nang Kỹ năng":
    st.header("Cẩm nang An toàn & Phòng chống bạo lực")
    
    st.subheader("1. Nhận diện bạo lực học đường")
    st.write("- **Thể chất:** Đánh đập, xô xát, đe dọa bằng vũ lực.")
    st.write("- **Tinh thần:** Tẩy chay, lan truyền tin đồn thất thiệt, cô lập.")
    st.write("- **Trực tuyến (Cyberbullying):** Bắt nạt qua mạng xã hội, tin nhắn.")
    
    st.subheader("2. Nguyên tắc ứng phó (Quy tắc 3K)")
    st.info("**Không** im lặng chịu đựng.\n\n**Không** tham gia cổ vũ hoặc phát tán hình ảnh.\n\n**Kịp thời** báo cáo cho lực lượng hỗ trợ.")

# --- MODULE 2: GỬI BÁO CÁO ẨN DANH ---
elif menu == "🚨 Gửi Báo cáo SOS":
    st.header("Hộp thư Báo cáo Ẩn danh")
    st.markdown("*Mọi thông tin của bạn được bảo mật tuyệt đối. Hãy chia sẻ nếu bạn hoặc bạn bè đang gặp rắc rối.*")
    
    with st.form("form_sos", clear_on_submit=True):
        loai_van_de = st.selectbox(
            "Phân loại rủi ro:",
            ["Bạo lực học đường", "Tai nạn thương tích", "Áp lực tâm lý", "Vấn đề an ninh quanh trường"]
        )
        noi_dung = st.text_area("Mô tả chi tiết sự việc (địa điểm, thời gian, người liên quan...):")
        
        btn_gui = st.form_submit_button("Gửi Báo Cáo Khẩn Cấp")
        
        if btn_gui:
            if noi_dung.strip() == "":
                st.warning("Vui lòng nhập nội dung mô tả sự việc!")
            else:
                luu_bao_cao(loai_van_de, noi_dung)
                st.success("✅ Báo cáo của bạn đã được ghi nhận và gửi đến Ban quản lý. Hãy yên tâm nhé!")

# --- MODULE 3: MẠNG LƯỚI HỖ TRỢ ---
elif menu == "🤝 Mạng lưới Hỗ trợ":
    st.header("Mạng lưới Lực lượng Hỗ trợ Học sinh")
    st.write("Hệ sinh thái an toàn học đường bao gồm sự phối hợp chặt chẽ của các lực lượng sau:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.error("🏫 Từ phía Nhà trường")
        st.write("▪ **Giáo viên chủ nhiệm:** Thầy/Cô trực tiếp hướng dẫn.")
        st.write("▪ **Tổ Tư vấn tâm lý:** Hỗ trợ tháo gỡ khó khăn tinh thần.")
        st.write("▪ **Ban Giám thị / Đoàn Thanh niên:** Xử lý kỷ luật, nề nếp.")
    with col2:
        st.success("🏡 Gia đình & Cộng đồng")
        st.write("▪ **Cha mẹ học sinh:** Lực lượng đồng hành, phối hợp giáo dục cốt lõi.")
        st.write("▪ **Người dân ở cộng đồng:** Hỗ trợ đảm bảo an ninh trật tự quanh khu vực trường học.")
        st.write("▪ **Công an khu vực:** Xử lý các tình huống vi phạm pháp luật.")

# --- MODULE 4: KÊNH QUẢN LÝ (GÓC GIÁO VIÊN) ---
elif menu == "👨‍🏫 Kênh Quản lý (Dành cho GV)":
    st.header("Hệ thống Theo dõi & Quản lý Rủi ro")
    st.write("Tài khoản quản lý nội bộ dành cho GVCN (Chi đoàn 10A6)")
    
    mat_khau = st.text_input("Nhập mã truy cập:", type="password")
    
    # Mật khẩu mặc định là: gvcn123
    if mat_khau == "gvcn123":
        du_lieu = doc_bao_cao()
        if not du_lieu.empty:
            st.dataframe(du_lieu, use_container_width=True)
            st.download_button(
                label="📥 Tải dữ liệu báo cáo (CSV)",
                data=du_lieu.to_csv(index=False).encode('utf-8'),
                file_name='DuLieu_GocAnToan.csv',
                mime='text/csv',
            )
        else:
            st.info("Hiện tại chưa có báo cáo nào.")
    elif mat_khau:
        st.error("Mã truy cập không chính xác!")
