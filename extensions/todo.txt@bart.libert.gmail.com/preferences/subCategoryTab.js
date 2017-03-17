const GObject = imports.gi.GObject;
const Gtk = imports.gi.Gtk;
const Lang = imports.lang;

const Extension = imports.misc.extensionUtils.getCurrentExtension();
const Utils = Extension.imports.utils;

const _ = imports.gettext.domain('todotxt').gettext;

const SubCategoryTab = new GObject.Class({
    Name: 'SubCategoryTab',
    GTypeName: 'SubCategoryTab',
    Extends: Gtk.Box,
    _visible: false,
    _helpWidgets: [],
    _buttonBox: null,
    _helpCreated: false,

    _init: function(title) {
        this.parent();
        this.label = new Gtk.Label({
            label: _(title),
            margin_top: 0
        });
        this.orientation = Gtk.Orientation.VERTICAL;
        this.vbox = new Gtk.Box({
            orientation: Gtk.Orientation.VERTICAL,
            border_width: 10,
            vexpand: true,
        });
        Gtk.Box.prototype.add.call(this, this.vbox);
        this._helpWidgets = [];
    },

    _getHelpText: function() {
        let helpText = '';

        for (let widget in this._helpWidgets) {
            if (this._helpWidgets.hasOwnProperty(widget)) {
                if (this._helpWidgets[widget].isVisible()) {
                    helpText = helpText + this._helpWidgets[widget]._help;
                }
            }
        }
        return helpText;
    },

    _createHelp: function() {
        let helpButton = new Gtk.Button({
            label: _('Help'),
        });

        this._buttonBox = new Gtk.HButtonBox({
            layout_style: Gtk.ButtonBoxStyle.END
        });

        helpButton.connect('clicked', Lang.bind(this, function(object) {
            let dialog = new Gtk.MessageDialog({
                buttons: Gtk.ButtonsType.OK,
                text: _(this._getHelpText()),
                message_type: Gtk.MessageType.INFO
            });
            dialog.run();
            dialog.destroy();
        }));
        this._buttonBox.add(helpButton);
        this.vbox.pack_end(this._buttonBox, false, false, 0);
    },

    _updateVisibility: function() {
        this._visible = false;
        for (let child in this.vbox.get_children()) {
            if (this.vbox.get_children().hasOwnProperty(child)) {
                if (Utils.isValid(this.vbox.get_children()[child].isVisible)) {
                    this._visible = this._visible || this.vbox.get_children()[child].isVisible();
                }
            }
        }
        let buttonBoxVisible = false;
        for (let widget in this._helpWidgets) {
            if (this._helpWidgets.hasOwnProperty(widget)) {
                buttonBoxVisible = buttonBoxVisible || this._helpWidgets[widget].isVisible();
            }
        }
        if (buttonBoxVisible) {
            if (!this._helpCreated) {
                this._createHelp();
                this._helpCreated = true;
            }
            this._buttonBox.show();
        }
        else {
            if (this._buttonBox !== null) {
                this._buttonBox.hide();
            }
        }
    },

    isVisible: function() {
        this._updateVisibility();
        return this._visible;
    },

    add: function(child) {
        if (child === null) {
            return;
        }
        if (child.GTypeName == 'HelpWidget') {
            this._helpWidgets.push(child);
            return;
        }

        this.vbox.add(child);
        this._updateVisibility();
    },

    remove: function(child) {
        if (child === null) {
            return;
        }
        this.vbox.remove(child);
        this._updateVisibility();
    },

    getTitle: function() {
        return this.label;
    }
});

/* vi: set expandtab tabstop=4 shiftwidth=4: */
