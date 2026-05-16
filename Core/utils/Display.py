import shutil
from scapy.all import get_if_addr, conf


def display_network_results(active_ips, local_ip=None, subnet_mask=None):
    """Display network scan results in a formatted box"""
    
    width = shutil.get_terminal_size().columns
    
    # Get the same box width as the description box from Banner.py
    description = "GhostARP is a Layer 2 packet manipulation and network discovery tool focused on ARP behavior, Ethernet communication, and local network experimentation."
    max_text_width = min(width - 8, 100)
    
    # Calculate box width (same logic as Banner.py)
    words = description.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + len(current_line) <= max_text_width:
            current_line.append(word)
            current_length += len(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_length = len(word)
    
    if current_line:
        lines.append(" ".join(current_line))
    
    box_width = max(len(line) for line in lines) + 4
    
    # Prepare local IP info
    if local_ip is None:
        local_ip = get_if_addr(conf.iface)
    
    # Build header lines
    content_lines = [
        f"Local IP: {local_ip}",
        f"Subnet Mask: /{subnet_mask}" if subnet_mask else "",
        f"Active Hosts: {len(active_ips)}",
    ]
    
    # Parse devices to find max widths for alignment
    devices = []
    for device_info in active_ips:
        parts = device_info.split(',')
        if len(parts) == 3:
            ip, mac, vendor = parts
            devices.append((ip, mac, vendor))
    
    # Calculate column widths
    max_ip_len = max(len(d[0]) for d in devices) if devices else 15
    max_mac_len = max(len(d[1]) for d in devices) if devices else 17
    
    # Add device list with aligned columns
    for i, (ip, mac, vendor) in enumerate(devices, 1):
        # Format with fixed spacing between columns
        line = f"{i})  {ip:<{max_ip_len}}    {mac:<{max_mac_len}}    {vendor}"
        
        # Truncate if too long to fit in box
        max_line_length = box_width - 4
        if len(line) > max_line_length:
            line = line[:max_line_length - 3] + "..."
        
        content_lines.append(line)
    
    # Print the box (left-aligned)
    print("┌" + "─" * (box_width - 2) + "┐")
    
    for line in content_lines:
        if line:  # Skip empty lines
            padding = box_width - len(line) - 4
            print("│ " + line + " " * padding + " │")
    
    print("└" + "─" * (box_width - 2) + "┘")
    print()


def display_interfaces(availInterface):
    """Display available network interfaces in a formatted box"""
    
    width = shutil.get_terminal_size().columns
    
    # Get the same box width as the description box
    description = "GhostARP is a Layer 2 packet manipulation and network discovery tool focused on ARP behavior, Ethernet communication, and local network experimentation."
    max_text_width = min(width - 8, 100)
    
    # Calculate box width (same logic as Banner.py)
    words = description.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + len(current_line) <= max_text_width:
            current_line.append(word)
            current_length += len(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_length = len(word)
    
    if current_line:
        lines.append(" ".join(current_line))
    
    box_width = max(len(line) for line in lines) + 4
    
    # Build content lines
    content_lines = []
    
    # Add instruction line
    instruction = f"Available network interfaces (0-{len(availInterface)})"
    if len(instruction) > box_width - 4:
        instruction = instruction[:box_width - 7] + "..."
    content_lines.append(instruction)
    
    # Build single line with all interfaces
    interface_parts = [f"{i}) {interface}" for i, interface in enumerate(availInterface, 1)]
    single_line = "    ".join(interface_parts)
    
    # Truncate if too long to fit in box
    max_line_length = box_width - 4
    if len(single_line) > max_line_length:
        single_line = single_line[:max_line_length - 3] + "..."
    
    content_lines.append(single_line)
    
    # Print the box with "Network Interfaces" heading (left-aligned)
    title = " Network Interfaces "
    title_pos = (box_width - len(title)) // 2
    top_border = "┌" + "─" * (title_pos - 1) + title + "─" * (box_width - title_pos - len(title) - 1) + "┐"
    
    print(top_border)
    
    for line in content_lines:
        padding = box_width - len(line) - 4
        print("│ " + line + " " * padding + " │")
    
    print("└" + "─" * (box_width - 2) + "┘")
    print()

