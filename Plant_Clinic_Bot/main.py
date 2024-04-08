import sys
from dist.__init__.reddit_bot import main

if __name__ == "__main__":
    args = sys.argv[1:]

    main(*args)