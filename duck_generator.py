import boto3
from PIL import Image, ImageDraw, ImageFont
import io
import time

S3_BUCKET_NAME = 'duck-bucket-xcdf2024'

duck_color = 'hotpink'

def generate_image():
    """
    Generates an image of a duck.

    Parameters:
    - x1 (str): Description of parameter

    Returns:
    PIL.Image.Image: An image object of the generated duck.
    """
    # Create an image with light blue background
    img = Image.new('RGB', (200, 200), color='lightblue')
    draw = ImageDraw.Draw(img)

    # Draw the body
    draw.ellipse((50, 70, 150, 170), fill=duck_color, outline='black')

    # Draw the head
    draw.ellipse((70, 30, 130, 90), fill=duck_color, outline='black')

    # Draw the beak
    draw.polygon([(100, 60), (140, 70), (140, 80), (100, 80)], fill='orange', outline='black')
    draw.polygon([(100, 70), (140, 80), (140, 90), (100, 90)], fill='orange', outline='black')

    # Draw the eye
    draw.ellipse((90, 50, 110, 70), fill='white', outline='black')
    draw.ellipse((95, 55, 105, 65), fill='black')

    return img


def upload_to_s3(image, bucket_name, key):
    """
    Pushes the specified image to the specified bucket under the given key.

    Parameters:
    - image (PIL.Image.Image): The image to store in the bucket.
    - bucket_name (str): The name of the bucket to store the image into.
    - key (str): The key to store the image under within the bucket (i.e. filename).

    Returns:
    None
    """
    buffer = io.BytesIO()
    image.save(buffer, 'PNG')
    buffer.seek(0)
    s3_client = boto3.client('s3')
    s3_client.put_object(Bucket=bucket_name, Key=key, Body=buffer, ContentType='image/png')


def lambda_handler(event, context):
    """
    Handles the generating and uploading actions when invoked. Used by lambda to execute logic.

    Parameters:
    - event (dict): The event data passed by Lambda.
    - context (object): Data about invocation, function, and execution env provided by Lambda.

    Returns:
    None
    """
    datestamp = time.strftime('%Y%m%d')
    timestamp = time.strftime("%H%M%S")
    image = generate_image()
    s3_key =  f'{datestamp}/{timestamp}.png'
    upload_to_s3(image, S3_BUCKET_NAME, s3_key)
    return {
        'statusCode': 200,
        'body': 'Image uploaded successfully'
    }

# Generate and view the image locally in-memory.
# image = generate_image()
# image.show()