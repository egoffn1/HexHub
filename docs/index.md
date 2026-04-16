# HexHub Documentation

Welcome to the HexHub documentation site. This documentation provides detailed information about using and contributing to HexHub.

## Table of Contents

- [Getting Started](#getting-started)
- [Data Structure](#data-structure)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [FAQ](#faq)

---

## Getting Started

### What is HexHub?

HexHub is a cross-platform hardware spellbook - a centralized database of drivers, protocols, and diagnostic tools with ready-to-paste commands for Linux, Windows, and macOS.

### Quick Start

```bash
# Clone the repository
git clone https://github.com/egoffn1/HexHub.git
cd HexHub

# Generate README from data
python scripts/generate_readme.py

# Validate your changes
python -m json.tool data/drivers.json > /dev/null
```

---

## Data Structure

### Drivers Schema

Each driver entry in `drivers.json` follows this structure:

```json
{
  "name": "string (required)",
  "description": "string (required)",
  "category": "enum (required)",
  "vendor": "string (required)",
  "hardware_ids": ["array of strings"],
  "installation": {
    "windows": {
      "command": "string",
      "url": "string"
    },
    "linux": {
      "debian": "string",
      "rhel": "string",
      "arch": "string",
      "generic": "string"
    },
    "macos": {
      "brew": "string",
      "url": "string"
    }
  }
}
```

### Categories

Valid categories for drivers:
- `GPU` - Graphics processing units
- `Network` - Network adapters and wireless cards
- `Audio` - Sound cards and audio devices
- `Storage` - Storage controllers and drives
- `Chipset` - Motherboard chipsets
- `Input` - Keyboards, mice, and input devices
- `Printer` - Printers and scanners
- `Virtualization` - Virtual device drivers
- `Other` - Other hardware

---

## API Reference

### generate_readme.py

The main script that generates README content.

**Usage:**
```bash
python scripts/generate_readme.py
```

**Markers:**
The script looks for these HTML comments in README.md:
- `<!-- BEGIN_DRIVERS_TABLE -->...<!-- END_DRIVERS_TABLE -->`
- `<!-- BEGIN_INSTALLATION_DETAILS -->...<!-- END_INSTALLATION_DETAILS -->`
- `<!-- BEGIN_QUICK_COMMANDS -->...<!-- END_QUICK_COMMANDS -->`

---

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed contribution guidelines.

### Quick Contribution Guide

1. Fork the repository
2. Create a new branch
3. Make your changes to JSON files
4. Run `python scripts/generate_readme.py`
5. Validate JSON: `python -m json.tool data/drivers.json`
6. Commit and create a Pull Request

---

## FAQ

### Q: Why JSON and not a database?
A: JSON is human-readable, version-control friendly, and doesn't require any server setup. It's perfect for a community-driven project.

### Q: How often is the README updated?
A: The README is automatically regenerated on every pull request via GitHub Actions.

### Q: Can I use HexHub data in my project?
A: Yes! HexHub is licensed under MIT. You can use the data freely in your projects.

### Q: How do I find hardware IDs for my device?
A: 
- **Windows:** Device Manager → Properties → Details → Hardware Ids
- **Linux:** `lspci -nn` for PCI devices, `lsusb` for USB devices
- **macOS:** System Information → Hardware

---

## Support

- **Issues:** [GitHub Issues](https://github.com/egoffn1/HexHub/issues)
- **Discussions:** [GitHub Discussions](https://github.com/egoffn1/HexHub/discussions)
- **Email:** egoffn1@users.noreply.github.com

---

*Last updated: 2026*
