import hug

@hug.get('/')
def hello():
    return {
        "Welcome to SRD API"
    }
