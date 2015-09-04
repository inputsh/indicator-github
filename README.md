# GitHub Indicator

Simple GitHub notification indicator designed for elementary OS Freya. It should work with Ubuntu 14.04 and its derivatives.

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
