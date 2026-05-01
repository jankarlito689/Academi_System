from app.config.BD import supabase

TABLE = "atletas"

def get_atleta_by_id(atleta_id: int, academia_id: int):
    return supabase.table(TABLE).select("*").eq("id", atleta_id).eq("academia_id", academia_id).single().execute()

def get_atletas_by_academia_id(academia_id: int):
    return supabase.table(TABLE).select("*").eq("academia_id", academia_id).execute()

def get_atletas_by_email(email: str, academia_id: int):
    return supabase.table(TABLE).select("*").eq("email", email).eq("academia_id", academia_id).execute()

def get_atletas_by_estado(academia_id: int, estado: str):
    return supabase.table(TABLE).select("*").eq("academia_id", academia_id).eq("estado", estado).execute()

def search_atletas_by_name(name: str, academia_id: int):
    return supabase.table(TABLE).select("*").ilike("nombre", f"%{name}%").eq("academia_id", academia_id).execute()

def create_atleta(atleta_data: dict):
    return supabase.table(TABLE).insert(atleta_data).execute()

def update_atleta(atleta_id: int, atleta_data: dict):
    return supabase.table(TABLE).update(atleta_data).eq("id", atleta_id).execute()

def delete_atleta(atleta_id: int):
    return supabase.table(TABLE).delete().eq("id", atleta_id).execute()