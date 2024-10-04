# Device Management App

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Getting Started](#getting-started)
4. [Usage Guide](#usage-guide)
   - [Adding a Device](#adding-a-device)
   - [Viewing Devices](#viewing-devices)
   - [Updating a Device](#updating-a-device)
   - [Deleting a Device](#deleting-a-device)
   - [Searching Devices](#searching-devices)
   - [Sorting Devices](#sorting-devices)
   - [Exporting Devices](#exporting-devices)
   - [Importing Devices](#importing-devices)
5. [Battery Status](#battery-status)
6. [Dark Mode](#dark-mode)
7. [Responsive Design](#responsive-design)
8. [Local Storage](#local-storage)
9. [Security](#security)
10. [Troubleshooting](#troubleshooting)

## Introduction

The Device Management App is a web-based application that allows users to manage and track various electronic devices. It provides an intuitive interface for adding, updating, and monitoring devices with their respective battery statuses.

## Features

- Add, update, and delete devices
- View devices in a sortable table
- Search functionality for quick device lookup
- Battery status tracking with visual indicators
- Dark mode for comfortable viewing
- Export and import device data
- Responsive design for mobile compatibility
- Local storage for data persistence
- Battery level simulation
- Data visualization with a battery status chart

## Getting Started

To use the Device Management App, simply open the HTML file in a modern web browser. No additional installation or setup is required.

## Usage Guide

### Adding a Device

1. Scroll to the "Add New Device" section.
2. Fill in the required fields:
   - Device Name
   - Device Type (select from the dropdown)
   - Owner Name
   - Battery Status (0-100%)
3. Click the "Add Device" button.

### Viewing Devices

All added devices are displayed in the "Existing Devices" table. Each device entry shows:
- Device Name
- Device Type (with an icon)
- Owner Name
- Battery Status (percentage and visual bar)
- Action buttons (Update and Delete)

### Updating a Device

1. Click the "Update" button next to the device you want to modify.
2. The update form will appear with pre-filled information.
3. Make the necessary changes.
4. Click the "Update Device" button to save changes.

### Deleting a Device

1. Click the "Delete" button next to the device you want to remove.
2. Confirm the deletion when prompted.

### Searching Devices

1. Use the search bar at the top of the device list.
2. Type in your search query (device name, type, or owner).
3. The table will automatically filter to show matching results.

### Sorting Devices

Click on any column header in the device table to sort the list based on that column. Click again to reverse the sort order.

### Exporting Devices

1. Click the "Export Devices" button.
2. A JSON file containing all device data will be downloaded.

### Importing Devices

1. Click the "Import Devices" button.
2. Select a previously exported JSON file.
3. The app will load the imported devices, replacing the current list.

## Battery Status

- Battery status is displayed as a percentage and a colored bar for each device.
- The battery level decreases slowly over time to simulate real-world usage.
- Green indicates a charged battery, while red indicates a low battery.

## Dark Mode

Toggle dark mode by clicking the "Toggle Dark Mode" button in the top-right corner for a more comfortable viewing experience in low-light environments.

## Responsive Design

The app is designed to work on both desktop and mobile devices. On smaller screens, the table layout adjusts for better readability.

## Local Storage

The app uses local storage to save your device data. This means your devices will persist even if you close and reopen the browser.

## Security

Input data is sanitized to prevent XSS attacks. However, as this is a client-side application, sensitive data should not be stored or managed here.

## Troubleshooting

- If devices are not appearing, check if your browser supports local storage and JavaScript.
- Clear your browser cache if you experience any unusual behavior.
- Ensure you're using a modern, up-to-date web browser for the best experience.

---

This Device Management App provides a comprehensive solution for tracking and managing your electronic devices. With its user-friendly interface and powerful features, you can easily keep tabs on all your devices and their battery statuses. Enjoy using the app!