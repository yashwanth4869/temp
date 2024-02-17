from pydantic import BaseModel


class Blog(BaseModel):
    blog_title : str
    blog_content : str