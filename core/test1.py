import re
import os

print('hello')
migrationNames = sorted(os.listdir('/Users/lx/projects/emotibot_deploy/init-db/minio/migration'))
lastVersion = int('010403001_tde_parsers_init.py'[:9])
pattern = re.compile("^[0-9]{9}\w*.(py|sh)$")

for migrationName in migrationNames :
    if pattern.match(migrationName) and int(migrationName[:9]) > lastVersion:
        if migrationName.endswith('.py'):
            print('Execute python: migration/' + migrationName)

print("Migration Done")