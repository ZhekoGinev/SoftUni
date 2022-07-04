class Article:
    def __init__(self, title: str, content: str, author: str) -> None:
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_content: str):
        self.content = new_content

    def change_author(self, new_author: str):
        self.author = new_author

    def rename(self, new_title: str):
        self.title = new_title

    def __repr__(self) -> str:
        return f"{self.title} - {self.content}: {self.author}"
