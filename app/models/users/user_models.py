from app.config.BD import supabase

TABLE = "users"

def get_all_users():
    return supabase.table(TABLE).select("*").execute()

def get_user_by_id(user_id: int):
    return supabase.table(TABLE).select("*").eq("id", user_id).single().execute()

def create_user(user_data: dict):
    return supabase.table(TABLE).insert(user_data).execute()

def update_user(user_id: int, user_data: dict):
    return supabase.table(TABLE).update(user_data).eq("id", user_id).execute()

def delete_user(user_id: int):
    return supabase.table(TABLE).delete().eq("id", user_id).execute()