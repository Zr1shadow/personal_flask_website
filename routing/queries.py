from routing import db 
from routing.models import Manga, MangaChapters
from sqlalchemy import text


class MangaQueries():
    
    def getAllMangaTitles(self): 
        titles = []

        for x in db.session.query(Manga):
            titles.append(x.title)
            print(x.title)
        return titles

    def getMangaContent(self, manga_title):
        content = {}
        chapter_link = []
        chapters = []
        title = db.session.query(Manga).filter_by(title = manga_title).first()
        # print(title.id)
        for x in db.session.query(MangaChapters).filter(title.id == MangaChapters.category_id).all():
            my_tuple = (x.chapter, x.chapter_link)
            chapters.append(my_tuple)
            # chapter_link.append(x.chapter_link)
            # print(x.chapter, x.chapter_link)
        # content['chapter'] = chapter
        # content['chapter_link'] = chapter_link
        
        print(chapters)
        return chapters
        # print(db.session.query(MangaChapters).get(title.id))


    def dailyUpdate(self):
        resutld = db.session.execute('SELECT category_id FROM manga_chapters ')
        print(resutld)
# for x, y in db.session.query(Manga, MangaChapters).filter(Manga.id == MangaChapters.category_id).all():
#             manga_chapters.append(y.chapter)
#             manga_link.append(y.chapter_link)
            
#             print(x.id, x.title, y.chapter)

