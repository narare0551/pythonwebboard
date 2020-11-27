# !-- 빅데이터 처리하는 코드를 여기서 하면 됩니다
# 1. 크롤링
#    1. https://movie.naver.com/movie/point/af/list.nhn
#    2. 제목, 평점, 리뷰 가져오기
# 2. 지도 그리기
# 3. 그래프 그리기
# ----- ----- ----- ----- -----
from collections import Counter
import os

from folium import plugins
from bs4 import BeautifulSoup
import folium
from konlpy.tag._okt import Okt
from matplotlib import font_manager, rc  # 한글 적용에 필요한 것
import pytagcloud
import requests  # 다른 페이지에 넘어갈? 접속할? 때 필요한 것

import matplotlib.pyplot as plt  # 그래프 그릴 때 필요한 것
import numpy as np
import pandas as pd
from pyboard.settings import STATIC_DIR, TEMPLATE_DIR


def movie_crawling(data):
    for i in range(100):
        url="https://movie.naver.com/movie/point/af/list.nhn?&page="
        url=url+str(i+1)
        req=requests.get(url)
        if req.ok :
            html=req.text
            soup=BeautifulSoup(html,"html.parser")
            titles=soup.select(".title a.movie")
            points=soup.select(".title em")
            contents=soup.select(".title")
            n=len(titles)
            for i in range(n):
                title=titles[i].get_text()
                point=points[i].get_text()
                contentarr=contents[i].get_text().replace('신고','').split("\n\n")
                content=contentarr[2].replace("\t","").replace("\n","")
                data.append([title,point,content])
                


#그래프 그리기 
'''
def make_graph(titles,points):
    font_location = "c:/Windows/fonts/batang.ttc"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    
    plt.xlabel('영화제목')
    plt.ylabel('평균평점')
    plt.grid(True)
    #'int(), float() df['필드명'].astype(float32)'    
    plt.bar(range(len(titles)), points, align='center')
    plt.xticks(range(len(titles)), list(titles), rotation='70')
    plt.savefig(os.path.join(STATIC_DIR,'images/fig01.png'), dpi=300)
    
   ''' 
    
def make_graph(titles,points):
    font_location = "c:/Windows/fonts/batang.ttc"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    
    plt.xlabel('영화제목')
    plt.ylabel('평균평점')
    plt.grid(True)
    #'int(), float() df['필드명'].astype(float32)'    
    plt.bar(range(len(titles)), points, align='center')
    plt.xticks(range(len(titles)), list(titles), rotation='70')
    plt.savefig(os.path.join(STATIC_DIR,'images/fig01.png'), dpi=300)
    
    
    
    
    
    
    
def saveWordcloud(contents):
    nlp = Okt()
    wordtext=""
    for t in contents:
        wordtext+=str(t)+" "
        
    nouns = nlp.nouns(wordtext)
    count = Counter(nouns)
    
    wordInfo = dict()
    for tags, counts in count.most_common(100):
        if (len(str(tags)) > 1):
            wordInfo[tags] = counts
    filename=os.path.join(STATIC_DIR,'images/wordcloud01.png')
    taglist = pytagcloud.make_tags(dict(wordInfo).items(), maxsize=80)
    pytagcloud.create_tag_image(taglist, filename, size=(640, 480), fontname='Korean', rectangular=False)
    
    
def cctv_map():
    popup=[]
    data_lat_log=[]
    df=pd.read_csv("e:/data/input/map/cctv.csv",encoding="utf-8")
    for data in df.values:
        if data[4]>0:
            popup.append(data[2])
            data_lat_log.append([data[3],data[4]])
    
    m=folium.Map([35.1803305,129.0516257], zoop_start=11)
    plugins.MarkerCluster(data_lat_log,popups=popup).add_to(m)
    m.save(os.path.join(TEMPLATE_DIR,'map/map01.html'))   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    