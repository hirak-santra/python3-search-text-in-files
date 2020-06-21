import os
import re


searchConfig = {
   "rootPath": "C:\\HirakSantra\\Node js",
   "fileExtension": ".txt",
   "search": "Hirak|Santra|I am the don"
}



class HiSearch:


    def __init__(self):
        self.file_store = []
        self.search_store = []
        self.extension = searchConfig.get('fileExtension')
        self.search_word = searchConfig.get('search')
       
       
       
    def is_match_found(self, text):
        word_list = self.search_word.split('|')
        for word in word_list:
            x = re.search(word, text)
            if x is not None:
                return True
        return False
    
    
    
    
    def find(self, path=searchConfig.get('rootPath')):
        for obj in os.listdir(path):
            f_path = os.path.join(path, obj)
            if os.path.isdir(f_path):
                self.find(f_path)
            elif obj.endswith(self.extension):
                self.file_store.append(f_path)
                with open( f_path, "r") as fd:
                    content = fd.read()
                    if self.is_match_found(content):
                        self.search_store.append({
                            "content": content,
                            "path": f_path
                        })
                    
       
    
    def print_match_files(self):
        print(self.search_store)
       
       
       
    def print_all_same_type_files(self):
        print(self.file_store)
       
                
                
if __name__=='__main__':
    searcher = HiSearch()
    searcher.find()
    searcher.print_all_same_type_files();
    searcher.print_match_files();
    
