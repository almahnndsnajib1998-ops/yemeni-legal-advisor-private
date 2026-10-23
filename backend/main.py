
from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="المستشار القانوني اليمني الذكي",
    description="نظام قانوني خاص لإدارة القضايا والبحث القانوني اليمني",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "name": "المستشار القانوني اليمني الذكي",
        "owner_mode": True,
        "status": "development",
        "message": "الخادم الأساسي قيد التطوير",
        "time": datetime.now(timezone.utc).isoformat()
    }

@app.get("/health")
def health():
    return {"status": "ok"}
