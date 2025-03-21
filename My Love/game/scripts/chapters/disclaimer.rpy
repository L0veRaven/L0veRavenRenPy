image splash = "gui/presplash.png"

label splashscreen:

    show splash with dissolve

    $ persistent.quick_menu_display = False

    pause 1.0

    show text """
    \n
    {b}W A R N I N G{/b}\n\n
    This game contains depictions and themes of:\n
    harassment, stalking, assault, violence, and death.\n\n
    Please send all bug reports to {u}support@l0veraven.com{/u}
    """
    with dissolve

    pause 10.0

    hide text with dissolve
    hide splash with dissolve
    
    pause 2.0

    return