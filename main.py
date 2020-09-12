import uvicorn

if __name__ == "__main__":
    uvicorn.run('server:server', host="localhost", port=8000, reload=True)