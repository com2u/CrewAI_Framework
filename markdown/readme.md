```markdown
# Device Management App

Welcome to the Device Management App! This application allows you to manage and keep track of various devices, including adding new devices, editing existing ones, and deleting devices. Each device's battery status is visually updated over time, simulating battery drain.

## Features

- Add new devices with details like name, type, owner, and battery status.
- Edit existing devices to update their details.
- Delete devices that are no longer needed.
- Real-time battery status update for each device.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Components](#components)
- [Adding a Device](#adding-a-device)
- [Editing a Device](#editing-a-device)
- [Deleting a Device](#deleting-a-device)
- [Battery Status](#battery-status)

## Installation

No installation is necessary. Simply open the `index.html` file in your web browser to start using the app.

## Usage

- The main interface displays a list of devices.
- You can add a new device using the form in the "Add New Device" section.
- You can edit or delete an existing device using the buttons next to each device listed.

## Components

- **Device List:** Displays all the devices added.
- **Add Device Form:** Form to input new device details.
- **Edit Device Form:** Form to update existing device details.

### HTML Structure

**Device List Section:**
```html
<div class="device-list" id="deviceList"></div>
```

**Add Device Section:**
```html
<div class="add-device">
    <h2>Add New Device</h2>
    <form id="addDeviceForm"> ... </form>
</div>
```

**Edit Device Section:**
```html
<div class="edit-device" style="display:none;">
    <h2>Edit Device</h2>
    <form id="editDeviceForm"> ... </form>
</div>
```

## Adding a Device

1. Fill out the "Add New Device" form with the following information:
    - **Device Name:** Name of the device.
    - **Device Type:** Type of the device (Smartphone, Tablet, Camera).
    - **Owner Name:** Name of the device owner.
    - **Battery Status:** Battery level percentage.
2. Click the `Add Device` button to add the device to the list.

```html
<form id="addDeviceForm">
    <fieldset>
        <legend>Device Information</legend>
        <label for="deviceName">Device Name</label>
        <input type="text" id="deviceName" name="deviceName" required>
        
        <label for="deviceType">Device Type</label>
        <select id="deviceType" name="deviceType" required>
            <option value="Smartphone">Smartphone</option>
            <option value="Tablet">Tablet</option>
            <option value="Camera">Camera</option>
        </select>
        
        <label for="ownerName">Owner Name</label>
        <input type="text" id="ownerName" name="ownerName" required>
        
        <label for="batteryStatus">Battery Status</label>
        <input type="number" id="batteryStatus" name="batteryStatus" min="0" max="100" required>
        
        <button type="submit">Add Device</button>
    </fieldset>
</form>
```

## Editing a Device

1. Click the `Edit` button next to the device you want to modify.
2. The "Edit Device" form will populate with the current device's details.
3. Update the information and click the `Update Device` button.
4. You can cancel the edit by clicking the `Cancel` button.

```html
<form id="editDeviceForm">
    <fieldset>
        <legend>Device Information</legend>
        <label for="editDeviceName">Device Name</label>
        <input type="text" id="editDeviceName" name="deviceName" required>
        
        <label for="editDeviceType">Device Type</label>
        <select id="editDeviceType" name="deviceType" required>
            <option value="Smartphone">Smartphone</option>
            <option value="Tablet">Tablet</option>
            <option value="Camera">Camera</option>
        </select>
        
        <label for="editOwnerName">Owner Name</label>
        <input type="text" id="editOwnerName" name="ownerName" required>
        
        <label for="editBatteryStatus">Battery Status</label>
        <input type="number" id="editBatteryStatus" name="batteryStatus" min="0" max="100" required>
        
        <button type="submit">Update Device</button>
        <button type="button" onclick="cancelEdit()">Cancel</button>
    </fieldset>
</form>
```

## Deleting a Device

1. Click the `Delete` button next to the device you want to remove.
2. The device will be immediately removed from the list.

## Battery Status

- Each device's battery status is automatically reduced by 1% every second, simulating battery drain.
- When the battery status reaches 0%, it stops decreasing.

## Script

The app uses JavaScript to manage device data, handle form submissions, and update the user interface.

```javascript
let devices = [];
let editIndex = -1;

function renderDevices() {
    const deviceList = document.getElementById('deviceList');
    deviceList.innerHTML = '';

    devices.forEach((device, index) => {
        const deviceItem = document.createElement('div');
        deviceItem.className = 'device-item';

        deviceItem.innerHTML = `
            <strong>Device Name:</strong> ${device.deviceName}<br>
            <strong>Device Type:</strong> ${device.deviceType}<br>
            <strong>Owner Name:</strong> ${device.ownerName}<br>
            <strong>Battery Status:</strong> <span id="batteryStatus${index}">${device.batteryStatus}%</span>
            <div class="device-actions">
                <button onclick="editDevice(${index})" class="update">Edit</button>
                <button onclick="deleteDevice(${index})" class="delete">Delete</button>
            </div>
        `;

        deviceList.appendChild(deviceItem);

        // Start draining battery
        if (device.batteryStatus > 0) {
            decreaseBatteryStatus(index);
        }
    });
}

function addDevice(device) {
    devices.push({...device, batteryStatus: Number(device.batteryStatus)});
    renderDevices();
}

function editDevice(index) {
    editIndex = index;
    const device = devices[index];

    document.getElementById('editDeviceName').value = device.deviceName;
    document.getElementById('editDeviceType').value = device.deviceType;
    document.getElementById('editOwnerName').value = device.ownerName;
    document.getElementById('editBatteryStatus').value = device.batteryStatus;

    document.querySelector('.add-device').style.display = 'none';
    document.querySelector('.edit-device').style.display = 'block';
}

function updateDevice(updatedDevice) {
    devices[editIndex] = {...updatedDevice, batteryStatus: Number(updatedDevice.batteryStatus)};
    renderDevices();
    cancelEdit();
}

function deleteDevice(index) {
    devices.splice(index, 1);
    renderDevices();
}

function decreaseBatteryStatus(index) {
    if (devices[index] && devices[index].batteryStatus > 0) {
        setTimeout(() => {
            devices[index].batteryStatus -= 1;
            document.getElementById(`batteryStatus${index}`).innerText = `${devices[index].batteryStatus}%`;
            decreaseBatteryStatus(index);
        }, 1000);
    }
}

function cancelEdit() {
    editIndex = -1;
    document.getElementById('editDeviceForm').reset();
    document.querySelector('.add-device').style.display = 'block';
    document.querySelector('.edit-device').style.display = 'none';
}

document.getElementById('addDeviceForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const newDevice = {
        deviceName: this.deviceName.value,
        deviceType: this.deviceType.value,
        ownerName: this.ownerName.value,
        batteryStatus: this.batteryStatus.value
    };

    addDevice(newDevice);
    this.reset();
});

document.getElementById('editDeviceForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const updatedDevice = {
        deviceName: this.deviceName.value,
        deviceType: this.deviceType.value,
        ownerName: this.ownerName.value,
        batteryStatus: this.batteryStatus.value
    };

    updateDevice(updatedDevice);
});

// Initial render
renderDevices();
```

Enjoy managing your devices with ease! If you have any questions or face issues, feel free to reach out.
```

This `README.md` provides clear and detailed instructions for users on how to use the Device Management App, including adding, editing, and deleting devices, and understanding the real-time battery status feature.