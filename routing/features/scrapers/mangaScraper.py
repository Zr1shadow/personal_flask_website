from bs4 import BeautifulSoup
import requests
import json
from routing.database.manga_schema import Manga, MangaChapters
from routing import db

class Scaper():

    def __init__(self, URL):
        r = requests.get(URL)
        self.soup = BeautifulSoup(r.content, features = 'html.parser')  
         
    def getAllChapterNum(self):
        
        self.title = self.soup.find('h1').text
        
        manga = Manga(title = self.title)

        self.chapters = self.soup.select('.chapter-name')            

        for chapter in self.chapters:
            self.chapter_num_unparsed = chapter.text
            self.chapter_link = chapter['href']
            self.chapter_num = self.parseForInt(self.chapter_num_unparsed)
            MangaChapters(chapter = self.chapter_num, chapter_link = self.chapter_link, manga = manga)
            
            
        db.session.add(manga)
        db.session.commit()

        # first_record = db.session.query(Manga).order_by(Manga.id.desc()).first()
        
        # for x, y in db.session.query(Manga, MangaChapters).filter(Manga.id == MangaChapters.category_id).all():
        #     print(x.id, x.title, y.chapter)
            
        # return manga

    def getMangaTitle(self):
        return self.title
    
    def getLatestChapter(self):
        self.latestChapter = self.soup.find("a", { "class": "chapter-name"}).text
        self.parseForInt(self.latestChapter)
        return self.latestChapter
    
    #split result by space. So "chapter 86.5 Vol 6" is [chapter, 86.5, Vol, 6]
    #find chapter and get its index get index as that should always be the chapter num 
    def parseForInt(self, chapters):
        intial_parser = chapters.split()
        
        result = intial_parser.index('Chapter') + 1
        
        final_parser = list(map(str,intial_parser[result]))
        
        for i in final_parser:
            
            if i.isnumeric():
                continue
            else:
                if i != '.':
                    final_parser.remove(i)
                else:
                    continue
        num = "".join(final_parser)
        print(num)
        return num

    # def compareDB_VS_LatestChapter(self):
    #     update = self.getLatestChapter()
    #     current = 


        
