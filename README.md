# irscript
Input Remapper text output macro generation based on variable inputs and keyboard layouts

## Short
Input Remapper helper script to transcode and translate text inputs to Input Remapper macros.

## Translation tables
Current translation tables to translate the inputs, by keyboard layout, like `german_de` or `english_us` (former needs work)
State for the translations which one might extend upon.

```python
conversion_table = {
    'german_de': {
        # german_de "qwertz" keyboard
        '°': 'Shift_R+dead_circumflex',
        '!': 'Shift_R+KEY_1',
        '"': 'Shift_R+KEY_2',
        '§': 'Shift_R+KEY_3',
        '$': 'Shift_R+KEY_4',
        '%': 'Shift_R+KEY_5',
        '&': 'Shift_R+KEY_6',
        '/': 'Shift_R+KEY_7',
        '(': 'Shift_R+KEY_8',
        ')': 'Shift_R+KEY_9',
        '\\': 'ISO_Level3_Shift+ssharp',
        '*': 'Shift_R+PLUS',
        '=': 'Shift_R+KEY_0',
        '#': 'numbersign',
        '?': 'Shift_R+ssharp',
        '[': 'ISO_Level3_Shift+8',
        ']': 'ISO_Level3_Shift+9',
        '{': 'ISO_Level3_Shift+7',
        '}': 'ISO_Level3_Shift+0',
        '~': 'ISO_Level3_Shift + plus',
        '^': 'dead_circumflex',
        '€': 'ISO_Level3_Shift+e',
        '<': 'less',
        '>': 'Shift_R+less',
        '+': 'plus',
        '-': 'minus',
        ',': 'comma',
        ';': 'Shift_R+comma',
        ':': 'Shift_R+period',
        '.': 'period',
        '_': 'Shift_R+minus',
        ' ': 'space',
        '´': 'Shift_L+dead_acute',
        '|': 'ISO_Level3_Shift + less',
        '\'': 'Shift_R+numbersign',
        '`': 'Shift_R+numbersign',
        '@': 'ISO_Level3_Shift+q',
        '\n': 'Return',
        '\t': 'Tab',
        '\b': 'BackSpace'
    },
    'english_us': {
        # english_us layout, needs work!
        # Should be tested/created with a original english keyboard
        '~': 'Shift_R+dead_circumflex',
        '!': 'Shift_R+KEY_1',
        '@': 'Shift_R+KEY_2',
        '#': 'Shift_R+KEY_3',
        '$': 'Shift_R+KEY_4',
        '%': 'Shift_R+KEY_5',
        '^': 'Shift_R+KEY_6',
        '&': 'Shift_R+KEY_7',
        '*': 'Shift_R+KEY_8',
        '(': 'Shift_R+KEY_9',
        ')': 'Shift_R+KEY_0',
        '<': 'less',
        '>': 'Shift_R+less',
        '+': 'plus',
        '-': 'minus',
        ',': 'comma',
        '.': 'period',
        ' ': 'space',
        '\n': 'Return',
        '\t': 'Tab',
        '\b': 'BackSpace'
    }
}
```

## Input text definitions dictionary

```python
input_strings = {
    'bash': {
        'your_custom_name': '#!/usr/bin/bash\n',
        'M6': 'for filename in $fileList; do\n\techo "$filename"\n\bdone\n',
        'M5': 'for item in "${arrayName[@]}"; do\n\techo "$item"\n\bdone\n',
        'M4': 'if [[ "$var" == true ]]; then\n\techo "$var"\n\bfi\n',
        'M3': 'firstChar="${text:0:1}"\n',
        'M2': 'charLength="${#text}"\n',
        'M1': 'case "$input" in\n\t\'a\'|\'c\')\n\techo "a" or "c"\n;;\n\b\'x\')\n\techo "x"\n;;\n\b*)\n\techo "everything-else"\n;;\n\b\besac\n\n'
    },
    'css': {
       'M6': 'name {\n\tkey: value\n\b}',
       'M5': '.className {\n\tcolor:darkblue;\nbackground: transparent\n\b}\n',
       'M4': 'background: linear-gradient(90deg, #005b1a 0%, #00621c 0%, #024515 100%);\n',
       'M3': 'margin:0;\npadding:0;\n',
       'M2': 'input[type="submit"] {\n\tcolor:green\b\n}',
       'M1': 'rgba(123, 80,10, 1.0);'
    },
    'inputremapper': {
       'M6': 'if_tap(\n\tif_tap(\n\tkey(a),\nkey(c)\n\b),\nkey(b)\n\b)\n'
    }
}
```

### Conversion triggering from within the script

Other examples are in the script too!

```python
# You can call it directly here or use the lang and your key value
# of the input string you want to translate.
MACRO_TEXT=text_2_macro(input_strings['inputremapper']['M6'], conversion_table['german_de'])
print('MACRO_TEXT')
print(MACRO_TEXT)
```



