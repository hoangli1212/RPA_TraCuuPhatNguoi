import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image, ImageEnhance
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\tesseract\tesseract.exe'

def tra_cuu_phat_nguoi():
    success = False

    while not success:
        driver = webdriver.Chrome()
        driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")

        try:
            xpath_xemay = '//*[@id="formBSX"]/div[2]/div[2]/select/option[2]'
            element_xemay = driver.find_element(By.XPATH, xpath_xemay)
            element_xemay.click()

            element_bien_so = driver.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/div[1]/input')
            txt_bien_so = '74AH00234'
            element_bien_so.send_keys(txt_bien_so)

            i = 0
            max_attempts = 10

            while i < max_attempts:
                captcha_img = driver.find_element(By.ID, 'imgCaptcha')
                captcha_img.screenshot('captcha.png')

                # Xử lý ảnh Captcha
                captcha_image = Image.open('captcha.png')
                captcha_image = captcha_image.convert('L')
                captcha_image = captcha_image.point(lambda x: 0 if x < 140 else 255)
                enhancer = ImageEnhance.Contrast(captcha_image)
                captcha_image = enhancer.enhance(2)

                captcha_code = pytesseract.image_to_string(captcha_image, config='--psm 6').strip()
                print(f"({i + 1}) Mã captcha đọc được:", captcha_code)

                element_captcha = driver.find_element(By.NAME, 'txt_captcha')
                element_captcha.clear()
                element_captcha.send_keys(captcha_code)

                element_btn = driver.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/input[1]')
                element_btn.click()

                time.sleep(5)

                # Kiểm tra lỗi captcha
                try:
                    error_div = driver.find_element(By.CLASS_NAME, 'xe_texterror')
                    error_text = error_div.text.strip()
                    if "Mã xác nhận sai" in error_text:
                        print("Captcha sai. Thử lại...")
                        i += 1
                        continue
                except:
                    pass  # Không có lỗi captcha, tiếp tục

                break  # Captcha đúng, thoát vòng lặp

            if i >= max_attempts:
                print("Đã thử quá 10 lần captcha nhưng không thành công.")
                break

            # Kiểm tra kết quả
            try:
                result_table = driver.find_element(By.ID, 'bodyPrint123')
                print("Kết quả tra cứu:")
                print(result_table.text)
            except:
                print("Không tìm thấy kết quả hoặc lỗi không xác định.")

            success = True

        except Exception as e:
            print("Đã xảy ra lỗi:", type(e).__name__, "-", str(e))

        finally:
            if os.path.exists('captcha.png'):
                os.remove('captcha.png')
            driver.quit()

schedule.every().day.at("06:00").do(tra_cuu_phat_nguoi)
schedule.every().day.at("12:00").do(tra_cuu_phat_nguoi)

while True:
    schedule.run_pending()
    time.sleep(1)
