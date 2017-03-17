const GObject = imports.gi.GObject;
const Gtk = imports.gi.Gtk;
const Lang = imports.lang;

const Extension = imports.misc.extensionUtils.getCurrentExtension();

const HelpWidget = new GObject.Class({
    Name: 'HelpWidget',
    GTypeName: 'HelpWidget',
    Extends: Extension.imports.preferences.preferenceWidget.PreferenceWidget,

    _init: function(setting, settings) {
        this.parent(setting, settings);
    }
});

/* vi: set expandtab tabstop=4 shiftwidth=4: */
