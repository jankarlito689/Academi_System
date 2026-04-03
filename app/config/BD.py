from supabase import create_client,Client
import os 

SUPABASE_URL = os.getenv("SUPABASE_URL") or "https://ixrurlduqijlrezkxudq.supabase.co"
SUPABASE_KEY = os.getenv("SUPABASE_KEY") or "sb_secret_797i6g7DJHMGaTW39B8P_A_wUEWjTSd"

supabase: Client = create_client(supabase_key=SUPABASE_KEY, supabase_url=SUPABASE_URL)