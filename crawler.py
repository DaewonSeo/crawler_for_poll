# coding: utf-8

from bs4 import BeautifulSoup
import requests
import csv


def remove_space(value):
    
    return value.replace('\t', "").replace('\n', "").replace("\r", "")

def crawling_page(file_name, url):
    with open('{}.csv'.format(file_name), 'w') as f:
        csv_writer = csv.writer(f) # csv를 작성하기 위한 쓰기 객체 생성

        req = requests.get(url) # 명시한url로request 요청
        html = req.text # request 결과값 텍스트 형태로 생성

        content = BeautifulSoup(html, 'lxml') # parser를 lxml로 선택하고 html 객체 인자 넘김

        tables = content.select('#content > div.bd_list > table > tbody')

        for row in tables:
            for tr in row.find_all('tr'):
                td = tr.find_all('td')
                register_num = remove_space(td[0].text) # 등록번호
                company_name = remove_space(td[1].text) # 여론조사기관명
                client_name = remove_space(td[2].text) # 조사의뢰기관명
                poll_name = remove_space(td[3].text) # 여론조사명
                created_at = td[4].text # 등록일
                region = remove_space(td[5].text) # 대상지역

                csv_writer.writerow([register_num, company_name, client_name, poll_name, created_at, region])


def main(file_name, url):
    crawling_page(file_name, url)

if __name__ == "__main__":
    file_name = 'poll_list'
    url ='http://www.nesdc.go.kr/portal/bbs/B0000005/list.do?searchCnd=&searchWrd=\
            &gubun=&delCode=0&delcode=0&useAt=&replyAt=&menuNo=200467&sdate=&edate=\
            &pdate=&deptId=&isk=&ise=&viewType=&pollGubuncd=&categories=&searchKey=&searchTime=&searchCode=&searchDecision=&pageIndex=8'
    main(file_name, url)
