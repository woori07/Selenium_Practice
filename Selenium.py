
# 크롬 드라이버 기본 모듈
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import time

# 키 입력 모듈 
from selenium.webdriver.common.keys import Keys

# 크롬 드라이버 자동 업데이트를 위한 모듈
from webdriver_manager.chrome import ChromeDriverManager
# 크롬 드라이버 최신 버전 설정 
service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome()
driver.get('http://python.org')
# 이동한 주소의 title 정보를 얻어와 driver.title이 Python이 아니면 예외처리
assert "Python" in driver.title
# name 속성이 q 값을 가진 엘리먼트를 가져옴
elem = driver.find_element(by="name", value="q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.ENTER)
time.sleep(2)
assert "No results found." in driver.page_source
driver.close()