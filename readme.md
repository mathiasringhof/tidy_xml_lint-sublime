# Format XML files using xmllint for Sublime Text 2

Uses ´xmllint´ to format either the whole file or the current selection.

Nearly all code from http://www.bergspot.com/blog/2012/05/formatting-xml-in-sublime-text-2-xmllint/
Added code to check if some text is selected, if not formats the whole document.

Tested on OSX Lion w/ Xcode and Developer tools installed.
*not sure if this will work for Windows or Linux*

## Installing
**Without Git:** Download the latest source zip from [github](https://github.com/mathiasringhof/tidy_xml_lint-sublime/zipball/master) and extract the files to your Sublime Text "Packages" directory, into a new directory named `tidy_xml_lint`.

**With Git:** Clone the repository in your Sublime Text "Packages" directory:

    git clone git://github.com/mathiasringhof/tidy_xml_lint-sublime.git tidy_xml_lint

The "Packages" directory is located at:

* OS X:
    `~/Library/Application Support/Sublime Text 2/Packages/`
* Linux:
    `~/.Sublime Text 2/Packages/`
* Windows:
    `%APPDATA%/Sublime Text 2/Packages/`