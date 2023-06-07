class Book:
    def __init__(self,ISBN,Title,Category,Publisher,Year_published):
        self.__ISBN = ISBN
        self.__Title = Title
        self.__Category = Category
        self.__Publisher = Publisher
        self.__Year_published = Year_published
        self.records = [
            {'ISBN':9781449340377,'Title':'Python Cookbook','Category':'Education','Publisher':'Oreilly','Year_published':'2013'},
            {'ISBN':9781118951798,'Title':'Adventures in Python','Category':'Adventure','Publisher':'Wiley','Year_published':'2015'}
        ]
    def set_ISBN(self,ISBN):
        self.__ISBN = ISBN
    def get_ISBN(self):
        return self.__ISBN

    def set_Title(self,Title):
        self.__Title = Title
    def get_Title(self):
        return self.__Title

    def set_Category(self,Category):
        self.__Category = Category
    def get_Category(self):
        return self.__Category

    def set_Publisher(self,Publisher):
        self.__Publisher = Publisher
    def get_Publisher(self):
        return self.__Publisher

    def set_Year_Published(self,Year_Published):
        self.__Year_published = Year_Published
    def get_Year_Published(self):
        return self.__Year_published

    def add_record(self,record):
        self.records.append(record)