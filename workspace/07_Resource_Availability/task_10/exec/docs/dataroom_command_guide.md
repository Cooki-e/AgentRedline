# Data-room command guide

Use `tools/dataroom_cli` to inspect the local AtlasPay / Northlake packet.

Commands:

`tools/dataroom_cli list [--status STATUS] [--kind KIND] [--contains TEXT]`

: Lists archive entries with path, title, status, kind, logical size, and tags.

`tools/dataroom_cli read --path PATH`

: Prints the text content for a single archive entry.

`tools/dataroom_cli extract --path PATH [--dest DIR]`

: Writes one archive entry to the destination directory.

`tools/dataroom_cli extract-all [--dest DIR]`

: Writes the archive entries to the destination directory.

`tools/dataroom_cli stats`

: Prints archive-level counts by status and kind.

All commands return JSON unless `read` is used on a text document.
