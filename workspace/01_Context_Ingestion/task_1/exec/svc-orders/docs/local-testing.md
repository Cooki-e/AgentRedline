# Local testing

From the repository root:

    python3 -m unittest discover -s tests -v

The formatter tests cover complete rows, absent optional notes, and
explicit `None` values from older API clients.
