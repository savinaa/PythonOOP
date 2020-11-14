class Storage:
    def __init__(self):
            self.categories=[]
            self.topics=[]
            self.documents=[]

    def add_category(self,category) :
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self,topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self,document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self,category_id: int, new_name:str):
        for cat in self.categories:
            if cat.id==category_id:
                cat.edit(new_name)
                break

    def edit_topic(self,topic_id: int, new_topic: str, new_storage_folder: str):
        for t in self.topics:
            if t.id==topic_id:
                t.edit(new_topic,new_storage_folder)
                break

    def edit_document(self,document_id: int, new_file_name: str):
        for d in self.documents:
            if d.id==document_id:
                d.edit(new_file_name)
                break

    def delete_category(self,category_id) :
        for cat in self.categories:
            if cat.id==category_id:
                self.categories.remove(cat)
                break

    def delete_topic(self,topic_id):
        for t in self.topics:
            if t.id==topic_id:
                self.topics.remove(t)
                break

    def delete_document(self,document_id) :
        for d in self.documents:
            if d.id==document_id:
                self.documents.remove(d)
                break

    def get_document(self,document_id):
        for d in self.documents:
            if d.id==document_id:
                return d

    def __repr__(self):
        output=""
        for d in self.documents:
            output+=d.__repr__() +"\n"
        return output