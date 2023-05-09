// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "pho-visually-distinct-tabs" is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with registerCommand
	// The commandId parameter must match the command field in package.json
	let disposable = vscode.commands.registerCommand('pho-visually-distinct-tabs.helloWorld', () => {
		// The code you place here will be executed every time your command is executed
		// Display a message box to the user
		vscode.window.showInformationMessage('Hello World from pho-visually-distinct-tabs!');
	});

	context.subscriptions.push(disposable);

	let disposable2 = vscode.commands.registerCommand('pho-visually-distinct-tabs.changeTabColor', function () {
		vscode.window.visibleTextEditors.forEach(function (editor) {
			if (editor.document.fileName.endsWith('.md')) {
				let index = vscode.window.visibleTextEditors.indexOf(editor);
				vscode.window.visibleTextEditors[index].setDecorations(editorDecorationType, { backgroundColor: 'green' });
			}
		});
	});
	context.subscriptions.push(disposable2);

}

// This method is called when your extension is deactivated
export function deactivate() {}

const editorDecorationType = vscode.window.createTextEditorDecorationType({
	backgroundColor: 'green'
});
