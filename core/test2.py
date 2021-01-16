import os
print(int('010403001_tde_parsers_init.py'[:9]))
migrationNames = sorted(os.listdir('/Users/lx/projects/emotibot_deploy/init-db/minio/migration'))
print(migrationNames)