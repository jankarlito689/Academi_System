from app.config.BD import supabase

TABLE = "academias"

def get_all_academias():
    return supabase.table(TABLE).select("*").execute()

def get_academia_by_id(academia_id: int):
    return supabase.table(TABLE).select("*").eq("id", academia_id).single().execute()

def create_academia(academia_data: dict):
    return supabase.table(TABLE).insert(academia_data).execute()

def update_academia(academia_id: int, academia_data: dict):
    return supabase.table(TABLE).update(academia_data).eq("id", academia_id).execute()

def delete_academia(academia_id: int):
    return supabase.table(TABLE).delete().eq("id", academia_id).execute()