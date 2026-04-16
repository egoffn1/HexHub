# HexHub

<div align="center">

![HexHub Logo](https://img.shields.io/badge/HexHub-Hardware%20Spellbook-blue?style=for-the-badge&logo=github)

### 🧙 The Cross-Platform Spellbook for Hardware

**Centralized database of drivers, protocols, and diagnostic tools with ready-to-paste commands for Linux, Windows, and macOS.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/egoffn1/HexHub?style=social)](https://github.com/egoffn1/HexHub/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/egoffn1/HexHub?style=social)](https://github.com/egoffn1/HexHub/network/members)
[![GitHub issues](https://img.shields.io/github/issues/egoffn1/HexHub)](https://github.com/egoffn1/HexHub/issues)

</div>

---

## 📦 Data Branch

**All data files are stored in the [`data`](https://github.com/egoffn1/HexHub/tree/data) branch!** This keeps the main branch clean and allows community contributions without affecting the core project structure.

### How to Contribute

1. **Fork** the repository
2. **Checkout** the `data` branch: `git checkout data`
3. **Add** your driver/protocol/tool to the appropriate JSON file
4. **Submit** a Pull Request to the `data` branch

👉 [View Data Files](https://github.com/egoffn1/HexHub/tree/data) | [Contribution Guide](CONTRIBUTING.md)

---

## 📖 About HexHub

HexHub is not just a database—it's an **interactive reference** for system administrators and developers. It provides structured information about hardware (drivers, protocols, utilities) and, most importantly, **ready-to-copy installation commands** grouped by operating system (Windows, Linux, macOS, BSD).

### ✨ Features

- 🚀 **One-Click Commands**: Copy-paste installation commands for any OS
- 📊 **Structured Data**: JSON-based database easy to extend and automate
- 🔍 **Hardware ID Search**: Find drivers by PCI, USB, and other hardware IDs
- 🌐 **Cross-Platform**: Support for Windows, Linux (Debian/RHEL/Arch), and macOS
- 🤖 **Auto-Generated Docs**: README updates automatically via CI/CD
- 📦 **Extensible**: Easy to add new drivers, protocols, and tools

---

## 📦 Database Contents

<!-- BEGIN_DRIVERS_TABLE -->
| Name | Category | Vendor | Hardware IDs |
|------|----------|--------|---------------|
| Realtek RTL8821CE Wi-Fi Driver | Network | Realtek | `PCI\VEN_10EC&DEV_C821, PCI\VEN_10EC&DEV_C822` |
| NVIDIA Proprietary GPU Driver | GPU | NVIDIA | `PCI\VEN_10DE&DEV_1B80, PCI\VEN_10DE&DEV_1B81, P...` |
| USBPcap - USB Packet Capture Driver | Virtualization | Open Source | `USB\VID_0000&PID_0000` |

<!-- END_DRIVERS_TABLE -->

---

## 🚀 Quick Commands Sandbox

<!-- BEGIN_QUICK_COMMANDS -->
### 🚀 Quick Commands Sandbox

> **Tip:** Select your OS and copy the command directly!

#### GPU

**NVIDIA Proprietary GPU Driver**

🪟 **Windows:** ` winget install Nvidia.GeForceNow --source winget `

🐧 **Debian/Ubuntu:** ` sudo ubuntu-drivers autoinstall || sudo apt install nvidia-driver-535 `

📦 **Arch:** ` sudo pacman -S nvidia nvidia-utils nvidia-settings `

🍎 **macOS:** ` echo 'NVIDIA drivers not supported on modern macOS (Metal API only)' `

---

#### Network

**Realtek RTL8821CE Wi-Fi Driver**

🪟 **Windows:** ` winget install Realtek.RTL8821CE --source winget `

🐧 **Debian/Ubuntu:** ` sudo add-apt-repository ppa:kelebek333/rtl8821ce && sudo apt update && sudo apt install rtl8821ce-dkms `

📦 **Arch:** ` yay -S rtl8821ce-dkms-git `

---

#### Virtualization

**USBPcap - USB Packet Capture Driver**

🪟 **Windows:** ` winget install DESKTOPNW.USBPcap --source winget `

🐧 **Debian/Ubuntu:** ` sudo apt install wireshark usbmon && sudo modprobe usbmon `

📦 **Arch:** ` sudo pacman -S wireshark-qt && sudo modprobe usbmon `

🍎 **macOS:** ` brew install wireshark `

---


<!-- END_QUICK_COMMANDS -->

---

## 💻 Installation Commands Reference

<!-- BEGIN_INSTALLATION_DETAILS -->
<details>
<summary><strong>🪟 Windows Installation Commands</strong></summary>

| Driver | Command | Download |
|--------|---------|----------|
| Realtek RTL8821CE Wi-Fi Driver | `winget install Realtek.RTL8821CE --source winget` | [Download](https://www.realtek.com/en/component/zoo/category/network-interface-controllers-10-100-1000m-pci-express) |
| NVIDIA Proprietary GPU Driver | `winget install Nvidia.GeForceNow --source winget` | [Download](https://www.nvidia.com/Download/index.aspx) |
| USBPcap - USB Packet Capture Driver | `winget install DESKTOPNW.USBPcap --source winget` | [Download](https://desowin.github.io/usbpcap/) |

</details>

<details>
<summary><strong>🐧 Linux Installation Commands</strong></summary>

### Realtek RTL8821CE Wi-Fi Driver

**Debian/Ubuntu:**
```bash
sudo add-apt-repository ppa:kelebek333/rtl8821ce && sudo apt update && sudo apt install rtl8821ce-dkms
```

**RHEL/CentOS/Fedora:**
```bash
sudo dnf install kernel-devel kernel-headers gcc make git && git clone https://github.com/tomaspinho/rtl8821ce.git && cd rtl8821ce && sudo ./dkms-install.sh
```

**Arch/Manjaro:**
```bash
yay -S rtl8821ce-dkms-git
```

**Generic:**
```bash
git clone https://github.com/tomaspinho/rtl8821ce.git && cd rtl8821ce && sudo ./dkms-install.sh
```

### NVIDIA Proprietary GPU Driver

**Debian/Ubuntu:**
```bash
sudo ubuntu-drivers autoinstall || sudo apt install nvidia-driver-535
```

**RHEL/CentOS/Fedora:**
```bash
sudo dnf install epel-release && sudo dnf config-manager --add-repo=https://download.nvidia.com/XFree86/Linux-x86_64 && sudo dnf install nvidia-driver
```

**Arch/Manjaro:**
```bash
sudo pacman -S nvidia nvidia-utils nvidia-settings
```

**Generic:**
```bash
wget https://download.nvidia.com/XFree86/Linux-x86_64/535.104.05/NVIDIA-Linux-x86_64-535.104.05.run && chmod +x NVIDIA-Linux-x86_64-535.104.05.run && sudo ./NVIDIA-Linux-x86_64-535.104.05.run
```

### USBPcap - USB Packet Capture Driver

**Debian/Ubuntu:**
```bash
sudo apt install wireshark usbmon && sudo modprobe usbmon
```

**RHEL/CentOS/Fedora:**
```bash
sudo dnf install wireshark && sudo modprobe usbmon
```

**Arch/Manjaro:**
```bash
sudo pacman -S wireshark-qt && sudo modprobe usbmon
```

**Generic:**
```bash
sudo modprobe usbmon && ls /sys/kernel/debug/usbmon
```

</details>

<details>
<summary><strong>🍎 macOS Installation Commands</strong></summary>

| Driver | Homebrew | Download |
|--------|----------|----------|
| Realtek RTL8821CE Wi-Fi Driver | `echo 'Not available via Homebrew'` | [Download](https://github.com/christianrondeau/RTL8821CU-macOS-Driver) |
| NVIDIA Proprietary GPU Driver | `echo 'NVIDIA drivers not supported on modern macOS (Metal API only)'` | [Download](https://www.nvidia.com/object/mac-driver-archive.html) |
| USBPcap - USB Packet Capture Driver | `brew install wireshark` | [Download](https://github.com/drecc/USBBugle) |

</details>


<!-- END_INSTALLATION_DETAILS -->

---

## 🗂️ Project Structure

```
HexHub/
├── README.md                 # This file (auto-generated sections)
├── LICENSE                   # MIT License
├── CONTRIBUTING.md           # Contribution guidelines
├── CODE_OF_CONDUCT.md        # Code of conduct
├── .gitignore                # Git ignore rules
├── data/                     # Database files
│   ├── drivers.json          # Driver entries
│   ├── protocols.json        # Protocol specifications
│   └── tools.json            # Diagnostic tools
├── scripts/                  # Automation scripts
│   └── generate_readme.py    # README generator
├── docs/                     # GitHub Pages documentation
└── .github/                  # GitHub templates & workflows
    ├── ISSUE_TEMPLATE/       # Issue templates
    ├── PULL_REQUEST_TEMPLATE.md
    └── workflows/            # GitHub Actions CI/CD
```

---

## 🛠️ Usage

### For End Users

1. Browse the [Quick Commands Sandbox](#-quick-commands-sandbox) section above
2. Find your OS and hardware category
3. Copy the command and paste it into your terminal

### For Developers

```bash
# Clone the repository
git clone https://github.com/egoffn1/HexHub.git
cd HexHub

# Run the README generator
python scripts/generate_readme.py

# Validate JSON data
python -m json.tool data/drivers.json > /dev/null && echo "Valid JSON"
```

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### How to Add a New Driver

1. Fork the repository
2. Edit `data/drivers.json` following the schema in `data/drivers_schema.json`
3. Run `python scripts/generate_readme.py` to update the README
4. Commit and create a Pull Request

**Example entry:**
```json
{
  "name": "Your Driver Name",
  "description": "Brief description",
  "category": "Network",
  "vendor": "Vendor Name",
  "hardware_ids": ["PCI\\VEN_XXXX&DEV_XXXX"],
  "installation": {
    "windows": {
      "command": "winget install ...",
      "url": "https://..."
    },
    "linux": {
      "debian": "sudo apt install ...",
      "rhel": "sudo dnf install ...",
      "arch": "sudo pacman -S ..."
    },
    "macos": {
      "brew": "brew install ...",
      "url": "https://..."
    }
  }
}
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🔗 Related Projects

- [Linux Hardware Database](https://github.com/linuxhw)
- [PCI ID Repository](http://pci-ids.ucw.cz/)
- [USB ID Repository](http://www.linux-usb.org/usb.ids)

---

<div align="center">

**Made with ❤️ by the HexHub Contributors**

[Report a Bug](https://github.com/egoffn1/HexHub/issues) · [Request a Feature](https://github.com/egoffn1/HexHub/issues) · [View Discussions](https://github.com/egoffn1/HexHub/discussions)

</div>
