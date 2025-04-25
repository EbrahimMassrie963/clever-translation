from .session import engine
from .models import Base
from sqlalchemy import inspect

def create_tables():
    inspector = inspect(engine)
    if not inspector.has_table("translation_requests"): 
        print("Creating tables...")
        Base.metadata.create_all(bind=engine)  
        print("✅ Tables created successfully!")
    else:
        print("✅ Tables already exist.")
