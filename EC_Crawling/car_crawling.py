# asdf
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from copy import deepcopy

import pandas as pd
import time
import sys


def crawling(webpage):
    driver = webdriver.Chrome()
    driver.get(webpage)  # "https://tago.kr/model/index.htm"
    # driver.maximize_window()
    time.sleep(2)
    dataset = []

    for i in range(1, 49):
        if i == 9:
            pass
        else:
            element = driver.find_element(
                By.XPATH, f'//*[@id="container"]/div/div/div[2]/div[{i}]/div/a[1]'
            ).send_keys(Keys.ENTER)
            time.sleep(1)
            # element.location_once_scrolled_into_view
            # element.click()

            time.sleep(1)

            url = driver.current_url

            # 모델명
            url = url[22:-4]

            # 차량 한 줄 설명

            try:
                text = driver.find_element(
                    By.XPATH, '//*[@id="container"]/div/div[3]/h4[1]/span'
                ).text
            except:
                text = "값 추출 못함"
            # 1회 충전 주행 가능 거리

            try:
                drive_range = driver.find_element(
                    By.XPATH, '//*[@id="container"]/div/div[3]/div[2]/div[1]/div'
                ).text
            except:
                drive_range = "값 추출 못함"
            # 충전 시간

            try:
                charge_time = driver.find_element(
                    By.XPATH, '//*[@id="container"]/div/div[3]/div[2]/div[2]/div'
                ).text
            except:
                charge_time = "값 추출 못함"
            # 최고 출력

            try:
                power = driver.find_element(
                    By.XPATH, '//*[@id="container"]/div/div[3]/div[2]/div[3]/div'
                ).text
            except:
                power = "값 추출 못함"
            try:
                전장 = driver.find_element(
                    By.XPATH,
                    '//*[@id="container"]/div/div[3]/div[6]/div[1]/table/tbody/tr[1]/td[2]',
                ).text
            except:
                전장 = "값 추출 못함"
            try:
                전폭 = driver.find_element(
                    By.XPATH,
                    '//*[@id="container"]/div/div[3]/div[6]/div[1]/table/tbody/tr[2]/td[2]',
                ).text
            except:
                전폭 = "값 추출 못함"
            try:
                전고 = driver.find_element(
                    By.XPATH,
                    '//*[@id="container"]/div/div[3]/div[6]/div[1]/table/tbody/tr[3]/td[2]',
                ).text
            except:
                전고 = "값 추출 못함"
            try:
                축거 = driver.find_element(
                    By.XPATH,
                    '//*[@id="container"]/div/div[3]/div[6]/div[1]/table/tbody/tr[4]/td[2]',
                ).text
            except:
                축거 = "값 추출 못함"
            dataset.append(
                [url, text, drive_range, charge_time, power, 전장, 전폭, 전고, 축거]
            )

            try:

                driver.get(webpage)

                time.sleep(1)

            except:

                print("에러")
    driver.close()

    return dataset


if __name__ == "__main__":
    dataset = crawling("https://tago.kr/model/index.htm")

    model = []
    text = []
    drive_range = []
    charge_time = []
    power = []
    전장 = []
    전폭 = []
    전고 = []
    축거 = []

    for i in dataset:
        model.append(i[0])
        text.append(i[1])
        drive_range.append(i[2])
        charge_time.append(i[3])
        power.append(i[4])
        전장.append(i[5])
        전폭.append(i[6])
        전고.append(i[7])
        축거.append(i[8])

    data = {
        "model": model,
        "text": text,
        "drive_range": drive_range,
        "charge_time": charge_time,
        "power": power,
        "전장": 전장,
        "전폭": 전폭,
        "전고": 전고,
        "축거": 축거,
    }

    df = pd.DataFrame(data)
    df.to_csv("car.csv", encoding="utf-8-sig", index = False)
