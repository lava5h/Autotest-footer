from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Запуск браузера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открытие сайта
driver.get("https://only.digital/")

# Поиск футера
footer = driver.find_element(By.TAG_NAME, "footer")

print("Футер найден!")

# Поиск элементов внутри футера
elements = [
    (By.CSS_SELECTOR, 'div button.StartProjectButton_root__jB_Lv'),
    (By.CSS_SELECTOR, 'div div a[href*="behance.net"]'),
    (By.CSS_SELECTOR, 'div div a[href*="t.me"]'),
    (By.CSS_SELECTOR, 'div div a[href*="vk.com"]'),
    (By.CSS_SELECTOR, 'div div a[href*="dprofile.ru"]'),
    (By.CSS_SELECTOR, 'div p.Footer_year__nyNCc'),
    (By.CSS_SELECTOR, 'div p.Footer_text___ATim'),
    (By.CSS_SELECTOR, 'div div.Footer_contacts__s7c9v'),
    (By.CSS_SELECTOR, 'div div.Footer_telegram__Y0DSn'),
    (By.CSS_SELECTOR, 'div div div a[href$=".pdf"]'),
    (By.CSS_SELECTOR, 'div div div a[href*="pitch.com"]'),
    (By.CSS_SELECTOR, 'div div p.Documents_documentsDescription__ARJsa'),
    (By.CSS_SELECTOR, 'div span.line'),
    (By.CSS_SELECTOR, 'div svg.Footer_logo__2QEhf')
]

for by, selector in elements:
    try:
        element = footer.find_element(by, selector)
        print(f"Элемент найден: {selector}")
    except:
        print(f"Элемент не найден: {selector}")
