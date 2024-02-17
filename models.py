from sqlalchemy import Integer, Column, String, Text
from database import Base

class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key = True, index = True)
    blog_title = Column(String(255), nullable = False)
    blog_content = Column(Text)