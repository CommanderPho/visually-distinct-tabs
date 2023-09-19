# pho-visually-distinct-tabs README

Allows setting special file icons 


## 2023-05-09 - File Icon Theme Aproach:

https://code.visualstudio.com/api/extension-capabilities/theming

File Icon Theme: A mapping from file type / file name to images. File icons are displayed across the VS Code UI in places such as File Explorer, Quick Open List, and Editor Tab.


#### Resources
https://code.visualstudio.com/api/extension-guides/file-icon-theme
https://github.com/microsoft/vscode/tree/main/extensions/theme-defaults
https://github.com/microsoft/vscode/tree/main/extensions/theme-seti

## 2023-05-09 - Might not be possible with an extension:

From https://code.visualstudio.com/api/extension-capabilities/overview
```text
No DOM Access

Extensions have no access to the DOM of VS Code UI. You cannot write an extension that applies custom CSS to VS Code or adds an HTML element to VS Code UI.

At VS Code, we're continually trying to optimize use of the underlying web technologies to deliver an always available, highly responsive editor and we will continue to tune our use of the DOM as these technologies and our product evolve. To ensure that extensions cannot interfere with the stability and performance of VS Code, and that we can continue to improve the DOM of VS Code without breaking existing extensions, we run extensions in an Extension Host process and prevent direct access to the DOM.
No custom style sheets

A custom style sheet provided by users or extensions would work against the DOM structure and class names. These are not documented as we consider them internal. To evolve, refactor, or improve VS Code, we need the freedom to make changes to the user interface. Any change to the DOM can break existing custom style sheets, resulting in frustration for style sheet providers and a bad user experience with UI glitches coming from the broken style sheet.

Instead, VS Code aims to provide a well-designed extension API supporting UI customizations. The API is documented, comes with tooling and samples, and is kept stable across all upcoming releases of VS Code.
```


## Features

Describe specific features of your extension including screenshots of your extension in action. Image paths are relative to this README file.

For example if there is an image subfolder under your extension project workspace:

\!\[feature X\]\(images/feature-x.png\)

> Tip: Many popular extensions utilize animations. This is an excellent way to show off your extension! We recommend short, focused animations that are easy to follow.

## Requirements

If you have any requirements or dependencies, add a section describing those and how to install and configure them.

## Extension Settings

Include if your extension adds any VS Code settings through the `contributes.configuration` extension point.

For example:

This extension contributes the following settings:

* `myExtension.enable`: Enable/disable this extension.
* `myExtension.thing`: Set to `blah` to do something.

## Known Issues

Calling out known issues can help limit users opening duplicate issues against your extension.

## Release Notes

Users appreciate release notes as you update your extension.

### 1.0.0

Initial release of ...

### 1.0.1

Fixed issue #.

### 1.1.0

Added features X, Y, and Z.


