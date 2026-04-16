# HexHub Data Repository

This branch contains all the downloadable files (drivers, protocols, tools) for HexHub.

## Structure

```
├── windows/          # Files for Windows OS
│   ├── drivers/      # Driver packages (.zip, .exe, .msi)
│   ├── protocols/    # Protocol implementations
│   └── tools/        # Utility tools
├── linux/            # Files for Linux distributions
│   ├── drivers/
│   ├── protocols/
│   └── tools/
├── macos/            # Files for macOS
│   ├── drivers/
│   ├── protocols/
│   └── tools/
└── all-systems/      # Cross-platform files
    ├── drivers/
    ├── protocols/
    └── tools/
```

## How to Contribute

### Adding a New File

1. **Choose the correct directory** based on your target OS:
   - `windows/` - Windows-specific files
   - `linux/` - Linux-specific files
   - `macos/` - macOS-specific files
   - `all-systems/` - Cross-platform files

2. **Prepare your archive**:
   - Package your file as `.zip` (preferred), `.tar.gz`, or other common archive format
   - Include a README inside the archive with installation instructions
   - Ensure no malicious content

3. **Name your file properly**:
   ```
   {vendor}_{product}_{version}.{ext}
   ```
   Examples:
   - `realtek_rtl8821ce_v5.2.5.zip`
   - `nvidia_driver_535.104.tar.gz`
   - `wireshark_usbpcap_1.5.3.msi`

4. **Submit a Pull Request**:
   - Fork this repository
   - Add your file to the appropriate directory
   - Create a PR with description including:
     - Device/Protocol name
     - Vendor
     - Version
     - Compatible hardware IDs (for drivers)
     - Installation instructions

### File Requirements

- ✅ Must be safe and malware-free
- ✅ Should include documentation
- ✅ Preferably open-source or freely distributable
- ✅ Maximum file size: 100MB (use releases for larger files)
- ✅ Clear naming convention

### Example Submission

```bash
# Directory structure for a Realtek WiFi driver
windows/drivers/realtek_rtl8821ce_v5.2.5.zip
linux/drivers/realtek_rtl8821ce_v5.2.5.tar.gz
```

## Verification

All submissions are reviewed before merging. We check:
- File integrity
- Correct categorization
- Proper documentation
- License compatibility

## Download Files

To download a specific file:

```bash
# Using git sparse-checkout (recommended for large repos)
git clone --no-checkout https://github.com/egoffn1/HexHub.git
cd HexHub
git sparse-checkout init --cone
git sparse-checkout set data/windows/drivers
git checkout data
```

Or browse files directly on GitHub and click to download.

## License

All files in this repository are subject to their respective licenses.
Check individual archives for license information.

HexHub project is under MIT License.
