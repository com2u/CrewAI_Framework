# Device Management App

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Getting Started](#getting-started)
4. [Usage](#usage)
   - [Adding a New Device](#adding-a-new-device)
   - [Viewing Devices](#viewing-devices)
   - [Updating a Device](#updating-a-device)
   - [Deleting a Device](#deleting-a-device)
   - [Sorting Devices](#sorting-devices)
5. [Battery Status Simulation](#battery-status-simulation)
6. [User Interface](#user-interface)
7. [Technical Details](#technical-details)
8. [Troubleshooting](#troubleshooting)

## Introduction

The Device Management App is a web-based application that allows users to manage and monitor various electronic devices. It provides a simple and intuitive interface for adding, updating, and deleting devices, as well as tracking their battery status in real-time.

## Features

- Add new devices with details such as name, type, owner, and battery status
- View all devices in a sortable table format
- Update existing device information
- Delete devices from the list
- Real-time battery status simulation
- Sorting functionality for easy device management
- Responsive design for various screen sizes

## Getting Started

To use the Device Management App, simply open the HTML file in a modern web browser. No additional installation or setup is required.

## Usage

### Adding a New Device

1. Locate the "Add New Device" form at the top of the page.
2. Fill in the required fields:
   - Device Name: Enter a unique name for the device
   - Device Type: Select from the dropdown menu (Smartphone, Tablet, Camera, Laptop, Car, or Powerbank)
   - Owner Name: Enter the name of the device owner
   - Battery Status: Enter a number between 0 and 100 to represent the battery percentage
3. Click the "Add Device" button to add the device to the list

### Viewing Devices

All added devices are displayed in a table below the form. Each row represents a device and shows its name, type (with an icon), owner, battery status, and available actions.

### Updating a Device

1. Find the device you want to update in the table
2. Click the "Update" button in the Actions column
3. The device's information will be populated in the "Add New Device" form
4. Make the necessary changes to the device information
5. Click the "Add Device" button to save the changes

Note: Updating a device will remove it from its current position in the table and add it as a new entry.

### Deleting a Device

1. Locate the device you want to remove in the table
2. Click the "Delete" button in the Actions column
3. The device will be immediately removed from the list

### Sorting Devices

Click on any column header in the table to sort the devices based on that column. Clicking the same header again will reverse the sort order.

## Battery Status Simulation

The app includes a battery status simulation feature:

- Each device's battery status is represented by a colored bar and percentage
- The battery status decreases by 1% every second for all devices with a battery level above 0%
- When a device's battery reaches 0%, it stops decreasing

## User Interface

The app features a clean and responsive user interface:

- The "Add New Device" form is prominently displayed at the top of the page
- Devices are listed in a table format for easy viewing and management
- Each device type is represented by an icon for quick visual identification
- Battery status is displayed as both a colored bar and a percentage
- Action buttons (Update and Delete) are provided for each device

## Technical Details

The Device Management App is built using:

- HTML5 for structure
- CSS3 for styling and responsiveness
- JavaScript for dynamic functionality and real-time updates

Key JavaScript functions:

- `addDevice()`: Handles the addition of new devices
- `updateTable()`: Refreshes the device table display
- `updateDevice()`: Populates the form with a device's data for editing
- `deleteDevice()`: Removes a device from the list
- `sortTable()`: Implements the table sorting functionality
- `updateBatteryStatus()`: Simulates battery drain for all devices

## Troubleshooting

If you encounter any issues while using the Device Management App:

1. Ensure you're using a modern, up-to-date web browser
2. Clear your browser's cache and reload the page
3. Check that all required fields are filled when adding or updating a device
4. Verify that the battery status is a number between 0 and 100

If problems persist, try reopening the HTML file or restarting your browser.