from main import app

def test_home_route():
    response = app.test_client().get("/")
    print(response)
