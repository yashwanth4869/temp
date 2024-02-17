
from fastapi import FastAPI, Depends, status, Response, HTTPException
import models, database, schemas
from sqlalchemy.orm import Session
import uvicorn
from database import SessionLocal
# from django.conf import settings

app = FastAPI()

models.Base.metadata.create_all(database.engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog')
def add_blog(request : schemas.Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(blog_title = request.blog_title, blog_content = request.blog_content)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog')
def get_all_blogs(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/blog/{id}')
def get_blog(id, response : Response, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = 404
        # return {"detail" : f"blog with the id {id} is not found"}
        raise HTTPException()
    return blog

