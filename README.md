# To run this project
1. Install Python 3.7 to run this project bug free
2. Install "requests" and "beautiful soup" libraries using command:
``` console
pip install requests bs4
```
3. Update ```./PriceTracker/configs.py``` file, where replace ```YOUR_EMAIL_HERE``` with your gmail email with permissions enabled to send mail from external apps. Replace ```YOUR_APP_PASSWORD_HERE``` with your app password which you received from Google after enabling the mail service.
4. Open your terminal and type the command:
``` console
python3 main.py
```
This will open the app and you can select various options available there and configure are per your needs. 

5. This app runs in backgroud to fetch data from your given data and check if price fell down or not, so ```main_backgroud.py``` needs to be executed in backgroud for the app to run. To do that, you need to add ```python3 main_background.py``` command in the startup script of your OS.
