'''
    Input Remapper helper script to transcode and translate
    text inputs to Input Remapper macros.
'''
#-----------------------------------------------------------------
# Some translation dictionary - for a German "qwertz" keyboard,
# but you can and should adapt of course!
#
# Refining is "likely" needed, just check your input
# from "1","2", "3"... to the "0" key, using "Shift_R" and so on.
# And special characters you need.
# This might help figure out the main char combinations.
#

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

# Here starts the input to generate the macros from
# its some bash shortcuts I want to use to make
# my life easier in the future, thx Input Remapper and
# the original author "W-L"!
'''
    Note - the "notUsedYet" and "M6" to "M1" are just for easier
    navigation inside the macro strings. Bare with me, you will
    find that pretty handy.

    Because I got lost when testing here first..
    to which key the macro was made for!

    You can name it any value you want, just keep
    them "unique" inside the dictionary.
'''

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

#
# Original by "W-L", modified slightly, see source:
# https://github.com/sezanzeb/input-remapper/issues/173
#
# Uppercase modifier key is by default "Shift_R" here
#
UPPERCASE_KEY='Shift_R'

#
# This function does the magic and returns the macro text
# You can call it directly here or use the lang
#
# You likely need not to modify here, but if you find
# some room for improvement, go ahead of course! :)

def text_2_macro(input_text, translate_dictionary):
    '''
    Input text to convert and do the conversion
    according to the translation table.

    You might not need to change anything here.
    Just be sure to set your "UPPERCASE_KEY"
    before this function call in the script
    if not "Shift_R".
    '''

    macro_list = []
    for c in input_text:
        try:
            if c.isalnum():
                if c.isupper():
                    macro_list.append(f"modify({UPPERCASE_KEY}, key({c})).wait(1)")
                else:
                    macro_list.append(f"key({c}).wait(1)")
            else:
                # translate character to input-remapper macro
                if '+' in translate_dictionary[c]:
                    a, b = translate_dictionary[c].split('+', 2)
                    macro_list.append(f"modify({a}, key({b})).wait(1)")
                else:
                    macro_list.append(f"key({translate_dictionary[c]}).wait(1)")

        except KeyError:
            # If a key is not defined but used in "input_text"
            # this error is shown in the console!
            print(f"Symbol for: ' {c} ' not in translation table.")

    return '.'.join(macro_list)

#-----------------------------------------------------------------
# Helper function to choose a "lang" for the shortcuts
# so it can be extended freely! :)
#-----------------------------------------------------------------
def create_macros_for(lang, translation_table, no_print_do_return=False):
    '''
    Helper function to select and translate by language/flavour,
    so there is no need to start from scratch by allowing a
    "lang" key and keystring to be added or extended on.

    If you enter something else what is no there, you
    get a list of possible keys.

    It prints the results of all lang entries to console
    if "no_print_do_return" is "False" (default), otherwise
    a dictionary with each generated macro item for "lang" is
    returned.

    It is a dictionary for reason, to easier distinguish
    your assigned key, you can change this values, depeding
    on your needs.
    '''

    if not lang in input_strings:
        print(f'Language key not found, you entered "{lang}", available are:')
        for subkey in input_strings[lang]:
            print(subkey)

        return

    if no_print_do_return:
        macro_dictionary={}
        for subkey in input_strings[lang]:
            macro_text=[]
            for index, input_text in enumerate(input_strings[lang][subkey]):
                #-----------------------------------------------------------------
                # This function call does all the work..
                macro_text_output=text_2_macro(input_text, translation_table)

                # Add to return array
                macro_text.append(macro_text_output)
                #-----------------------------------------------------------------
            macro_dictionary[subkey] = '.'.join(macro_text)
        return macro_dictionary

    for index, subkey in enumerate(input_strings[lang]):
        print(f'\n# MACRO "{lang}" "{subkey}" {index+1}')

        # This function call does all the work..
        macro_text_output=text_2_macro(input_strings[lang][subkey], translation_table)
        print(macro_text_output)

        print(f'#/MACRO "{lang}" "{subkey}" {index+1}\n')

#-----------------------------------------------------------------
# You can call it directly here or use the lang and your key value
# of the input string you want to translate.
MACRO_TEXT=text_2_macro(input_strings['inputremapper']['M6'], conversion_table['german_de'])
print('MACRO_TEXT')
print(MACRO_TEXT)

for key, input_string in input_strings['bash'].items():
    print(f'\nOUTPUT MACRO "{key}"   ----------------------------------------------------------------')
    MACRO_TEXT=text_2_macro(input_string, conversion_table['german_de'])
    print(MACRO_TEXT)
    print('\n')

#-----------------------------------------------------------------
# Prints directly
create_macros_for('inputremapper', conversion_table['german_de'], False)
#create_macros_for('bash', conversion_table['german_de'], False)

#-----------------------------------------------------------------
# Return dictionary with each entry in "lang" by keyboard layout
#MACRO_DICTIONARY = create_macros_for('inputremapper', conversion_table['german_de'], True)
MACRO_DICTIONARY = create_macros_for('bash', conversion_table['german_de'], True)

# How to print out :)
for key in MACRO_DICTIONARY:
    print(f'KEY: {key}')
    print(MACRO_DICTIONARY[key])
    print()
#-----------------------------------------------------------------
# / END OF SCRIPT
#-----------------------------------------------------------------
