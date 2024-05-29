# from helpers.db import MySQLDatabase
from helpers.db2 import *
from openpyxl import Workbook

# from helpers.crawling import 수집
from helpers.crawlingsele import User
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from sqlalchemy import create_engine


driver = r"C:\Users\USER\Desktop\workspace01\Project\driver\chromedriver.exe"

if __name__ == "__main__":

    # 크롬 버전 125.0.6422.113(공식 빌드) (64비트)

    # https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.113/win64/chromedriver-win64.zip

    # <------------------!지자체 보조금-------------------->
    subsidy = []
    시도 = []
    전기자동차보조금 = []
    수소자동차보조금 = []

    user = User("n")
    user.페이지이동("https://ev.or.kr/nportal/buySupprt/initBuySubsidySupprtAction.do#")
    time.sleep(1)

    user.객체선택하고클릭('//*[@id="subPage"]/div/div/ul/li[3]')  # 지자체 보조금 선택
    time.sleep(1)

    시도.append(
        user.객체선택하고객체의텍스트추출(
            '//*[@id="subPage"]/div/div/div[3]/div/div/table/thead/tr/th[1]'
        )
    )
    전기자동차보조금.append(
        user.객체선택하고객체의텍스트추출(
            '//*[@id="subPage"]/div/div/div[3]/div/div/table/thead/tr/th[2]'
        )
    )
    수소자동차보조금.append(
        user.객체선택하고객체의텍스트추출(
            '//*[@id="subPage"]/div/div/div[3]/div/div/table/thead/tr/th[3]'
        )
    )

    # //*[@id="subPage"]/div/div/div[3]/div/div/table/tbody/tr[1]/td[1]
    for i in range(0, 17):
        try:
            시도.append(
                user.객체선택하고객체의텍스트추출(
                    f'//*[@id="subPage"]/div/div/div[3]/div/div/table/tbody/tr[{i+1}]/td[1]'
                )
            )
        except Exception as e:
            시도.append("시도 정보 안 들어옴")
    for i in range(0, 17):
        try:
            전기자동차보조금.append(
                user.객체선택하고객체의텍스트추출(
                    f'//*[@id="subPage"]/div/div/div[3]/div/div/table/tbody/tr[{i+1}]/td[2]'
                )
            )
        except Exception as e:
            전기자동차보조금.append("전기자동차보조금 정보 안 들어옴")
    for i in range(0, 17):
        try:
            수소자동차보조금.append(
                user.객체선택하고객체의텍스트추출(
                    f'//*[@id="subPage"]/div/div/div[3]/div/div/table/tbody/tr[{i+1}]/td[3]'
                )
            )
        except Exception as e:
            수소자동차보조금.append("수소자동차보조금 정보 안 들어옴")

    subsidy = [시도, 전기자동차보조금, 수소자동차보조금]

    wb = Workbook()
    ws = wb.active

    for row_index, row_data in enumerate(subsidy):
        for col_index, cell_data in enumerate(row_data):
            ws.cell(
                row=col_index + 1, column=row_index + 1, value=cell_data
            )  # 이중배열이라 세로로 돌려서 저장하는 방법

        wb.save("subsidy.xlsx")

        user.종료()
