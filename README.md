# Polybar Lyrics
## Installation

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

    After step 2, paste the Client ID, Client Secret and your spotify username in polybar-lyrics.py.
    Line 10-12 should look something like this:
    ```python
    USERNAME = "John_Doe"  # Put your Spotify username here
    CLIEND_ID = "3450345073645sdfsdf0763"  # Here your Client ID
    CLIENT_SECRET = "8345897s78734587ds7h87fgh7096"  # And client secret
    ```
    of course filled in with your credentials ;)