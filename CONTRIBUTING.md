# Contributing to HexHub Data Repository

Thank you for contributing to HexHub! This guide will help you submit drivers, protocols, and tools.

## Quick Start

1. **Fork** the repository
2. **Clone** your fork:
   ```bash
   git clone --single-branch --branch data https://github.com/YOUR_USERNAME/HexHub.git
   cd HexHub
   ```

3. **Add your file** to the appropriate directory:
   ```
   windows/drivers/     - Windows drivers
   linux/drivers/       - Linux drivers
   macos/drivers/       - macOS drivers
   all-systems/drivers/ - Cross-platform drivers
   
   windows/protocols/   - Windows protocols
   linux/protocols/     - Linux protocols
   macos/protocols/     - macOS protocols
   all-systems/protocols/ - Cross-platform protocols
   
   windows/tools/       - Windows tools
   linux/tools/         - Linux tools
   macos/tools/         - macOS tools
   all-systems/tools/   - Cross-platform tools
   ```

4. **Name your file** following the convention:
   ```
   {vendor}_{product}_{version}.{ext}
   ```
   Examples:
   - `realtek_rtl8821ce_v5.2.5.zip`
   - `nvidia_driver_535.104.tar.gz`
   - `wireshark_usbpcap_1.5.3.msi`

5. **Commit and push**:
   ```bash
   git add windows/drivers/realtek_rtl8821ce_v5.2.5.zip
   git commit -m "Add Realtek RTL8821CE driver v5.2.5 for Windows"
   git push origin data
   ```

6. **Create a Pull Request** on GitHub

## File Requirements

### ✅ Must Have
- Safe, malware-free content
- Clear naming convention
- Documentation inside the archive (README.txt or similar)
- Proper licensing (open-source or freely distributable)

### 📦 Supported Formats
- `.zip` (preferred)
- `.tar.gz` / `.tgz`
- `.7z`
- `.exe` (Windows only)
- `.msi` (Windows only)
- `.gz`, `.bz2`, `.xz`

### ⚠️ Restrictions
- Maximum file size: 100MB per file
- No proprietary binaries without distribution rights
- No cracked/pirated software
- No malicious content

## Archive Contents

Each archive should include:

```
archive.zip
├── README.txt          # Installation instructions
├── LICENSE             # License file
├── driver.sys          # Driver files
└── setup.exe           # Installer (optional)
```

### README.txt Template

```
=== [Product Name] ===
Vendor: [Company Name]
Version: [X.Y.Z]
Date: [YYYY-MM-DD]

== System Requirements ==
- OS: Windows 10/11, Linux kernel 5.x, etc.
- Architecture: x64, arm64, etc.

== Installation ==
1. Extract the archive
2. Run setup.exe (Windows) or install.sh (Linux)
3. Reboot if required

== Hardware Compatibility ==
- Device Model A (ID: XXXX:YYYY)
- Device Model B (ID: XXXX:ZZZZ)

== License ==
[License information]

== Support ==
Website: https://...
Issues: https://github.com/egoffn1/HexHub/issues
```

## Pull Request Checklist

Before submitting your PR:

- [ ] File is in the correct directory
- [ ] Filename follows convention: `vendor_product_version.ext`
- [ ] Archive includes README with installation instructions
- [ ] File is under 100MB
- [ ] I have rights to distribute this file
- [ ] No malware or suspicious content
- [ ] Commit message is descriptive

## Review Process

1. **Automated Checks**: GitHub Actions validates file structure and naming
2. **Manual Review**: Maintainers check:
   - File safety (virus scan)
   - Licensing compliance
   - Documentation quality
   - Correct categorization

3. **Merge**: Approved PRs are merged to the `data` branch

## Reporting Issues

Found a problem with a file? Open an issue with:
- File name and location
- Problem description
- Expected behavior
- Screenshots/logs if applicable

## Questions?

- Check existing issues
- Read the main README.md
- Contact maintainers via GitHub Discussions

Thank you for making HexHub better! 🎉
