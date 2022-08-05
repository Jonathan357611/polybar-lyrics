# Polybar Lyrics 🎶

This is what it looks like in my Polybar config!

![image](https://user-images.githubusercontent.com/63909127/170585863-2dd2e349-5616-46d1-91a8-df5a7efcd170.png)

Demonstrated using lyrics from Without me - Eminem.

### IMPORTANT

**PLEASE READ**
My program currently uses a free and not-so-good lyrics api (api.textyl.co) which experiences **lots** of downtime, so sadly it isnt uncommon that you wont see any lyrics in your polybar :(

## Installation 💿


1. Clone the Repository:

    ```bash
    git clone https://github.com/Jonathan357611/polybar-lyrics
    cd polybar-lyrics
    ```
2. Get spotify credentials:

    Go to the [Spotify Dashboard](https://developer.spotify.com/dashboard/applications)
    and click on "Create an App" and select a name and description.
    After that, you should see your App's dashboard, click on "Edit Settings"
    and add "http://127.0.0.1/callback" to the redirect URIs. Save that.

3. Set credentials:

    After step 2, paste the Client ID, Client Secret and your spotify username in polybar-lyrics.py, you should get these informations on the App Dashboard.
    Line 10-12 should look something like this:
    ```python
    USERNAME = ""  # Put your Spotify username here
    CLIEND_ID = ""  # Here your Client ID
    CLIENT_SECRET = ""  # And client secret
    ```
    of course filled in with your credentials ;)

4. Polybar Config:
    
    Paste this in your polybar-config.
    
    It's important to set the interval to 0 as there already is a wait in polybar-lyrics.py! 
    ```ini
    [module/polybar-lyrics]
    type = custom/script
    exec = python3 <path to polybar-lyrics.py>
    interval = 0
    ```

5. Initial start:

    **IMPORTANT:**
    You should run the script yourself as an initial setup.
    Execute it like this:
    ```bash
    python3 polybar-lyrics.py
    ```
    It should redirect you to a login screen. Login.
    The script should ask you for the URL your beeing redirect to after the Login. Paste it there and press enter.

    You should have a file called .cache-\<username\> (Use ```ls -a```) . Paste that to your home directory (~)

6. Done

    Everything should now be setup, just add the module to your bar and your ready to go!

    If somethings not working just hit me up and I'll try my best helping you :D

## Advanced options ⚙️

- REDIRECT_URI: Default=http://127.0.0.1/callback Set an own redirect URI (Unnecessary)

- TRUNCATE: Default=90 Amount of letters to show before cutting of

- DELAY: Default=0.8 Delay in seconds.

- LYRICS_API: Default=https://api.textyl.co/api/lyrics?q= Lyrics API to use. If you change this, you maybe need to rewrite the lyrics parsing script due to different API-answers!

- TEMP_FILE: Default=/tmp/.song.json File to temporarly store the songs lyrics.



## Currently working on 🔨

This is in early stage of testing.
Currently the script is pulling song status from Spotify's API directly.
It would probably be better to do this over something like DBUS.
The only problem I encountered using Dbus was that I could not fetch the song progress.

_Theoretically_ I could measure elapsed time with checking if the song has paused. This method could face problems when using multiple devices.

I am thinking about fetching the spotify progress status over the API every few (10?) seconds instead of every. single. one. And check if the song has been paused in between using the dbus approach.
The Pro's would be fewer API calls and a way more synchronised script.


## Support me

If you like my program, please consider donating some ETH!
```0x1f2C6e62622051b3F4d4a3545B17018704630c35```
