# GitHub Indicator

Simple GitHub notification indicator designed for elementary OS Freya. It should work with Ubuntu 14.04 and its derivatives.

## Why have I chosen to build an indicator

While the space in the notification area _is_ limited, I have concluded that this application needs to be an indicator first (see [future plans](#future-plans)) nonetheless. The whole point of this idea to have an easy way to access your GitHub notification regardless of your choice of the browser. While there are some browser extensions (like [github-notifier-firefox](https://github.com/sindresorhus/github-notifier-firefox) which I'm currently using) that basically do the same thing, I believe that anybody should be able to quickly access them regardless of their browser choice.

## Future plans

After some careful considerations and the [input I got from the elementary Google+ community](https://plus.google.com/u/0/+AleksandarTodorovi%C4%87r3bl/posts/FffNxGYJ3aw), I have decided that after I finish packaging the first version of this indicator, I'll look into re-creating this as a Vala application that will be integrated with the [Online Accounts plug](https://launchpad.net/switchboard-plug-onlineaccounts) that's going to surpass this indicator implementation, which will probably (I can't guarantee that at the moment) still be avalable for distros other than elementary OS.

## Setup

First, you'll need to run:

```bash
$ git clone https://github.com/aleksandar-todorovic/indicator-github
```

Then, you're going to have to generate a GitHub token.

1. To do so, open up your settings.
![01](https://r3bl.me/apps/img/indicator-github/01.png)

2. Navigate to `Personal access tokens`. Once you're in there, click on `Generate new token`.

3. Select a name for your token (it doesn't really matter which name are you going to choose). In the `Select scopes` section, everything should be unchecked except `notifications`
![](https://r3bl.me/apps/img/indicator-github/02.png)

4. Click on `Generate token`.

5. Copy your token and paste it to the `token` file.

Final step:

    $ python indicator-python.py


## License

This program is licensed under GNU's GPL v3. Its full text is in the [LICENSE](/license.txt) file. The basic code logic was copied from [alimox/indicator-github](https://github.com/alim0x/indicator-github).
