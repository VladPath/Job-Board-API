from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
async def get_name():
	return 'Hello Job Board'

if __name__ == '__main__':
	uvicorn.run(app)


