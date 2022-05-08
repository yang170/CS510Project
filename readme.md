# How to run the Extension

## Step 1. Load the extension

0. Clone the repository
1. Nevigate to the Chrome extension management page by typing chrome://extensions/ in your browser
2. Enable developer mode (upper right conner)
3. Click "Load unpacked" button
4. Select the project folder
5. That's it 🥳

## Step 2. Run backend server

0. Nevigate the folder where you cloned the repository
1. Install the dependencies
   ```bash
   pip install -r requirement.txt
   ```
2. Go the the backend folder
   ```bash
   cd backend
   ```
3. Run the backend server
   ```
   python api.py
   ```

## Step 3. Use the extension

Select any text on the web page you are browsering, then click the extension icon.
You will see a list of peer reviewed papers related to the text you selected.
