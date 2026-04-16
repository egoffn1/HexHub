# HexHub 🧙‍♂️

> **The cross-platform spellbook for hardware**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/egoffn1/HexHub)](https://github.com/egoffn1/HexHub/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/egoffn1/HexHub)](https://github.com/egoffn1/HexHub/issues)
[![GitHub forks](https://img.shields.io/github/forks/egoffn1/HexHub)](https://github.com/egoffn1/HexHub/network/members)
[![Data Branch](https://img.shields.io/badge/data%20branch-ready-green)](https://github.com/egoffn1/HexHub/tree/data)

Centralized database of drivers, protocols, and diagnostic tools with ready-to-paste commands and downloadable archives for Linux, Windows, macOS, and BSD.

---

## 📖 Table of Contents

- [About](#about)
- [Quick Commands Sandbox](#-quick-commands-sandbox)
- [Download Files](#-download-files)
- [Structure](#structure)
- [How to Contribute](#-how-to-contribute)
- [Community Guidelines](#community-guidelines)
- [License](#license)

---

## About

HexHub is not just a database—it's an interactive handbook for system administrators and developers. It provides structured information about hardware (drivers, protocols, utilities) and, most importantly, **ready-to-copy installation commands** grouped by operating systems (Windows, Linux, macOS, BSD).

### Key Features

- 📦 **Downloadable Archives**: Drivers, protocols, and tools packaged as `.zip`, `.tar.gz`, etc.
- 🖥️ **OS-Specific**: Organized by Windows, Linux, macOS, and cross-platform
- 🔍 **Searchable**: Easy to find what you need
- 🤝 **Community-Driven**: Anyone can contribute
- ✅ **Verified**: All submissions are reviewed for safety

---

## 🚀 Quick Commands Sandbox

Select your OS and category to get started:

<details>
<summary><strong>🪟 Windows</strong></summary>

### Drivers
```powershell
# Example: Install Realtek WiFi driver via winget
winget install Realtek.RTL8821CE
```

### Tools
```powershell
# Example: Install Wireshark
winget install Wireshark.Wireshark
```

### Protocols
```powershell
# Example: Enable SMBv3
Enable-WindowsOptionalFeature -Online -FeatureName SMBv3
```

</details>

<details>
<summary><strong>🐧 Linux</strong></summary>

### Drivers
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install realtek-dkms

# RHEL/Fedora
sudo dnf install kmod-rtl8821ce

# Arch Linux
yay -S rtl8821ce-dkms-git
```

### Tools
```bash
# Ubuntu/Debian
sudo apt install wireshark

# RHEL/Fedora
sudo dnf install wireshark

# Arch Linux
sudo pacman -S wireshark-qt
```

### Protocols
```bash
# Enable IPv6
sudo sysctl -w net.ipv6.conf.all.disable_ipv6=0
```

</details>

<details>
<summary><strong>🍎 macOS</strong></summary>

### Drivers
```bash
# Install via Homebrew
brew install --cask realtek-usb-ethernet
```

### Tools
```bash
# Install Wireshark
brew install --cask wireshark
```

### Protocols
```bash
# Enable IPv6
networksetup -setv6automatic Ethernet
```

</details>

<details>
<summary><strong>🌐 All Systems (Cross-Platform)</strong></summary>

### Universal Tools
```bash
# Download and run cross-platform tools
# See the all-systems/tools directory for archives
```

### Protocols
```bash
# Cross-platform protocol implementations
# Check all-systems/protocols for documentation
```

</details>

---

## 📦 Download Files

All downloadable files (drivers, protocols, tools) are stored in the **`data` branch**.

### Browse by OS

| OS | Drivers | Protocols | Tools |
|----|---------|-----------|-------|
| 🪟 Windows | [`windows/drivers/`](https://github.com/egoffn1/HexHub/tree/data/windows/drivers) | [`windows/protocols/`](https://github.com/egoffn1/HexHub/tree/data/windows/protocols) | [`windows/tools/`](https://github.com/egoffn1/HexHub/tree/data/windows/tools) |
| 🐧 Linux | [`linux/drivers/`](https://github.com/egoffn1/HexHub/tree/data/linux/drivers) | [`linux/protocols/`](https://github.com/egoffn1/HexHub/tree/data/linux/protocols) | [`linux/tools/`](https://github.com/egoffn1/HexHub/tree/data/linux/tools) |
| 🍎 macOS | [`macos/drivers/`](https://github.com/egoffn1/HexHub/tree/data/macos/drivers) | [`macos/protocols/`](https://github.com/egoffn1/HexHub/tree/data/macos/protocols) | [`macos/tools/`](https://github.com/egoffn1/HexHub/tree/data/macos/tools) |
| 🌐 All Systems | [`all-systems/drivers/`](https://github.com/egoffn1/HexHub/tree/data/all-systems/drivers) | [`all-systems/protocols/`](https://github.com/egoffn1/HexHub/tree/data/all-systems/protocols) | [`all-systems/tools/`](https://github.com/egoffn1/HexHub/tree/data/all-systems/tools) |

### Download a Specific File

```bash
# Clone only the data branch
git clone --no-checkout https://github.com/egoffn1/HexHub.git
cd HexHub
git sparse-checkout init --cone
git sparse-checkout set data/windows/drivers
git checkout data
```

Or browse directly on GitHub and click to download!

---

## Structure

### Main Branch (`main`)
Documentation, contribution guides, and project metadata.

### Data Branch (`data`)
All downloadable files organized by OS and category:

```
data/
├── windows/
│   ├── drivers/      # .zip, .exe, .msi archives
│   ├── protocols/    # Protocol implementations
│   └── tools/        # Utility tools
├── linux/
│   ├── drivers/
│   ├── protocols/
│   └── tools/
├── macos/
│   ├── drivers/
│   ├── protocols/
│   └── tools/
└── all-systems/
    ├── drivers/
    ├── protocols/
    └── tools/
```

---

## 🤝 How to Contribute

We welcome contributions! Here's how you can help:

### Adding a New File

1. **Fork** the repository
2. **Clone** the data branch:
   ```bash
   git clone --single-branch --branch data https://github.com/YOUR_USERNAME/HexHub.git
   ```
3. **Add your file** to the appropriate directory
4. **Name it properly**: `vendor_product_version.ext`
5. **Submit a Pull Request**

### File Requirements

- ✅ Safe and malware-free
- ✅ Clear naming convention
- ✅ Documentation included
- ✅ Under 100MB
- ✅ Proper licensing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed instructions.

### Report Issues

Found a problem? [Open an issue](https://github.com/egoffn1/HexHub/issues)!

---

## Community Guidelines

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) to keep our community welcoming and inclusive.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
Copyright (c) 2026 HexHub Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">

**Made with ❤️ by the HexHub Community**

[Report Issue](https://github.com/egoffn1/HexHub/issues) • [Request Feature](https://github.com/egoffn1/HexHub/issues) • [Discussions](https://github.com/egoffn1/HexHub/discussions)

</div>
