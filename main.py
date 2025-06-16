from supabase import create_client
from fastapi import FastAPI

app = FastAPI()

supabase_url = "https://rkwhnbhuasicbfgskuih.supabase.co"
supabase_api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJrd2huYmh1YXNpY2JmZ3NrdWloIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk4MjE3NzMsImV4cCI6MjA2NTM5Nzc3M30.lz5JCN07H0phADuK9eQ-czTtnBAEHfdzVj3sZ9LvoHo"

database = create_client(supabase_url, supabase_api_key)

#Read
# result = database.table("app_users").select('*').execute()

@app.post("/login")
def login(username, password):
    #get db record with username
    result = database.table("app_users").select("*").eq('username', username).eq('password', password).execute()
    if len(result.data) > 0:
        return True
    else:
        return False
    

@app.get("/users")
def read_users():
    result = database.table('app_users').select('*').execute()
    return result.data

@app.get('/create')
def create_user(name, age, pass2):
    result = database.table('app_users').insert({
        'name': name,
        'age': age,
        'password': pass2
    }).execute()

    return result.data