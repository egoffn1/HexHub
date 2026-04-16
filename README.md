# HexHub 🧙‍♂️

> **The cross-platform spellbook for hardware.**  
> Centralized database of drivers, protocols, and diagnostic tools with ready-to-paste commands for Linux, Windows, and macOS.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/egoffn1/HexHub.svg)](https://github.com/egoffn1/HexHub/stargazers)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](../CONTRIBUTING.md)

## 📦 About This Branch

**You are currently on the `data` branch!** This is where all community contributions happen.

### What's Here?

- `drivers.json` - Hardware driver database
- `protocols.json` - Communication protocols reference
- `tools.json` - Diagnostic and management tools

## 🚀 How to Contribute

### Add a New Driver/Protocol/Tool

1. **Fork** the repository
2. **Checkout** this branch: `git checkout data`
3. **Edit** the appropriate JSON file (see schema below)
4. **Validate** your JSON: `python -m json.tool drivers.json > /dev/null`
5. **Commit**: `git commit -m "Add driver: [Name]"`
6. **Push**: `git push origin data`
7. **Create PR** to the `data` branch

### Data Schema

#### Drivers (`drivers.json`)
```json
{
  "name": "Driver Name",
  "description": "What it does",
  "category": "GPU|Network|Audio|Storage|Chipset|Input|Printer|Virtualization|Other",
  "vendor": "Manufacturer",
  "hardware_ids": ["PCI\\VEN_1234&DEV_5678"],
  "installation": {
    "windows": {"command": "winget install ...", "url": "https://..."},
    "linux": {
      "debian": "sudo apt install ...",
      "rhel": "sudo dnf install ...",
      "arch": "sudo pacman -S ...",
      "generic": "build command"
    },
    "macos": {"brew": "brew install ...", "url": "https://..."}
  }
}
```

#### Protocols (`protocols.json`)
```json
{
  "name": "Protocol Name",
  "description": "What it does",
  "type": "Serial|Parallel|Network|Storage",
  "specification_url": "https://...",
  "common_implementations": ["Implementation 1", "Implementation 2"]
}
```

#### Tools (`tools.json`)
```json
{
  "name": "Tool Name",
  "description": "What it does",
  "category": "Diagnostic|Monitoring|Flashing|Benchmark",
  "platform": ["windows", "linux", "macos"],
  "installation": {
    "windows": "winget install ...",
    "linux": "sudo apt install ...",
    "macos": "brew install ..."
  },
  "homepage": "https://..."
}
```

## 📁 Repository Structure

- **`main` branch**: Documentation, scripts, CI/CD workflows
- **`data` branch** (you are here): All JSON data files

## 🔗 Quick Links

- [Main Branch](https://github.com/egoffn1/HexHub/tree/main) - Project homepage
- [Contribution Guide](../CONTRIBUTING.md)
- [Code of Conduct](../CODE_OF_CONDUCT.md)

## ✅ Current Entries

### Drivers (3 entries)
- Realtek RTL8821CE Wi-Fi Driver
- NVIDIA Proprietary GPU Driver
- USBPcap - USB Packet Capture Driver

### Protocols & Tools
Coming soon! Add your own! 🎉

---

*Every contribution makes HexHub better for everyone!* 🧙‍♂️
