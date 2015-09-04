#!/usr/bin/env python3
# -*-utf8-*-

import os
from gi.repository import AppIndicator3
from gi.repository import Gtk, GObject
import requests
import webbrowser
import sys
import signal

temp = ""
out = ""
no = 0
menu = Gtk.Menu()

def goto_github(widget, callback_data=None):
    url = "https://github.com/notifications"
    webbrowser.open(url, new=0, autoraise=True)

def setup_github(widget, callback_data=None):
    url = "https://github.com/aleksandar-todorovic/indicator-github#setup"
    webbrowser.open(url, new=0, autoraise=True)

### Menu items ###
def item_setup(menu):
    link = Gtk.MenuItem(label = "Setup GitHub")
    link.connect("activate", setup_github, None)
    menu.append(link)
    link.show()

def item_github(menu):
    link = Gtk.MenuItem(label = "View on GitHub")
    link.connect("activate", goto_github, None)
    menu.append(link)
    link.show()

def item_quit(menu):
    exit_item = Gtk.MenuItem("Quit")
    exit_item.connect("activate", Gtk.main_quit)
    menu.append(exit_item)
    exit_item.show()

def no_of_notifications(menu, no):
    temp2 = no
    print "no in no_of_notifications = " + str(no)
    if temp2 == 1:
        notifications_item = Gtk.MenuItem(str(no) + " new notification")
        notifications_item.connect("activate", goto_github, None)
        menu.append(notifications_item)
        notifications_item.show()
    else:
        notifications_item = Gtk.MenuItem(str(no) + " new notifications")
        notifications_item.connect("activate", goto_github, None)
        menu.append(notifications_item)
        notifications_item.show()

def items_notifications(menu):
    print "Todo"

### Checks notification ###
def notify():
    with open(os.path.abspath(".") + "/token", "r") as f:
        token = f.read()
        token = token[:40]
        global temp
        global out

        if len(token) != 40:
            indicator.set_icon("github-new")
            temp = "Token Error"
        else:
            msg = requests.get("https://api.github.com/notifications?access_token=" + token)
            out = msg.text
            global no
            print out
            if msg.text == "[]":
                indicator.set_icon("github")
            elif msg.text == '{"message":"Bad credentials","documentation_url":"https://developer.github.com/v3"}':
                temp = "Token Error"
            else:
                indicator.set_icon("github-new")
                temp = "New Notifications"
                no = out.count ('{"title":')
                print no
        return True

if __name__ == "__main__":

    ### Sets indicator ###
    indicator = AppIndicator3.Indicator.new("GitHub Notifier", "github", 0)
    indicator.set_icon_theme_path(os.path.abspath("."))
    indicator.set_icon("github")
    indicator.set_status(1)

    notify()
    print "Valuable: " + str(no)
    GObject.timeout_add(30*1000, notify) ## Checks for notifications every 30 seconds
    print indicator.get_label()

    if temp == "Token Error":
        item_setup(menu)
        menu.append(Gtk.SeparatorMenuItem.new())
        item_quit(menu)
        menu.show_all()
    elif temp == "New Notifications":
        no_of_notifications(menu, no)
        menu.append(Gtk.SeparatorMenuItem.new())
        item_quit(menu)
        menu.show_all()
    else:
        print "This condition is useless and should be removed from the code"
        item_github(menu)
        menu.append(Gtk.SeparatorMenuItem.new())
        item_quit(menu)
        menu.show_all()

    indicator.set_menu(menu)
    Gtk.main()
