# How to run the Extension

## Step 1. Load the extension

1. Clone the repository
2. Navigate to the Chrome extension management page by typing chrome://extensions/ in your browser
3. Enable developer mode (upper right conner)
4. Click "Load unpacked" button
5. Select the project folder
6. That's it 🥳

## Step 2. Run backend server

1. Navigate the folder where you cloned the repository
2. Install the dependencies
   ```bash
   pip install -r requirement.txt
   ```
3. Go the the backend folder
   ```bash
   cd backend
   ```
4. Obtain an API key from the [Spinger Nature API portal](https://dev.springernature.com/)

5. In the backend folder, create a file and name it as `secret.py`, put your API key inside the file in the following format
   ```python
   API_KEY = 'YOUR_KEY'
   ```
6. Run the backend server
   ```
   python api.py
   ```

## Step 3. Use the extension

Select any text on the web page you are browsering, then click the extension icon.
You will see a list of peer reviewed papers related to the text you selected.
