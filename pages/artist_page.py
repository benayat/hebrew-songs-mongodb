
class ArtistsPages:
    base_url = 'https://shironet.mako.co.il/servlet/com.dic.shironet.site.index.servletGetPerformersIndexPrefix?lang' \
               '=1&prefix=letter&sort=alpha&page=page_number'  # class variable shared by all instances

    def __init__(self, letter, size):
        self.urls = set()
        for i in range(size):
            self.urls.add(self.base_url.replace("letter", letter).replace("page_number", str(i)))
