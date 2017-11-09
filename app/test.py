from pypresto import PrestoConnection

host = 'http://labs-puck-prestocoordinator-lv-101.labs.marinsw.net'
user = 'lli'
catalog = 'hive'
port = '8080'
schema = 'func03'

conn = PrestoConnection(host, user, catalog, port, schema)

qury = 'select sitelink_mapping_id,quality_score from sitelink_facts limit 1'

result = conn.run_query(qury)

print result