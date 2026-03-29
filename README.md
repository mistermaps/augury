# Augury

Augury is a terminal tarot reader with a keyboard-driven TUI, a scriptable CLI, and an optional Discord formatter/helper. It is designed to expose stable `augury` and `augury-discord` commands on `PATH`, even on systems where `pip` drops console scripts into a version-specific directory.

Created by **cassette, aka maps**  
Homepage: <https://cassette.help>

## Features

- Full-screen terminal UI for browsing cards, drawing readings, managing custom spreads, and reviewing history
- CLI commands for `read`, `daily`, `card`, `history`, `configure`, and `paths`
- JSON output for automation and scripting
- Optional Discord-friendly formatter via `augury-discord`
- Local preferences, custom spreads, and reading history stored in standard user config/data directories

## Installation

Install from a checkout:

```bash
pip install .
```

Then install stable launchers into `/usr/local/bin` by default, or `~/.local/bin` if `/usr/local/bin` is not writable:

```bash
python3 -m augury configure --no-input --install-launchers
```

Or, for a user-local CLI install:

```bash
pipx install .
```

Once installed, the package provides:

- `augury`
- `augury-discord`

The launcher install step above writes small wrapper scripts that execute `python -m augury` and
`python -m augury.discord` with the interpreter Augury was installed under. That keeps the binary
path stable for agents even if `pip` chose a versioned script directory internally.

## Quick Start

Launch the TUI:

```bash
augury
```

Draw a reading from the CLI:

```bash
augury read --spread three-card --query "What should I pay attention to this week?"
```

Emit machine-readable JSON without writing to history:

```bash
augury read --json --no-save --spread single --query "release check"
```

Inspect paths:

```bash
augury paths
```

Run setup and optionally install stable launchers:

```bash
augury configure
```

## Discord Integration

Augury ships with a formatter/parser module for Discord-style tarot commands.

Examples:

```bash
augury-discord handle "/tarot three What should I know?"
augury-discord card "The Fool"
augury-discord read --spread celtic-cross --query "What is the larger pattern?"
```

The `configure` flow can install stable `augury` and `augury-discord` launchers into a shared bin
directory. It still supports an explicit `augury-discord` helper path when you need one.

## Storage

By default Augury uses standard per-user config/data locations:

- Linux: `~/.config/augury` and `~/.local/share/augury`
- macOS: `~/Library/Application Support/augury`
- Windows: `%APPDATA%\\Augury` and `%LOCALAPPDATA%\\Augury`

You can override these with:

- `AUGURY_HOME`
- `AUGURY_CONFIG_DIR`
- `AUGURY_DATA_DIR`
- `AUGURY_BIN_DIR`

## Development

Run tests:

```bash
PYTHONPATH=src pytest
```

Run from a checkout without installing:

```bash
PYTHONPATH=src python -m augury
```

## TODO

- Replace the current `--interpret` stub with a real optional narrative/LLM mode
- Expand export/import support for readings and custom spreads
- Add data migration tooling from older private/local layouts
- Add broader automated coverage for the full-screen TUI interaction paths
- Package richer Discord integration examples beyond the formatter/helper CLI
- Support alternate decks, themes, and more presentation presets

## License

MIT. See [LICENSE](LICENSE).
