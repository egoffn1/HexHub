---
name: ➕ Add New Driver
about: Submit a new driver entry to the database
title: '[DRIVER] '
labels: new-driver
assignees: ''

---

**Driver Information**

- **Name:** 
- **Description:** 
- **Category:** [GPU/Network/Audio/Storage/Chipset/Input/Printer/Virtualization/Other]
- **Vendor:** 

**Hardware IDs**
```
PCI\VEN_XXXX&DEV_XXXX
USB\VID_XXXX&PID_XXXX
```

**Installation Commands**

- [ ] Windows command tested
- [ ] Linux (Debian) command tested
- [ ] Linux (RHEL) command tested
- [ ] Linux (Arch) command tested
- [ ] macOS command tested

**Windows**
```
Command: 
URL: 
```

**Linux - Debian/Ubuntu**
```
Command: 
```

**Linux - RHEL/CentOS/Fedora**
```
Command: 
```

**Linux - Arch/Manjaro**
```
Command: 
```

**macOS**
```
Homebrew: 
URL: 
```

**Sources/References**
- [ ] Official vendor documentation linked
- [ ] Community sources verified

**Additional Context**
Add any other information about the driver here.

---

**Checklist**
- [ ] I have followed the JSON schema in `data/drivers_schema.json`
- [ ] I have run `python scripts/generate_readme.py` to update the README
- [ ] I have validated the JSON with `python -m json.tool data/drivers.json`
- [ ] Installation commands have been tested (if possible)
