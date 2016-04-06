from aenea import (
    Key,
    Text,
    Mouse,
)
from dragonfly import Function
import re

def clean_prose(text):
    print "was: " + str(text)
# strip out the \punctuation that Dragon adds in for some reason:
    text = re.sub(r'\\[a-z-]+', r'', str(text))
# fix the spacing around punctuation:
    text = re.sub(r' ,', r',', text)
    text = re.sub(r' \?', r'? ', text)
    text = re.sub(r' \!', r'! ', text)
    text = re.sub(r' \.', r'. ', text)
    text = re.sub(r' \:', r':', text)
    text = re.sub(r' \;', r';', text)
# capitalize the letter I if it's a word on its own:
    text = re.sub(r'^i ', r'I ', text)
    text = re.sub(r' i ', r' I ', text)
# be smart about the spaces at the end of dictation:
    # text = re.sub(r'$', r' ', text)
    # text = re.sub(r' $', r'', text)
    text = re.sub(r'[ ]+', r' ', text)
# if these punctuation characters are on their own then don't have any spacing:
    # text = re.sub(r'^, $', r',', text)
    text = re.sub(r'^\: $', r':', text)
    text = re.sub(r'^\. $', r'.', text)
    text = re.sub(r'^\; $', r';', text)
    text = re.sub(r'^\! $', r'!', text)
    return text

def cap_that(text):
    text = clean_prose(str(text))
    text = text.capitalize()
    print "typing: " + text
    return Text(text).execute()

def lower_that(text):
    text = clean_prose(str(text))
    print "typing: " + text
    return Text(text).execute()

letterMap = {
    "(alpha|arch)": "a",
    "(bravo) ": "b",
    "(charlie|char) ": "c",
    "(delta) ": "d",
    "(echo|eck) ": "e",
    "(foxtrot|fox) ": "f",
    "(golf|gee) ": "g",
    "(hotel) ": "h",
    "(india|ice) ": "i",
    "(juliet) ": "j",
    "(kilo) ": "k",
    "(lug) ": "l",
    "(mike) ": "m",
    "(november) ": "n",
    "(oscar|ork) ": "o",
    "pooch ": "p",
    "(quebec|queen) ": "q",
    "(romeo) ": "r",
    "(sierra|souk) ": "s",
    "(tango) ": "t",
    "(union|unks) ": "u",
    "(victor|verge) ": "v",
    "(whiskey|womp) ": "w",
    "(x-ray) ": "x",
    "(yankee) ": "y",
    "(zulu) ": "z",
}

numberMap = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "duo": "2",
    "three": "3",
    "four": "4",
    "quad": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

controlKeyMap = {
    "left": "left",
    "right": "right",
    "up": "up",
    "down": "down",
    "page up": "pgup",
    "page down": "pgdown",
    "home": "home",
    "end": "end",
    "space": "space",
    "(enter|return)": "enter",
    "escape": "escape",
    "tab": "tab",
    "backspace": "backspace"
}

specialCharMap = {
    # "(bar|vertical bar|pipe)": "|",
    # "(dash|minus|hyphen)": "-",
    # "(dot|period)": ".",
    "calm": "comma",
    "backslash": "backslash",
    # "underscore": "_",
    # "asterisk": "*",
    # "colon": ":",
    # "semi-col": ";",
    # "at symbol": "@",
    # "[double] quote": """,
    # "single quote": """,
    # "pound|hash": "#",
    # "dollar": "$",
    # "percent": "%",
    # "and": "&",
    "slash": "slash",
    # "equal": "=",
    # "plus": "+",
    # "space": " "
}

release = Key("shift:up, ctrl:up, alt:up, win:up")

# Modifiers for the press-command.
modifierMap = {
    "alt|option": "a",
    "control": "c",
    "shift": "s",
    "command": "w",
}

# Modifiers for the press-command, if only the modifier is pressed.
singleModifierMap = {
    "alt|option": "a",
    "control": "c",
    "shift": "s",
    "command": "w",
}

pressKeyMap = {}
pressKeyMap.update(letterMap)
pressKeyMap.update(numberMap)
pressKeyMap.update(controlKeyMap)
pressKeyMap.update(specialCharMap)

# These words can be prefaced by the word "say"
reservedWord = {
    "up": "up",
    "down": "down",
    "left": "left",
    "right": "right",
    "space": "space",
    "tab": "tab",
    "backspace": "backspace",
    "delete": "delete",
    "enter": "enter",
    "paste": "paste",
    "copy": "copy",
    "cut": "cut",
    "undo": "undo",
    "release": "release",
    "page up": "page up",
    "page down": "page down",
    "say": "say",
    "select": "select",
    "uppercase": "uppercase",
    "lowercase": "lowercase",
    "expand": "expand",
    "squash": "squash",
    "dash": "dash",
    "underscore": "underscore",
    "dot": "dot",
    "period": "period",
    "minus": "minus",
    # "semicolon": "semi-colon",
    "semi": "semi",
    "hyphen": "hyphen",
    "triple": "triple",
    "kill": "kill",
    "to end": "to end",
    "slap": "slap",
    "pound": "pound",
    "hash": "hash",
    "escape": "escape",
}

nonVimGenericKeys = {
    "say <text>": Function(lower_that),
    "cap <text>": Function(cap_that),

    "[<n>] up": Key("up:%(n)d"),
    "[<n>] down": Key("down:%(n)d"),
    "[<n>] left": Key("left:%(n)d"),
    "[<n>] right": Key("right:%(n)d"),

    "undo [<n>]": Key("w-z:%(n)d"),
    "redo [<n>]": Key("sw-z:%(n)d"),
    "kill [<n>]": Key("del:%(n)d"),
    "kill to end": Key("c-k"),
    "cut line": Key("c-a, sw-right, w-x, w-right, del"),
    "copy line": Key("w-left, sw-right, w-c, w-right"),
    "copy [that]": Key("w-c"),
    "cut [that]": Key("w-x"),
    "paste [that]": Key("w-v"),

    "home": Key("w-left"),
    "end": Key("w-right"),
    "go to top": Key("w-up"),
    "go to bottom": Key("w-down"),

    "dupe line": Key("w-left, ws-right, w-c, w-right, enter, w-v"),
    "sell line": Key("w-left, ws-right"),
    'sell to start': Key('ws-left'),
    'sell to end': Key('ws-right'),
    'sell to top': Key('ws-up'),
    'sell to bottom': Key('ws-down'),

    "bit [<n>]": Key("a-left:%(n)d"),
    "fit [<n>]": Key("a-right:%(n)d"),
    "de-bit [<n>]": Key("sa-left:%(n)d") + Key("del"),
    "de-fit [<n>]": Key("sa-right:%(n)d") + Key("del"),

    "save file": Key("w-s"),
    "space [<n>]": Key("space:%(n)d"),
    "<letters>": Key("%(letters)s"),
    "sky <letters>": Key("s-%(letters)s"),
    "num <numbers>": Key("%(numbers)s"),
    "<numbers>": Key("%(numbers)s"),
    "(del|chuck) [<n>]": Key("backspace:%(n)d"),

    "<specials> [<n>]": Key("%(specials)s:%(n)d"),
    "(slap|slop) [<n>]": Key("enter:%(n)d"),
}

specialKeys = {
    "ampersand": "ampersand",
    "apostrophe": "apostrophe",
    "asterisk": "asterisk",
    "at symbol": "at",
    "backslash": "backslash",
    "backtick": "backtick",
    "bar": "bar",
    "caret": "caret",
    "colon": "colon",
    "calm": "comma",
    "dollar": "dollar",
    "dot": "dot",
    # "period": "dot,space",
    "semi": "semicolon",
    "quote": "dquote",
    "equals": "space, equal, space",
    "bang": "exclamation",
    "hash": "hash",
    "hyphen": "hyphen",
    "escape": "escape",
    "minus": "minus",
    "percent": "percent",
    "plus": "plus",
    "quest mark": "question",
    "slash": "slash",
    "single quote": "squote",
    "tilde": "tilde",
    "underscore": "underscore",
    "tab": "tab",
    "langle": "langle",
    "lace": "lbrace",
    "lack": "lbracket",
    "lap": "lparen",
    "rangle": "rangle",
    "race": "rbrace",
    "rack": "rbracket",
    "rap": "rparen",
}

genericKeys = {
    "release all": release,
    "press shift": Key("shift:down"),
    "release shift": Key("shift:up"),
    "press <pressKey>": Key("%(pressKey)s"),

    "say <reservedWord>": Text("%(reservedWord)s"),

 # Navigation keys.
    "page up [<n>]": Key("pgup:%(n)d"),
    "page down [<n>]": Key("pgdown:%(n)d"),


    "<modifier1> <pressKey> [<n>]":
      Key("%(modifier1)s-%(pressKey)s:%(n)d"),
    "<modifier1> <modifier2> <pressKey> [<n>]":
      Key("%(modifier1)s%(modifier2)s-%(pressKey)s:%(n)d"),

    "tick": Mouse("left"),
    "dub": Mouse("left:2"),
    "tock": Mouse("right"),
}
