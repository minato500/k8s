import os
from fastapi import FastAPI

app = FastAPI(title="Production Python API")

DB_USER = os.getenv("DB_USERNAME", "default_user_local")
DB_PASS = os.getenv("DB_PASSWORD", "default_pass_local")
JWT_SECRET = os.getenv("JWT_SECRET", "default_jwt_local")

@app.get("/")
def health_check():
    return {"status": "healthy", "message": "App is running smoothly."}

@app.get("/api/v1/data")
def get_api_data():
    # Matches the ALB path rule: /api/*
    return {"route": "/api", "data": "Secure API data transmission active."}

@app.get("/admin/status")
def get_admin_status():
    # Matches the ALB path rule: /admin/*
    # Demonstrating that the AWS DB Username secret was successfully mounted
    return {
        "route": "/admin", 
        "db_connection_user": DB_USER, 
        "status": "Admin panel active"
    }

@app.get("/dashboard/metrics")
def get_dashboard_metrics():
    # Matches the ALB path rule: /dashboard/*
    return {"route": "/dashboard", "metrics": "System metrics operational."}
