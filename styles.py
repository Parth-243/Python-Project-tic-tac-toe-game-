class GameStyles:
    # Color schemes
    COLORS = {
        'bg': '#2C3E50',        # Dark blue background
        'button': '#34495E',    # Lighter blue button
        'x': '#E74C3C',         # Red for X
        'o': '#2ECC71',         # Green for O
        'text': '#ECF0F1',      # White text
        'hover': '#465666',     # Hover effect
        'win': '#F1C40F'        # Yellow for winning combination
    }

    # Font styles
    FONTS = {
        'title': ('Helvetica', 32, 'bold'),
        'button': ('Helvetica', 24, 'bold'),
        'status': ('Helvetica', 16, 'normal'),
        'reset': ('Helvetica', 14, 'bold')
    }

    # Button styles
    BUTTON_STYLES = {
        'width': 3,
        'height': 1,
        'relief': 'raised',
        'borderwidth': 3,
        'padx': 5,
        'pady': 5
    }

    # Layout settings
    LAYOUT = {
        'padding': 20,
        'button_spacing': 5
    }

    # Messages
    MESSAGES = {
        'win': "🎉 Player {} wins! 🏆",
        'tie': "🤝 It's a tie! Well played! 🎮",
        'turn': "Player {}'s turn"
    }