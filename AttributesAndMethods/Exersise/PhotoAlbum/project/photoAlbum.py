class PhotoAlbum:
    PHOTOS_ON_PAGE=4
    def __init__(self, pages):
            self.pages = pages
            self.photos=[[] for i in range(self.pages)]

    @classmethod
    def from_photos_count(cls,photos_count: int):
        album_pages=photos_count//4
        return PhotoAlbum(album_pages)

    def add_photo(self,label:str):
        page_number=1
        for page in self.photos:
            if len(page)<4:
                page.append(label)
                return f"{label} photo added successfully on page {page_number} slot {len(page)}"
            page_number+=1
        else:
            return f"No more free spots"

    def display(self):
        separator="-----------\n"
        output=separator
        for page in self.photos:
            page_representation="[]"*len(page)
            page_representation=page_representation.replace("][","] [")
            output+=page_representation
            output+="\n"
            output+=separator
        return output

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())