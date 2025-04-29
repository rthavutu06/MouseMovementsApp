^e::
{
    Run '"C:\Program Files\Google\Chrome\Application\chrome.exe" --app=http://localhost:3000 --window-size=350,150 --window-position=0,880'
    Sleep 1000  ; Wait for Chrome to open
    WinWaitActive "Run Commands - Google Chrome"  ; Wait for the browser window to be active
    WinMove "Run Commands - Google Chrome", "", 0, 880, 350, 150  ; Move and resize the window
}
return
