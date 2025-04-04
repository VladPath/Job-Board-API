from typing import Annotated
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import uvicorn

from base.database import Base, session_local, engine
from models import models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = session_local()
    if db:
        yield db
    else:
        db.close()

db_depencety = Annotated[Session, Depends(get_db)]


@app.get('/')
async def get_name(db:db_depencety):
	return {'ok':True}


if __name__ == '__main__':
	uvicorn.run('main:app',reload=True)


