from psycopg2 import pool

# Initialize the connection pool (singleton)
db_pool = None

def init_db_pool(minconn=1, maxconn=5, db_config=None):
    """Initialize the connection pool. Call this once at app startup."""
    
    global db_pool
    if db_pool is None:
        db_pool = pool.SimpleConnectionPool(minconn, maxconn, **db_config)
    return db_pool

def get_connection():
    """Get a connection from the pool."""
    if db_pool is None:
        raise Exception("Connection pool is not initialized. Call init_db_pool first.")
    return db_pool.getconn()

def release_connection(conn):
    """Release the connection back to the pool."""
    if db_pool and conn:
        db_pool.putconn(conn)

def close_all_connections():
    """Close all connections (use at shutdown)."""
    if db_pool:
        db_pool.closeall()
