from supabase import create_client,Client
import os 
from dotenv import load_dotenv

# cargar variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception("Faltan variables de entorno de Supabase")

supabase: Client = create_client(supabase_key=SUPABASE_KEY, supabase_url=SUPABASE_URL)