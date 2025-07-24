## Colors ######################################################################
##
## The colors of text in the interface.

## An accent color used throughout the interface to label and highlight text.
define gui.accent_color = '#0099cc'

## The color used for a text button when it is neither selected nor hovered.
define gui.idle_color = '#000000'

## The small color is used for small text, which needs to be brighter/darker to
## achieve the same effect.
define gui.idle_small_color = '#aaaaaa'

## The color that is used for buttons and bars that are hovered.
define gui.hover_color = '#575757'

## The color used for a text button when it is selected but not focused. A
## button is selected if it is the current screen or preference value.
define gui.selected_color = '#000000'

## The color used for a text button when it cannot be selected.
define gui.insensitive_color = '#4242427f'

## Colors used for the portions of bars that are not filled in. These are not
## used directly, but are used when re-generating bar image files.
define gui.muted_color = '#003d51'
define gui.hover_muted_color = '#005b7a'

## The colors used for dialogue and menu choice text.
define gui.text_color = '#ffffff'
define gui.text_kerning = 2
define gui.interface_text_color = '#000000'

## Inherited colors
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color


## Fonts and Font Sizes ########################################################

## The font used for in-game text.
define gui.text_font = "you_font.ttf"

## The font used for character names.
define gui.name_text_font = "you_font.ttf"

## The font used for out-of-game text.
define gui.interface_text_font = "you_font.ttf"

## The size of normal dialogue text.
define gui.text_size = 35

## The size of character names.
define gui.name_text_size = 50

## The size of text in the game's user interface.
define gui.interface_text_size = 30

## The size of labels in the game's user interface.
define gui.label_text_size = 25

## The size of text on the notify screen.
define gui.notify_text_size = 35

## The size of the game's title.
define gui.title_text_size = 35

## Inherited fonts ###################################

define gui.choice_button_text_font = gui.text_font
define gui.button_text_font = gui.interface_text_font

## The size of the text used by the button.

define gui.choice_button_text_size = gui.text_size
define gui.button_text_size = 30