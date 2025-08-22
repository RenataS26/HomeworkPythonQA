import requests

token= "QGxajL-FieVKlECClZRYChyIY23fFop8mBTaS3cIn-YSooDd9deoUyiJ26QAxmqD"
base_url="https://yougile.com/api-v2/"
def test_edit_project():
    new_project = {"title": "МозгКипит"}
    headers = {
       "Authorization": f"Bearer {token}",
       "Content-Type": "application/json",
    }
    resp = requests.post(base_url + "projects", json=new_project, headers=headers)
    assert resp.status_code in (200, 201), f"Create project failed: {resp.status_code} {resp.text}"
    response_data = resp.json()
    project_id = response_data["id"]
    assert project_id, "Project id is empty"

    new_project = {"title": "МозгКипит_2"}
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    resp = requests.put(base_url + "projects/" + project_id, json=new_project, headers=headers)
    assert resp.status_code in (200, 201), f"Create project failed: {resp.status_code} {resp.text}"

    #негативный тест не верный id, пустой title
def test_edit_project_negative():
    invalid_project_id = "invalid_id_12345"

    new_project = {"title": ""}  
    headers = {
       "Authorization": f"Bearer {token}",
       "Content-Type": "application/json",
    }
    
    resp = requests.put(base_url + "projects/" + invalid_project_id, json=new_project, headers=headers)
    assert resp.status_code in (400, 404), f"Expected error code, got {resp.status_code}: {resp.text}"
    
    response_data = resp.json()
    assert "error" in response_data or "message" in response_data, "No error message in response"



