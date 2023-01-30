"""Start game module - operating script."""
from menu import menu
from player import Hero
import connector


def main():
    """Main function."""
    # Player initialization.
    player = Hero((500, 659))
    menu()
    connector.run_game_again(player)
    # connector.return_to_village(player)


if __name__ == "__main__":
    main()
