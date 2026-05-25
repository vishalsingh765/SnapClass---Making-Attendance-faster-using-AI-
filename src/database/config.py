from supabase import create_client

SUPABASE_URL = "https://kebzbvmhnakltwkgiyof.supabase.co"

SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtlYnpidm1obmFrbHR3a2dpeW9mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzk1MzQ3NjYsImV4cCI6MjA5NTExMDc2Nn0.7Dsi2nrO73ffc_TAStiWCftdZAyvvzEdQ4tYpsKjBP0"

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)