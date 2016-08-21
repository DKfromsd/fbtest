# Facebook Messenger Bot
This is a simple python template that uses Flask to build a webhook for Facebook's Messenger Bot API.
Original source : https://blog.hartleybrody.com/fb-messenger-bot/

Added information:
Install ; python, pip, Heroku toolbelt and from your command prompt.

1. mkvirtualenv test-bot (this is not needed.)
2. pip install -r requirements.txt  (this is required before upload to heroku.)
3. heroku : heroku create (heroku app is created in heroku.com before you upload local desktop.)
4. heroku local (In windows, you can see fatal error fctl win32 api. In devian, it is fine.)
5. git push heroku master (Please check if build success in heroku.)
6. heroku open (app must active until step 11.)
(If you used git in upper folder and created origin and remote, you must open one app only. Please remove multiple apps or specify one app if your git config includes many heroku apps.)
7. create page "your page name" from your facebook.com and create app developers.facebook.com.
8. app setting : APP_ID, SECRET ( copy this and paste in the heroku app's setting.)
9. app product messenger settings: token generator - select page and copy PAGE ACCESS TOKEN.
10. before setup the next step, please make sure this.
	a. "https:// <herokuappname>.herokuapp.com"  your URL works.
	b. command does works : heroku config:add PAGE_ACCESS_TOKEN=$your_page_token_here from step9.
	c. command does work : heroku config:set FACEBOOK_APP_ID=your fb id from step 8.
	d. If so, go to heroku app website and change config value.

11. FB web hook  - type verify token with your any string. Type URL callback with your heroku app URL.
12. 10.d , add  step 11's verify token.
13. subscribe page (this works fine.)
14. Start chat bot (enable messenger from your page. Page is ready to chat now.)
15. Other user access to this page and try to chat in messenger button.
<Up coming>
16. using TF learning result into bot.

"#fbtest" 
