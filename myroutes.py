from config import app

@app.get('/home')
def greetnow():
    return " this is home page...hi geetha"

@app.get('/sample')
def fun():
    return "this is sample page"
