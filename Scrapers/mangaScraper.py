from bs4 import BeautifulSoup
import requests
import json
from routing.models import Manga, MangaChapters
from routing import db
class Scaper():

    def __init__(URL):
        pass    
        
        
    
    # def scape(self,URL):

    #     r = requests.get(URL)
    #     soup = BeautifulSoup(r.content, 'html')
    #     self.title = soup.find('h1').text
        
    #     self.chapters = soup.select('.chapter-name')            

           
       
    #     return  self.chapters

    def getTitle(self):
        return self.title  
    def getChapterNum(self,URL):
        
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html')
        
        self.title = soup.find('h1').text
        
        manga = Manga(title = self.title)

        self.chapters = soup.select('.chapter-name')            

        for chapter in self.chapters:
            self.chapter_num = chapter.text
            self.chapter_link = chapter['href']
            MangaChapters(chapter = self.chapter_num, chapter_link = self.chapter_link, manga = manga)
            
            
        db.session.add(manga)
        db.session.commit()
        # return manga
    