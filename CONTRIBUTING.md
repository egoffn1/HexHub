# HexHub Contribution Guide

Thank you for your interest in contributing to HexHub! This guide will help you add drivers, protocols, and tools to our community-driven database.

## 📁 Data Storage

All data files are stored in the **`data`** branch, not in `main`. This keeps the main branch clean and focused on documentation and tooling.

## 🚀 How to Contribute

### Step 1: Fork the Repository

1. Go to https://github.com/egoffn1/HexHub
2. Click the "Fork" button in the top-right corner
3. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/HexHub.git
   cd HexHub
   ```

### Step 2: Checkout the Data Branch

```bash
git checkout data
```

If the branch doesn't exist locally yet:
```bash
git fetch origin data
git checkout data
```

### Step 3: Add Your Entry

Choose the appropriate file based on what you're adding:

- **`drivers.json`**: Hardware drivers (GPU, Network, Audio, etc.)
- **`protocols.json`**: Communication protocols (USB, PCIe, SATA, etc.)
- **`tools.json`**: Diagnostic and management tools

#### Example: Adding a Driver

Edit `drivers.json` and add a new entry following the schema:

```json
{
  "name": "Your Driver Name",
  "description": "Brief description of what this driver does",
  "category": "GPU",
  "vendor": "Vendor Name",
  "hardware_ids": ["VEN_1234&DEV_5678"],
  "installation": {
    "windows": {
      "command": "winget install vendor.driver",
      "url": "https://vendor.com/drivers/download"
    },
    "linux": {
      "debian": "sudo apt install driver-package",
      "rhel": "sudo dnf install driver-package",
      "arch": "sudo pacman -S driver-package",
      "generic": "git clone https://repo.com/driver && make && sudo make install"
    },
    "macos": {
      "brew": "brew install driver-cask",
      "url": "https://vendor.com/macos-driver"
    }
  }
}
```

### Step 4: Validate Your Changes

Ensure your JSON is valid:

```bash
python -m json.tool drivers.json > /dev/null && echo "JSON is valid"
```

### Step 5: Commit and Push

```bash
git add drivers.json  # or protocols.json, tools.json
git commit -m "Add driver: [Driver Name] for [Hardware]"
git push origin data
```

### Step 6: Create a Pull Request

1. Go to your fork on GitHub
2. Switch to the `data` branch
3. Click "Pull Request"
4. Select base repository: `egoffn1/HexHub`, base branch: `data`
5. Fill out the PR template
6. Submit!

## 📋 Data Schema Requirements

### Drivers (`drivers.json`)

Required fields:
- `name` (string): Human-readable name
- `description` (string): What the driver does
- `category` (string): One of: `GPU`, `Network`, `Audio`, `Storage`, `Chipset`, `Input`, `Printer`, `Virtualization`, `Other`
- `vendor` (string): Manufacturer name
- `hardware_ids` (array): PCI/USB IDs or other identifiers
- `installation` (object): Installation commands per OS

### Protocols (`protocols.json`)

Required fields:
- `name` (string): Protocol name
- `description` (string): What the protocol does
- `type` (string): e.g., `Serial`, `Parallel`, `Network`, `Storage`
- `specification_url` (string): Link to official spec
- `common_implementations` (array): List of implementations

### Tools (`tools.json`)

Required fields:
- `name` (string): Tool name
- `description` (string): What the tool does
- `category` (string): e.g., `Diagnostic`, `Monitoring`, `Flashing`, `Benchmark`
- `platform` (array): Supported platforms: `windows`, `linux`, `macos`
- `installation` (object): Installation commands per platform
- `homepage` (string): Project homepage

## ✅ Quality Guidelines

1. **Accuracy**: Verify all commands work before submitting
2. **Completeness**: Fill all required fields
3. **Clarity**: Use clear, concise descriptions
4. **Sources**: Include links to official sources when possible
5. **Testing**: Test commands on actual hardware when feasible

## 🔍 Review Process

1. Automated CI checks validate JSON syntax
2. Maintainers review for accuracy and completeness
3. Community feedback period (48 hours)
4. Merge upon approval

## ❓ Questions?

- Open an issue for questions
- Check existing issues for answers
- Join discussions in PRs

## 🙏 Thank You!

Every contribution makes HexHub better for everyone. Thank you for helping build the ultimate hardware spellbook! 🧙‍♂️
