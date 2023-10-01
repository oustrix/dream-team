import uvicorn

if __name__ == '__main__':
    uvicorn.run('market:app', reload=True)