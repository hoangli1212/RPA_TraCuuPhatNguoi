# Tra cứu phương tiện vi phạm giao thông (CSGT)

Ứng dụng Python sử dụng Selenium và OCR để tự động tra cứu thông tin vi phạm phương tiện từ trang web của Cục CSGT:  
🔗 [https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html](https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html)

## 🧰 Yêu cầu hệ thống

- Python 3.7+
- Google Chrome và ChromeDriver tương thích
- Tesseract OCR cài đặt tại: `C:\tesseract\tesseract.exe`

## 📦 Các thư viện cần cài

```bash
pip install -r requirements.txt
```

## 📁 File `requirements.txt`

```text
selenium
pillow
pytesseract
schedule
```

## ⚙️ Hướng dẫn cài đặt Tesseract

1. Tải về từ: https://github.com/tesseract-ocr/tesseract
2. Cài đặt vào thư mục: `C:\tesseract\`
3. Đảm bảo file `tesseract.exe` có đường dẫn: `C:\tesseract\tesseract.exe`
4. Nếu bạn cài ở nơi khác, sửa dòng sau trong code:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\tesseract\tesseract.exe'
   ```

## 🚀 Cách sử dụng

1. Mở file Python:

   ```bash
   python ten_file.py
   ```

2. Ứng dụng sẽ:
   - Mở trình duyệt Chrome
   - Chọn loại phương tiện (xe máy)
   - Nhập biển số
   - Tự động nhận dạng và nhập mã captcha (tối đa 10 lần)
   - Hiển thị kết quả nếu thành công

## ⏰ Lập lịch chạy tự động

Chương trình được thiết lập để tự động tra cứu vào:

- 06:00 sáng hàng ngày
- 12:00 trưa hàng ngày

Thông qua thư viện `schedule`.

## ⚠️ Lưu ý

- Captcha có thể gây sai sót, OCR không đảm bảo chính xác tuyệt đối.
- Website có thể thay đổi cấu trúc HTML, khiến chương trình không còn hoạt động nếu không cập nhật lại XPATH.
- Cần đảm bảo mạng ổn định và không bị tường lửa chặn kết nối SSL.
