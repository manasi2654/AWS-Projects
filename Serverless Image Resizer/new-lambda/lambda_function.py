import boto3
from PIL import Image
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print("Processing:", key)

    # جلوگیری infinite loop
    if key.startswith("resized-"):
        print("Skipping resized file")
        return

    # Download image
    response = s3.get_object(Bucket=bucket, Key=key)
    image_content = response['Body'].read()

    # Resize
    image = Image.open(io.BytesIO(image_content))
    image = image.resize((200, 200))

    # Save
    buffer = io.BytesIO()
    image.save(buffer, format='JPEG')
    buffer.seek(0)

    output_key = f"resized-{key}"

    # Upload to SAME bucket
    s3.put_object(
        Bucket=bucket,
        Key=output_key,
        Body=buffer,
        ContentType='image/jpeg'
    )

    print("Saved:", output_key)