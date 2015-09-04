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

## To-do list

* [ ] Create a new `github-new` icon.
* [x] Fix `View on GitHub` option.
* [ ] Make a better `About...` window.
* [ ] Make a settings window.
* [ ] Make a setup window (because the current setup process is a pain in the ass).
* [ ] Find a way to display the number of notifications.
* [ ] Make a list of the notifications in the dropdown menu.
* [ ] Reduce the size of the icons
* [ ] Change icons so they respect [GitHub's logo](https://github.com/logos)
