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

def goto_github(widget, callback_data=None):
    url = "https://github.com/notifications"
    webbrowser.open(url, new=0, autoraise=True)

def setup_github(widget, callback_data=None):
    url = "https://github.com/aleksandar-todorovic/indicator-github#setup"
    webbrowser.open(url, new=0, autoraise=True)

### Menu items ###
def add_separator(menu):
    separator = Gtk.SeparatorMenuItem()
    separator.show()
    menu.append(separator)

def add_setup_link(menu):
    link = Gtk.MenuItem(label = "Setup GitHub")
    link.connect("activate", setup_github, None)
    menu.append(link)
    link.show()

def add_github_link(menu):
    link = Gtk.MenuItem(label = "View on GitHub")
    link.connect("activate", goto_github, None)
    menu.append(link)
    link.show()

def item_about(menu):
    dialog = Gtk.AboutDialog.new()
    dialog.set_program_name("GitHub Indicator")
    dialog.set_version("v0.15 Alpha")
    dialog.set_comments("GitHub Indicator designed with elementary OS in mind.")
    dialog.set_authors(["r3bl"])
    dialog.set_website("https://r3bl.me")
    dialog.set_website_label("Website")
    with open("LICENSE.txt","r") as f:
        dialog.set_license(f.read())
    dialog.show_all()
    dialog.run()
    dialog.destroy()

def item_quit(menu):
    exit_item = Gtk.MenuItem("Quit")
    exit_item.connect("activate", Gtk.main_quit)
    menu.append(exit_item)
    exit_item.show()

### Checks notification ###
def notify():
    with open(os.path.abspath(".") + "/token", "r") as f:
        token = f.read()
        token = token[:40]
        global temp

        if len(token) != 40:
            indicator.set_icon("github-new")
            temp = "Token Error"
        else:
            msg = requests.get("https://api.github.com/notifications?access_token=" + token)
            print msg.text
            if msg.text == "[]":
                indicator.set_icon("github")
            elif msg.text == '{"message":"Bad credentials","documentation_url":"https://developer.github.com/v3"}':
                temp = "Token Error"
            else:
                indicator.set_icon("github-new")
        return True

if __name__ == "__main__":

    ### Sets indicator ###
    indicator = AppIndicator3.Indicator.new("GitHub Notifier", "github", 0)
    indicator.set_icon_theme_path(os.path.abspath("."))
    indicator.set_icon("github")
    indicator.set_status(1)

    notify()
    GObject.timeout_add(30*1000, notify) ## Checks for notifications every 30 seconds
    print indicator.get_label()

    if temp == "Token Error":
        menu = Gtk.Menu()
        add_setup_link(menu)
        menu.append(Gtk.SeparatorMenuItem.new())
        item_quit(menu)
        menu.show_all()
    else:
        menu = Gtk.Menu()
        add_github_link(menu)
        menu.append(Gtk.SeparatorMenuItem.new())
        menu_item = Gtk.MenuItem.new_with_label("About...")
        menu_item.connect("activate", item_about)
        menu.append(menu_item)
        menu.append(Gtk.SeparatorMenuItem.new())
        item_quit(menu)
        menu.show_all()

    indicator.set_menu(menu)
    Gtk.main()
