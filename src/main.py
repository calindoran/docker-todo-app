from fastapi import FastAPI, Depends, Request, Form, status

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from sqlalchemy.orm import Session

from src.database import SessionLocal, engine

import src.models
src.models.Base.metadata.create_all(bind=engine)

import src.templates
src.templates = Jinja2Templates(directory="./src/templates")

app = FastAPI()

# import redis

# r = redis.Redis(host="redis", port=6379)

# import debugpy
# debugpy.listen(("0.0.0.0", 5678))
# debugpy.wait_for_client()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    todos = db.query(src.models.Todo).all()
    return src.templates.TemplateResponse("base.html", {"request": request, "todo_list": todos})


@app.post("/add")
async def add(request: Request, title: str = Form(...), db: Session = Depends(get_db)):
    new_todo = src.models.Todo(title=title)
    db.add(new_todo)
    db.commit()

    url = request.url_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@app.get("/update/{todo_id}")
async def update(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(src.models.Todo).filter(src.models.Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.commit()

    url = request.url_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)


@app.get("/delete/{todo_id}")
async def delete(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(src.models.Todo).filter(src.models.Todo.id == todo_id).first()
    db.delete(todo)
    db.commit()

    url = request.url_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)

