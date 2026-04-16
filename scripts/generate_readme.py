#!/usr/bin/env python3
"""
HexHub README Generator

This script reads JSON data files from the /data directory and generates
Markdown content for the README.md file. It updates specific sections
marked with HTML comments.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any


def load_json_file(filepath: str) -> Dict[str, Any]:
    """Load and parse a JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_drivers_table(drivers: List[Dict[str, Any]]) -> str:
    """Generate a Markdown table for drivers."""
    if not drivers:
        return "No drivers available."
    
    table = "| Name | Category | Vendor | Hardware IDs |\n"
    table += "|------|----------|--------|---------------|\n"
    
    for driver in drivers:
        name = driver.get('name', 'Unknown')
        category = driver.get('category', 'Other')
        vendor = driver.get('vendor', 'Unknown')
        hw_ids = ', '.join(driver.get('hardware_ids', []))
        
        # Truncate hardware IDs if too long
        if len(hw_ids) > 50:
            hw_ids = hw_ids[:47] + "..."
        
        table += f"| {name} | {category} | {vendor} | `{hw_ids}` |\n"
    
    return table


def generate_installation_details(drivers: List[Dict[str, Any]]) -> str:
    """Generate collapsible details sections for installation commands."""
    html = ""
    
    # Group by OS
    windows_drivers = []
    linux_drivers = []
    macos_drivers = []
    
    for driver in drivers:
        installation = driver.get('installation', {})
        if 'windows' in installation:
            windows_drivers.append(driver)
        if 'linux' in installation:
            linux_drivers.append(driver)
        if 'macos' in installation:
            macos_drivers.append(driver)
    
    # Windows Section
    html += "<details>\n"
    html += "<summary><strong>🪟 Windows Installation Commands</strong></summary>\n\n"
    html += "| Driver | Command | Download |\n"
    html += "|--------|---------|----------|\n"
    
    for driver in windows_drivers:
        name = driver.get('name', 'Unknown')
        win_install = driver['installation'].get('windows', {})
        command = win_install.get('command', 'N/A')
        url = win_install.get('url', '#')
        
        html += f"| {name} | `{command}` | [Download]({url}) |\n"
    
    html += "\n</details>\n\n"
    
    # Linux Section
    html += "<details>\n"
    html += "<summary><strong>🐧 Linux Installation Commands</strong></summary>\n\n"
    
    for driver in linux_drivers:
        name = driver.get('name', 'Unknown')
        linux_install = driver['installation'].get('linux', {})
        
        html += f"### {name}\n\n"
        
        if 'debian' in linux_install:
            html += f"**Debian/Ubuntu:**\n```bash\n{linux_install['debian']}\n```\n\n"
        if 'rhel' in linux_install:
            html += f"**RHEL/CentOS/Fedora:**\n```bash\n{linux_install['rhel']}\n```\n\n"
        if 'arch' in linux_install:
            html += f"**Arch/Manjaro:**\n```bash\n{linux_install['arch']}\n```\n\n"
        if 'generic' in linux_install:
            html += f"**Generic:**\n```bash\n{linux_install['generic']}\n```\n\n"
    
    html += "</details>\n\n"
    
    # macOS Section
    html += "<details>\n"
    html += "<summary><strong>🍎 macOS Installation Commands</strong></summary>\n\n"
    html += "| Driver | Homebrew | Download |\n"
    html += "|--------|----------|----------|\n"
    
    for driver in macos_drivers:
        name = driver.get('name', 'Unknown')
        mac_install = driver['installation'].get('macos', {})
        brew = mac_install.get('brew', 'N/A')
        url = mac_install.get('url', '#')
        
        html += f"| {name} | `{brew}` | [Download]({url}) |\n"
    
    html += "\n</details>\n\n"
    
    return html


def generate_quick_commands_section(drivers: List[Dict[str, Any]]) -> str:
    """Generate the Quick Commands Sandbox section."""
    html = "### 🚀 Quick Commands Sandbox\n\n"
    html += "> **Tip:** Select your OS and copy the command directly!\n\n"
    
    categories = {}
    for driver in drivers:
        cat = driver.get('category', 'Other')
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(driver)
    
    for category, cat_drivers in sorted(categories.items()):
        html += f"#### {category}\n\n"
        for driver in cat_drivers:
            name = driver.get('name', 'Unknown')
            installation = driver.get('installation', {})
            
            html += f"**{name}**\n\n"
            
            if 'windows' in installation and installation['windows'].get('command'):
                cmd = installation['windows']['command']
                html += f"🪟 **Windows:** ` {cmd} `\n\n"
            
            if 'linux' in installation:
                linux = installation['linux']
                if linux.get('debian'):
                    html += f"🐧 **Debian/Ubuntu:** ` {linux['debian']} `\n\n"
                if linux.get('arch'):
                    html += f"📦 **Arch:** ` {linux['arch']} `\n\n"
            
            if 'macos' in installation and installation['macos'].get('brew'):
                brew_cmd = installation['macos']['brew']
                if 'Not available' not in brew_cmd:
                    html += f"🍎 **macOS:** ` {brew_cmd} `\n\n"
            
            html += "---\n\n"
    
    return html


def update_readme(readme_path: str, start_marker: str, end_marker: str, new_content: str) -> bool:
    """Update content between markers in README file."""
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        start_idx = content.find(start_marker)
        end_idx = content.find(end_marker)
        
        if start_idx == -1 or end_idx == -1:
            print(f"Warning: Markers not found in {readme_path}")
            return False
        
        # Include the markers in the replacement
        start_idx += len(start_marker)
        
        updated_content = content[:start_idx] + "\n" + new_content + "\n" + content[end_idx:]
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        return True
    except Exception as e:
        print(f"Error updating README: {e}")
        return False


def main():
    """Main function to generate README content."""
    # Define paths
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent
    data_dir = root_dir / 'data'
    readme_path = root_dir / 'README.md'
    
    print("🔍 Loading data files...")
    
    # Load drivers
    drivers_file = data_dir / 'drivers.json'
    if drivers_file.exists():
        drivers_data = load_json_file(str(drivers_file))
        drivers = drivers_data.get('drivers', [])
        print(f"✅ Loaded {len(drivers)} drivers")
    else:
        drivers = []
        print("⚠️  drivers.json not found")
    
    # Generate content
    print("📝 Generating content...")
    
    drivers_table = generate_drivers_table(drivers)
    installation_details = generate_installation_details(drivers)
    quick_commands = generate_quick_commands_section(drivers)
    
    # Update README
    print("🔄 Updating README.md...")
    
    success = True
    success &= update_readme(
        str(readme_path),
        "<!-- BEGIN_DRIVERS_TABLE -->",
        "<!-- END_DRIVERS_TABLE -->",
        drivers_table
    )
    
    success &= update_readme(
        str(readme_path),
        "<!-- BEGIN_INSTALLATION_DETAILS -->",
        "<!-- END_INSTALLATION_DETAILS -->",
        installation_details
    )
    
    success &= update_readme(
        str(readme_path),
        "<!-- BEGIN_QUICK_COMMANDS -->",
        "<!-- END_QUICK_COMMANDS -->",
        quick_commands
    )
    
    if success:
        print("✅ README.md updated successfully!")
    else:
        print("❌ Some updates failed. Check that markers exist in README.md")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
