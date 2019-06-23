'''
https://docs.microsoft.com/en-us/azure/cosmos-db/table-storage-how-to-use-python
'''

from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
import os

account_key = os.environ['AZURE_STORAGE_ACCOUNT_KEY']
table_service = TableService(account_name='lakemichigan',
                             account_key=account_key)

table_service.create_table('tasktable')

point = {'PartitionKey': 'datapoints', 'RowKey': '001', 'description' : '246 lines', 'priority' : 200}
table_service.insert_or_replace_entity('tasktable', point)

"""
insert_entity, insert_or_replace_entity, update_entity, merge_entity
"""

print('ok')