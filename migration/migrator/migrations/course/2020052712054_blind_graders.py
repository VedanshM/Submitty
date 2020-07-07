def up(config, database, semester, course):
    
    if not database.table_has_column('electronic_gradeable', 'limited_access_blind'):
        database.execute('ALTER TABLE electronic_gradeable ADD COLUMN eg_limited_access_blind INTEGER DEFAULT 1')
        database.execute('ALTER TABLE electronic_gradeable ADD COLUMN eg_peer_blind INTEGER DEFAULT 3')


def down(config, database, semester, course):
    
    database.execute('ALTER TABLE electronic_gradeable DROP COLUMN eg_limited_access_blind')
    database.execute('ALTER TABLE electronic_gradeable DROP COLUMN eg_peer_blind')
