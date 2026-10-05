import pytest
from app import app
from database import init_db
import os

@pytest.fixture
def client():
    app.config['TESTING'] = True
    init_db()
    with app.test_client() as client:
        yield client

def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Secure Notes' in rv.data

def test_create_note(client):
    rv = client.post('/add', data=dict(
        title='Test Title',
        content='Test Content'
    ), follow_redirects=True)
    assert rv.status_code == 200
    assert b'Note created successfully.' in rv.data
    assert b'Test Title' in rv.data

def test_create_empty_note(client):
    rv = client.post('/add', data=dict(
        title='',
        content=''
    ), follow_redirects=True)
    assert rv.status_code == 200
    assert b'Title and content are required.' in rv.data
