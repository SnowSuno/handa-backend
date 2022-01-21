import boto3

from app.core.config import settings

session = boto3.session.Session()
client = session.client(
    's3',
    region_name='sgp1',
    endpoint_url='https://sgp1.digitaloceanspaces.com',
    aws_access_key_id=settings.SPACES_KEY,
    aws_secret_access_key=settings.SPACES_SECRET
)


response = client.list_buckets()
for space in response['Buckets']:
    print(space['Name'])
