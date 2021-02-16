# MailPinger v0.8



Will just send emails to an address rapidly using googles SMTP. Google will stop sending emails after around 300. this was built with burn accounts in mind. 
The next versions will have automatic multiple account handling, proxies & multiple targets. (WIP)

(made this to test how a custom smtp server handled high stress traffic)


usage python MailPinger.py

usage python3 MailPinger.py



-----thego0n@MaL7------

Authenticating with Gmail

There are a few steps you need to take before you can send emails through Gmail with SMTP, and it has to do with authentication. If you're using Gmail as the provider, you'll need to tell Google to allow you to connect via SMTP, which is considered a "less secure" method.

You can't really blame Google for setting it up this way since your application (or some other 3rd party app) will need to have your plaint-text password for this to work, which is definitely not ideal. It's not like the OAuth protocol where a revocable token is issued, so they have to find another way to ensure no unauthorized parties access your data.

For many other email providers you won't need to do any of the extra steps I describe here.

First, you'll want to allow less secure apps to access your account. For detailed instructions on how to do this, you should check out this page:

Allowing less secure apps to access your account - https://support.google.com/accounts/answer/6010255

If you have 2-step verification enabled on your account, then you'll need to create an app-specific password for less secure apps like this. In that case, you'll need to follow the instructions here:

Sign in using App Passwords - https://support.google.com/accounts/answer/185833
