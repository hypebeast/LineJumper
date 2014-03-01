# LineJumper

LineJumper is a Sublime Text 3 plugin that adds commands to move your cursor and select
10 lines (or less or more) at a time.

It's inspired by [Line Jumper](https://atom.io/packages/line-jumper) for [Atom](https://atom.io).

## Installation

 * recommended is to use [Sublime Package
   Manager](http://wbond.net/sublime_packages/package_control#Features)
 * press `Ctrl+Shift+P` then `Package Control: Install Package`
 * look for `LineJumper` and install it.

## Usage

The LineJumper package adds four new commands to Sublime Text with the following default keybindings:

 * `alt-up` to move the cursor up 10 lines
 * `alt-down` to move the cursor down 10 lines
 * `alt-shift-up` to select up 10 lines
 * `alt-shift-down` to select down 10 lines

These commands are also available through the Command Palette. Press `Ctrl+Shift+P`
and then select from one of the following commands:

 * `LineJumper: Move up lines`
 * `LineJumper: Move down lines`
 * `LineJumper: Select up lines`
 * `LineJumper: Select down lines`

## Configuration

You can change the number of lines jumped by LineJumper in the settings file:

 * press `Ctrl+Shift+P` then `Preferences: LineJumper Settings – User`
 * and add the `number_of_lines` option
 * see `Preferences: LineJumper Settings – Default` for a example

or in the keybindings file:

 * press `Ctrl+Shift+P` then `Preferences: LineJumper Key Bindings – User`
 * and add a line like this:
   `{ "keys": ["alt+shift+up"], "command": "line_jumper", "args": { "number_of_lines": 10, "cmd": "up_select" } },`
 * open the default keybindings `Preferences: LineJumper Key Bindings – Default` to see all available commands


## License

Copyright (c) 2014 Sebastian Ruml <sebastian.ruml@gmail.com>

Released under The MIT License.

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
