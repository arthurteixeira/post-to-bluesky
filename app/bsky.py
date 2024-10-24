import os
from atproto import Client
from dotenv import load_dotenv

load_dotenv()

BSKY_USERNAME = os.getenv('BSKY_USERNAME', None)
BSKY_PASSWORD = os.getenv('BSKY_PASSWORD', None)

if BSKY_USERNAME is None:
    print("The environment variable BSKY_USERNAME is not set.")
if BSKY_PASSWORD is None:
    print("The environment variable BSKY_PASSWORD is not set.")

def config_bsky():
    """Configure and log in to the Bsky client."""
    client = Client(base_url='https://bsky.social/xrpc')
    client.login(BSKY_USERNAME, BSKY_PASSWORD)
    return client

def post_to_bsky(client, text, image_files='', alt=''):
    """Post text and images to Bsky."""
    print(image_files)
    try:
        if image_files:
            images_data = []
            for image_file in image_files:
                with open(image_file, 'rb') as f:
                    images_data.append(f.read())
            print(images_data)
            if len(images_data) == 1:
                client.send_image(text=text, image=images_data[0], image_alt=alt)
            else:
                client.send_image(text=text, image=images_data, image_alt=alt)
        else:
            client.send_post(text)
    except Exception as e:
        print(f"Error sending post: {e}")

def main():
    client = config_bsky()
    post_to_bsky(client, "My post", "../images/teste1.png")

if __name__ == '__main__':
    main()
