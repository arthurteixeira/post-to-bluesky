# Post to Bluesky

This Python script allows you to post text messages and images to Bluesky.social using your account credentials.

## Installation

1. Create a virtual environment:
   
   ``` shell
   python3 -m venv venv
   
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate.bat  # Windows
   ```
3. Install dependencies:
   
   ``` shell
   pip install -r requirements. txt
   ```

## Configuration
1. Create a ```.env``` file:
  Create a file named ``.env`` in the root of your project directory. It should contain your Bluesky username and password on separate lines:

    ``` shell
    BSKY_USERNAME=your_username
    BSKY_PASSWORD=your_password
    ```
## Usage

1. Run the script:
   
    ``` shell
    python app/bsky.py
    ```

## Example Usage
 ``` python
post_to_bsky(client, "This is my post with an image!", "../images/my_image.jpg", "Beautiful sunset")
```
    
