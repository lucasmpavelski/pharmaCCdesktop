#!/bin/sh

compiler=pyuic4

$compiler -o mainWindowUi.py mainWindow.ui

$compiler -o productIndexUi.py productIndex.ui
$compiler -o productFormUi.py productForm.ui

$compiler -o providerFormUi.py providerForm.ui
$compiler -o providerIndexUi.py providerIndex.ui

$compiler -o sellsFormUi.py sellsForm.ui
$compiler -o sellsIndexUi.py sellsIndex.ui
