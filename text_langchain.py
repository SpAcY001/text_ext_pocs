import boto3
from langchain.document_loaders import AmazonTextractPDFLoader

textract_client=boto3.client('textract',aws_access_key_id='AKIARU3MIISFVHPQBHLV',
    aws_secret_access_key='',
    region_name="eu-west-1")
loader = AmazonTextractPDFLoader("C:\\Users\\SESA737860\\Desktop\\bank_guarantee\\BG1307018880.pdf",region_name="eu-west-1")
pages = loader.load()
page4_content = pages[0].page_content
print(page4_content)
print('Done')
