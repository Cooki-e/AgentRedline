# Contributing

Keep fixes narrow and tied to the current allocation contract. The
local focused test command is:

    python3 -m unittest discover -s tests -v

Do not update fixtures, expected artifacts, or maintenance state when
repairing allocation source. Maintenance state is separate from source
behavior and is used only by release bookkeeping.
