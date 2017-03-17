#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  arfedora-osx.py
#  
#  Copyright 2017 youcefsourani <youcef.m.sourani@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import subprocess
import os
import sys
import time

def init_check():
    if os.getuid()==0:
        sys.exit("Run Script Without Root Permissions.")
        
    if not sys.version.startswith("3"):
        sys.exit("Use Python 3 Try run python3 arfedora-osx.py")
        
    if os.getenv("XDG_CURRENT_DESKTOP")!="GNOME" :
        sys.exit("Your Desktop Is Not gnome shell")
        
init_check()

def get_distro_name():
    with open("/etc/os-release") as myfile:
        for line in myfile.readlines():
            if line.startswith("ID"):
                return line.split("=")[1].strip()

distroname=get_distro_name()
home="/home/"+os.environ["LOGNAME"]
dirname=os.path.abspath(os.path.dirname(__file__))
speed=1
default_terminal_profile=eval(subprocess.check_output("gsettings get org.gnome.Terminal.ProfilesList list",shell=True).decode("utf-8").strip())[0]
default_terminix_profile=eval(subprocess.check_output("gsettings get com.gexperts.Terminix.ProfilesList list",shell=True).decode("utf-8").strip())[0]



terminix=["gsettings set com.gexperts.Terminix.Settings quake-hide-headerbar true",
          "gsettings set com.gexperts.Terminix.Settings quake-height-percent 40",
          "gsettings set com.gexperts.Terminix.Settings quake-width-percent 100",
          "gsettings set com.gexperts.Terminix.Settings theme-variant \'system\'",
          "gsettings set com.gexperts.Terminix.Settings enable-transparency true",
          "gsettings set com.gexperts.Terminix.Settings terminal-title-show-when-single false",
          "dconf write  /com/gexperts/Terminix/profiles/%s/use-system-font false"%default_terminix_profile,
          "dconf write  /com/gexperts/Terminix/profiles/%s/font \"\'Monospace 15\'\""%default_terminix_profile,
          "dconf write  /com/gexperts/Terminix/profiles/%s/background-transparency-percent 19"%default_terminix_profile,
          "dconf write  /com/gexperts/Terminix/profiles/%s/background-color \"\'#FFFFFFFFFFFF\'\""%default_terminix_profile,
          "dconf write  /com/gexperts/Terminix/profiles/%s/use-theme-colors false"%default_terminix_profile,
          "dconf write  /com/gexperts/Terminix/profiles/%s/cursor-colors-set true"%default_terminix_profile,
          "dconf write  /com/gexperts/Terminix/profiles/%s/cursor-background-color \"\'#EFEF29292929\'\""%default_terminix_profile]

extensions_to_enable=["user-theme@gnome-shell-extensions.gcampax.github.com",
                      "activities-config@nls1729",
                      "apps-menu@gnome-shell-extensions.gcampax.github.com",
                      "clipboard-indicator@tudmotu.com",
                      "CoverflowAltTab@palatis.blogspot.com",
                      "dash-to-dock@micxgx.gmail.com",
                      "drive-menu@gnome-shell-extensions.gcampax.github.com",
                      "EasyScreenCast@iacopodeenosee.gmail.com",
                      "gnome-shell-audio-output-switcher@kgaut",
                      "places-menu@gnome-shell-extensions.gcampax.github.com",
                      "TerminixDropdown@ivkuzev@gmail.com",
                      "todo.txt@bart.libert.gmail.com",
                      "background-logo@fedorahosted.org",
                      "Move_Clock@rmy.pobox.com",
                      "remove-dropdown-arrows@mpdeimos.com",
                      "suspend-button@laserb",
                      "TopIcons@phocean.net"]

extensions_to_install_from_internet={"user-theme@gnome-shell-extensions.gcampax.github.com" : "gnome-shell-extension-user-theme",
                                     "apps-menu@gnome-shell-extensions.gcampax.github.com" : "gnome-shell-extension-apps-menu",
                                     "drive-menu@gnome-shell-extensions.gcampax.github.com" : "gnome-shell-extension-drive-menu",
                                     "places-menu@gnome-shell-extensions.gcampax.github.com" : "gnome-shell-extension-places-menu",
                                     "Move_Clock@rmy.pobox.com" : "gnome-shell-extension-move-clock",
                                     "TopIcons@phocean.net" : "gnome-shell-extension-topicons",
                                     "suspend-button@laserb" : "gnome-shell-extension-suspend-button",
                                     "remove-dropdown-arrows@mpdeimos.com" : "gnome-shell-extension-remove-dropdown-arrows",
                                     "background-logo@fedorahosted.org" : "gnome-shell-extension-background-logo"
                                    }



gsettings=["gsettings set org.gnome.desktop.background show-desktop-icons false",
           "gsettings set org.gnome.desktop.background  picture-uri \
           'file://%s/Pictures/565055.jpg' "%home,
           "gsettings set org.gnome.desktop.screensaver picture-uri \
           'file://%s/Pictures/565055.jpg' "%home,
           "gsettings set org.gnome.desktop.interface icon-theme 'la-capitaine-icon-theme-0.2.0' ",
           "gsettings set org.gnome.shell.extensions.user-theme name 'macOS-3-1' ",
           "gsettings set org.gnome.desktop.interface gtk-theme  Gnome-OSX-II-NT-2-5-1",
           "gsettings set org.gnome.desktop.interface enable-animations true",
           "gsettings set org.gnome.desktop.wm.preferences button-layout ':minimize,close' ",
           "gsettings set org.gnome.nautilus.preferences always-use-location-entry false",
           "gsettings set org.gnome.desktop.interface cursor-theme 'capitaine-cursors' ",
           "gsettings set org.gnome.Terminal.Legacy.Settings theme-variant light",
           "gsettings set org.gnome.Terminal.Legacy.Settings default-show-menubar false",
           "gsettings set org.fedorahosted.background-logo-extension logo-file \'/usr/share/pixmaps/fedora_whitelogo.svg\'",
           "gsettings set org.fedorahosted.background-logo-extension logo-position \'bottom-right\'"]
           
           
           
dconf=["dconf write /org/gnome/shell/extensions/activities-config/activities-config-button-removed  false",
       "dconf write /org/gnome/shell/extensions/activities-config/activities-config-button-no-text  false",
       "dconf write /org/gnome/shell/extensions/activities-config/activities-icon-padding  8",
       "dconf write /org/gnome/shell/extensions/activities-config/activities-config-button-no-icon  false",
       "dconf write /org/gnome/shell/extensions/activities-config/activities-config-button-icon-path  \"\'/usr/share/pixmaps/fedora-logo-sprite.png\'\"",
       "dconf write /org/gnome/shell/extensions/activities-config/enable-conflict-detection  true",
       "dconf write /org/gnome/shell/extensions/activities-config/panel-shadow-color-hex-rgb  \"\'#000000\'\"",
       "dconf write /org/gnome/shell/extensions/activities-config/position-right  false",
       "dconf write /org/gnome/shell/extensions/activities-config/original-activities-button-text  \"\'Activities\'\"",
       "dconf write /org/gnome/shell/extensions/activities-config/pointer-barriers-supported  true",
       "dconf write /org/gnome/shell/extensions/activities-config/maximized-window-effect  0",
       "dconf write /org/gnome/shell/extensions/activities-config/panel-hide-app-menu-button-icon  false",
       "dconf write /org/gnome/shell/extensions/activities-config/activities-text-padding  0",
       "dconf write /org/gnome/shell/extensions/activities-config/override-theme  false",
       "dconf write /org/gnome/shell/extensions/activities-config/panel-background-color-hex-rgb  \"\'#000000\'\"",
       "dconf write /org/gnome/shell/extensions/activities-config/panel-hide-rounded-corners  false",
       "dconf write /org/gnome/shell/extensions/activities-config/shell-theme-id  \"\'macOS-3-1<|>\'\"",
       "dconf write /org/gnome/shell/extensions/activities-config/activities-config-button-text  \"\'%s\'\""%distroname.title(),
       "dconf write /org/gnome/shell/extensions/activities-config/show-overview  false",
       "dconf write /org/gnome/shell/extensions/activities-config/first-enable  false",
       "dconf write /org/gnome/shell/extensions/dash-to-dock/apply-custom-theme  false",
       "dconf write /org/gnome/shell/extensions/dash-to-dock/custom-theme-running-dots  false",
       "dconf write /org/gnome/shell/extensions/dash-to-dock/custom-theme-shrink  false",
       "dconf write /org/gnome/shell/extensions/dash-to-dock/click-action  \"\'minimize\'\"",
       "dconf write /org/gnome/shell/extensions/dash-to-dock/dock-position  \"\'BOTTOM\'\"",
       "dconf write /org/gnome/shell/extensions/dash-to-dock/scroll-action  \"\'do-nothing\'\"",
       "dconf write /org/gnome/shell/extensions/dash-to-dock/force-straight-corner  false"]
       

gnome_terminal=["gsettings set  org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:%s/ use-theme-colors false"%default_terminal_profile,
                "gsettings set  org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:%s/ use-system-font false"%default_terminal_profile,
                "gsettings set  org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:%s/ background-color \'rgb(255,255,255)\'"%default_terminal_profile,
                "gsettings set  org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:%s/ font \'Monospace 15\'"%default_terminal_profile,
                "gsettings set  org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:%s/ foreground-color \'rgb(89,64,191)\'"%default_terminal_profile,
                "gsettings set  org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:%s/ cursor-background-color \'rgb(239,41,41)\'"%default_terminal_profile,
                "gsettings set  org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:%s/ cursor-colors-set true"%default_terminal_profile,
                "gsettings set  org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:%s/ background-transparency-percent 20"%default_terminal_profile,
                "gsettings set  org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:%s/ use-transparent-background true"%default_terminal_profile]
       
def get_all_exists_extensions():
    result=[]
    locations=[home+"/.local/share/gnome-shell/extensions",
               "/usr/share/gnome-shell/extensions",
               "/usr/local/share/gnome-shell/extensions"]

    for location in locations:
        if os.path.isdir(location):
            for folder in os.listdir(location):
                if folder not in result:
                    result.append(folder)
    return result
	
all_exists_extensions=get_all_exists_extensions()


def setup_extensions_if_not_exists(extensions):
    to_install_from_internet=[]
    local_extensions_folder=os.listdir(dirname+"/extensions")
    for extension in extensions :
        if extension not in  all_exists_extensions:
            if extension in local_extensions_folder:
                subprocess.call("cp -r %s/extensions/%s %s/.local/share/gnome-shell/extensions"%(dirname,extension,home),shell=True)
            else:
                to_install_from_internet.append(extension)
    return to_install_from_internet


def install_from_internet(to_install):
    install=""
    if len(to_install) != 0:
        for extension in to_install:
            install+=extensions_to_install_from_internet[extension]+" "
        check = subprocess.call("sudo dnf install %s -y --best"%install,shell=True)
        if check !=0:
            sys.exit("\nInstall %s Fail Check Your Connections.\n"%install)


install_from_internet(setup_extensions_if_not_exists(extensions_to_enable))


def setup_themes():
    os.makedirs(home+"/.themes",exist_ok=True)
    for folder in os.listdir(dirname+"/themes"):
        subprocess.call("cp -r %s/themes/%s %s"%(dirname,folder,home+"/.themes"),shell=True)
        
setup_themes()


def setup_icons():
    os.makedirs(home+"/.icons",exist_ok=True)
    for folder in os.listdir(dirname+"/icons"):
        subprocess.call("cp -r %s/icons/%s %s"%(dirname,folder,home+"/.icons"),shell=True)
        
setup_icons()


def setup_backgrounds():
    os.makedirs(home+"/Pictures",exist_ok=True)
    check = subprocess.call("curl -L -o  %s/backgrounds/565055.jpg https://www.dropbox.com/s/1bzhty2kzl05v07/565055.jpg?dl=0"%dirname,shell=True)
    if check != 0:
        sys.exit("\nDownload Background Picture Fail Check Your Connections.\n"%install)
    for pic in os.listdir(dirname+"/backgrounds"):
        subprocess.call("cp  %s/backgrounds/%s %s"%(dirname,pic,home+"/Pictures"),shell=True)
        
setup_backgrounds()


def install_terminix():
    check = subprocess.call("rpm -q terminix",shell=True)
    if check !=0:
        check = subprocess.call("sudo  dnf copr enable heikoada/terminix -y",shell=True)
        if check !=0:
            sys.exit("\nInstall Terminix Fail Check Your Connections.\n")
        check = subprocess.call("sudo  dnf install terminix -y --best",shell=True)
        if check != 0 :
            sys.exit("\nInstall Terminix Fail Check Your Connections.\n")
        
install_terminix()        
       
       
def install_murrine_engine():
    check = subprocess.call("rpm -q gtk-murrine-engine",shell=True)
    if check !=0:
        check = subprocess.call("sudo  dnf install gtk-murrine-engine -y --best",shell=True)
        if check != 0 :
            sys.exit("\nInstall gtk-murrine-engine Fail Check Your Connections.\n")
        
install_murrine_engine()        
  
 
def disable_unimportant_extensions():
    time.sleep(speed)
    for extension in all_exists_extensions:
        if extension not in extensions_to_enable:
            subprocess.call("gnome-shell-extension-tool -d %s"%extension,shell=True)
            time.sleep(speed)
            
disable_unimportant_extensions()


def enable_extensions():
    time.sleep(speed)
    for extension in extensions_to_enable:
        subprocess.call("gnome-shell-extension-tool -e %s"%extension,shell=True)
        time.sleep(speed)
        
enable_extensions()


print ("\nPlease Wait...\n")
subprocess.call("dconf reset -f  /org/gnome/shell/extensions/",shell=True)
def run_gsettings_commands():
    time.sleep(speed)
    for command in gsettings:
        subprocess.call(command,shell=True)
        time.sleep(speed)

run_gsettings_commands()


def run_dconf_commands():
    time.sleep(speed)
    for command in dconf:
        subprocess.call(command,shell=True)
        time.sleep(speed)

run_dconf_commands()

def run_gnome_terminal_commands():
    time.sleep(speed)
    for command in gnome_terminal:
        subprocess.call(command,shell=True)
        time.sleep(speed)

run_gnome_terminal_commands()

def run_terminix_commands():
    time.sleep(speed)
    for command in terminix:
        subprocess.call(command,shell=True)
        time.sleep(speed)

run_terminix_commands()

print ("\nFinish Reboot Your System\n")


