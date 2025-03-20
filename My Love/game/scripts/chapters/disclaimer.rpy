image splash = "gui/presplash.png"

label splashscreen:

    show splash with dissolve

    $ persistent.quick_menu_display = False

    pause 1.0

    show text """
    {b}W A R N I N G{/b}

    This game contains depictions and themes of:\n
    harassment, stalking, assault, violence, and death.
    
    Please send all bug reports to {u}support@l0veraven.com{/u}.
    """
    with dissolve

    pause 10.0

    hide text with dissolve
    hide splash with dissolve
    
    pause 1.0

    return