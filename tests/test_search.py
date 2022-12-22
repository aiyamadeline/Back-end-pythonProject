
def test_search(client):
    response = client.get("/")
    assert b"<button>Search</button>" in response.data


    

