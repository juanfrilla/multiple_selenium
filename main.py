import os
import concurrent.futures
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


urls = [
    "https://www.windguru.cz/586104",  # costa teguise
    "https://www.windguru.cz/49323",  # las cucharas
    "https://www.windguru.cz/49326",  # Jameos del agua
    "https://www.windguru.cz/49325",  # La garita
    "https://www.windguru.cz/207014",  # la garita
    "https://www.windguru.cz/49328",  # famara
    "https://www.windguru.cz/501282",  # janubio
    "https://www.windguru.cz/49319",  # playa dorada
    "https://www.windguru.cz/430882",  # puerto calero
    "https://www.windguru.cz/49320",  # los pocillos
    "https://www.windguru.cz/49321",  # matagorda
    "https://www.windguru.cz/49322",  # playa honda
    "https://www.windguru.cz/49324",  # los charcos
    "https://www.windguru.cz/501281",  # la santa
]

def get_driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor="http://localhost:4444",
        options=options,
    )
    return driver

def get_soup(url, tag_to_wait="table.tabulka", timeout=60 * 1000):
    driver = get_driver()
    driver.get(url)
    if tag_to_wait:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, tag_to_wait))
        )
    html = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html, "html.parser")
    return soup


def parse_spot_name(soup):
    return soup.select("div.spot-name.wg-guide")[0].text.strip()


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        soups = list(executor.map(get_soup, urls))
    for soup in soups:
        print(parse_spot_name(soup))


if __name__ == "__main__":
    main()
