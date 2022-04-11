import json

from django.urls import reverse

def test_hello_world():
  assert "hello_world" == "hello_world"
  assert "foo" != "bar"
  
def test_ping(client):
  #dado - given
    #client
  
  #cuando - when
  url=reverse("ping")
  response = client.get(url)
  content = json.loads(response.content)
  
  #entonces - then
  assert response.status_code == 200
  assert content["ping"] == "pong!"