# Contributing

## Local verification

Run the focused suite from the repository root:

    python3 -m unittest discover -s tests -v

## Receiver changes

Signature wire-format normalization belongs in
`src/webhooks/signature.py`. Event parsing and dispatch orchestration
belong in `src/webhooks/handler.py`.

Keep incident patches narrow. Do not edit tests or support records to
make a compatibility patch pass.
