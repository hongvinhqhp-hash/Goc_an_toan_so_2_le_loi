import streamlit as st
import pandas as pd
from datetime import datetime
import os

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Góc An Toàn Học Đường", page_icon="🛡️", layout="centered")

# Mã truy cập dùng chung cho toàn bộ giáo viên/nhà trường
MAT_KHAU_CHUNG = "gvleloi2026"

# --- HÀM XỬ LÝ DỮ LIỆU ---
def luu_bao_cao(phan_loai, noi_dung):
    thoi_gian = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Tạo DataFrame từ dữ liệu mới
    df_new = pd.DataFrame({"Thời gian": [thoi_gian], "Phân loại": [phan_loai], "Nội dung": [noi_dung]})
    
    # Ghi nối tiếp vào file CSV
    if not os.path.isfile("baocao_sos.csv"):
        df_new.to_csv("baocao_sos.csv", index=False, encoding='utf-8-sig')
    else:
        df_new.to_csv("baocao_sos.csv", mode='a', header=False, index=False, encoding='utf-8-sig')

# --- GIAO DIỆN MENU BÊN TRÁI ---
with st.sidebar:
    st.title("📌 Menu Chức Năng")
    menu = st.radio("Chọn chức năng:", ["📖 Cẩm nang Kỹ năng", "🚨 Gửi Báo cáo SOS", "🤝 Mạng lưới Hỗ trợ", "👨‍🏫 Kênh Quản lý (Dành cho GV)"])

# --- PHÂN HỆ 1: CẨM NANG ---
if menu == "📖 Cẩm nang Kỹ năng":
    st.title("🛡️ GÓC AN TOÀN HỌC ĐƯỜNG")
    st.subheader("Xây dựng tình bạn đẹp - Nói không với bạo lực")
    st.info("**Quy tắc 3K:** Không im lặng - Không cổ vũ - Kịp thời báo cáo.")
    st.write("Bạo lực học đường không chỉ là những tổn thương về thể chất (đánh nhau, xô xát) mà còn là những tổn thương về tinh thần (tẩy chay, nói xấu, đe dọa trên mạng xã hội). Hãy lên tiếng để bảo vệ chính mình và bạn bè!")

# --- PHÂN HỆ 2: GỬI BÁO CÁO (CHUNG TOÀN TRƯỜNG) ---
elif menu == "🚨 Gửi Báo cáo SOS":
    st.title("🚨 Hộp thư Báo cáo Ẩn danh")
    st.markdown("*Mọi thông tin của bạn được bảo mật tuyệt đối. Không ai biết bạn là ai.*")
    
    phan_loai = st.selectbox("Vấn đề bạn đang gặp phải là gì?", ["Bạo lực học đường", "Áp lực tâm lý", "An ninh quanh trường", "Khác"])
    noi_dung = st.text_area("Mô tả chi tiết sự việc (địa điểm, thời gian, người liên quan...):", height=150)
    
    if st.button("Gửi Báo Cáo Khẩn Cấp", type="primary"):
        if noi_dung.strip() == "":
            st.warning("Vui lòng nhập mô tả sự việc trước khi gửi!")
        else:
            luu_bao_cao(phan_loai, noi_dung)
            st.success("✅ Hệ thống đã ghi nhận báo cáo của bạn. Các thầy cô sẽ xử lý ngay lập tức!")

# --- PHÂN HỆ 3: MẠNG LƯỚI HỖ TRỢ ---
elif menu == "🤝 Mạng lưới Hỗ trợ":
    st.title("🤝 Mạng Lưới Hỗ Trợ Khẩn Cấp")
    st.markdown("Đừng ngần ngại liên hệ khi cần sự giúp đỡ. Chúng tôi luôn ở đây!")
    
    st.subheader("🏫 Lực lượng trong nhà trường")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**👨‍🏫 Ban Giám thị**\n\n📞 SĐT: 0233.xxx.xxxx\n\n📍 Phòng Giám thị (Tầng 1)")
    with col2:
        st.info("**🚩 Đoàn Thanh niên**\n\n📞 SĐT: 09xx.xxx.xxx\n\n📍 Văn phòng Đoàn")
        
    st.subheader("🏘️ Lực lượng Cộng đồng")
    col3, col4 = st.columns(2)
    with col3:
        st.warning("**👮 Công an Phường/Xã**\n\n📞 Hotline: 113")
    with col4:
        st.error("**🆘 Tổng đài Bảo vệ Trẻ em**\n\n📞 Nhấn gọi: 111 (Miễn phí 24/7)")

# --- PHÂN HỆ 4: KÊNH QUẢN LÝ (CHUNG) ---
elif menu == "👨‍🏫 Kênh Quản lý (Dành cho GV)":
    st.title("👨‍🏫 Bảng Điều Khiển Trung Tâm")
    st.markdown("Vui lòng nhập mã truy cập của nhà trường để xem dữ liệu.")
    
    mat_khau_nhap = st.text_input("Mã truy cập:", type="password")
    
    if mat_khau_nhap:
        if mat_khau_nhap == MAT_KHAU_CHUNG:
            st.success("✅ Đăng nhập thành công!")
            
            try:
                # Đọc dữ liệu từ file CSV
                df = pd.read_csv("baocao_sos.csv")
                
                st.subheader("📊 Dữ Liệu Báo Cáo Toàn Trường")
                st.info(f"Hệ thống đang ghi nhận tổng cộng **{len(df)}** báo cáo.")
                
                # Hiển thị bảng dữ liệu trực quan
                st.dataframe(df, use_container_width=True)
                
                # Nút tải dữ liệu về máy để làm minh chứng
                csv = df.to_csv(index=False).encode('utf-8-sig') # Dùng utf-8-sig để Excel không lỗi font
                st.download_button(
                    label="📥 Tải tệp dữ liệu về máy tính (CSV)",
                    data=csv,
                    file_name="BaoCao_ToanTruong.csv",
                    mime='text/csv',
                )
                
            except FileNotFoundError:
                st.warning("Hệ thống hiện chưa ghi nhận bất kỳ báo cáo nào từ học sinh.")
            except Exception as e:
                st.error("Có lỗi xảy ra khi đọc dữ liệu. Vui lòng kiểm tra lại cấu trúc file CSV.")
        else:
            st.error("Mã truy cập không hợp lệ. Vui lòng thử lại!")