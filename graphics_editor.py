import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import xml.etree.ElementTree as ET
import os
import configparser

# Configuration file to store the folder path
CONFIG_FILE = "config.ini"

# Load or create the configuration file
def load_config():
    config = configparser.ConfigParser()
    if os.path.exists(CONFIG_FILE):
        config.read(CONFIG_FILE)
    else:
        config["DEFAULT"] = {"xml_folder": ""}
    return config

# Save the configuration file
def save_config(config):
    with open(CONFIG_FILE, "w") as configfile:
        config.write(configfile)

# Prompt the user to select the folder containing the XML file
def select_xml_folder():
    folder = filedialog.askdirectory(title="Select Folder Containing Stronghold2.GraphicsSettings.xml")
    if folder:
        return folder
    return None

# Full path to the XML file
def get_xml_file_path(folder):
    return os.path.join(folder, "Stronghold2.GraphicsSettings.xml")

# Load XML file
def load_xml(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"XML file not found at: {file_path}")
    tree = ET.parse(file_path)
    return tree.getroot()

# Save XML file
def save_xml(file_path, root):
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding="utf-8", xml_declaration=True)

# Define presets
PRESETS = {
    "Lowest": {
        "resolution": {"width": "1280", "height": "720", "format": "X8R8G8B8", "refreshRate": "60"},
        "multiSamples": {"value": "0"},
        "Ansiotropy": {"value": "0"},
        "drawDistance": {"value": "0.000000"},
        "nPatchLevel": {"value": "0.000000"},
        "levelOfDetail": {"value": "0.000000"},
        "modelDetail": {"value": "0"},
        "textureDetail": {"value": "3"},
        "drawGroundShadows": {"enabled": "false"},
        "bloomEnabled": {"enabled": "false"},
        "drawRealTimeShadows": {"enabled": "false"},
        "drawReflections": {"enabled": "false"},
        "drawArrowTrails": {"enabled": "false"},
        "drawParticles": {"enabled": "false"},
        "drawGrass": {"enabled": "false"},
        "earlyCulling": {"enabled": "false"},
        "enhancedWater": {"enabled": "false"},
        "normalMaps": {"enabled": "true"},
        "multipassShaders": {"enabled": "false"},
        "settingsDialog": {"enabled": "true"},
        "shaderVersion": {"value": "0.0"},
        "gfxLevel": {"value": "0"},
        "cloudShadow": {"enabled": "false"},
        "particleLevel": {"value": "0"},
        "snow": {"enabled": "false"},
        "waterSetting": {"value": "0"},
        "windowed": {"enabled": "false"},
    },
    "Low": {
        "resolution": {"width": "1280", "height": "720", "format": "X8R8G8B8", "refreshRate": "60"},
        "multiSamples": {"value": "2"},
        "Ansiotropy": {"value": "2"},
        "drawDistance": {"value": "0.500000"},
        "nPatchLevel": {"value": "0.500000"},
        "levelOfDetail": {"value": "0.500000"},
        "modelDetail": {"value": "1"},
        "textureDetail": {"value": "2"},
        "drawGroundShadows": {"enabled": "true"},
        "bloomEnabled": {"enabled": "false"},
        "drawRealTimeShadows": {"enabled": "false"},
        "drawReflections": {"enabled": "false"},
        "drawArrowTrails": {"enabled": "false"},
        "drawParticles": {"enabled": "true"},
        "drawGrass": {"enabled": "false"},
        "earlyCulling": {"enabled": "true"},
        "enhancedWater": {"enabled": "false"},
        "normalMaps": {"enabled": "true"},
        "multipassShaders": {"enabled": "false"},
        "settingsDialog": {"enabled": "true"},
        "shaderVersion": {"value": "1.1"},
        "gfxLevel": {"value": "1"},
        "cloudShadow": {"enabled": "false"},
        "particleLevel": {"value": "1"},
        "snow": {"enabled": "false"},
        "waterSetting": {"value": "1"},
        "windowed": {"enabled": "false"},
    },
    "Medium": {
        "resolution": {"width": "1920", "height": "1080", "format": "X8R8G8B8", "refreshRate": "60"},
        "multiSamples": {"value": "4"},
        "Ansiotropy": {"value": "4"},
        "drawDistance": {"value": "1.000000"},
        "nPatchLevel": {"value": "1.000000"},
        "levelOfDetail": {"value": "1.000000"},
        "modelDetail": {"value": "2"},
        "textureDetail": {"value": "1"},
        "drawGroundShadows": {"enabled": "true"},
        "bloomEnabled": {"enabled": "true"},
        "drawRealTimeShadows": {"enabled": "true"},
        "drawReflections": {"enabled": "false"},
        "drawArrowTrails": {"enabled": "true"},
        "drawParticles": {"enabled": "true"},
        "drawGrass": {"enabled": "true"},
        "earlyCulling": {"enabled": "true"},
        "enhancedWater": {"enabled": "true"},
        "normalMaps": {"enabled": "true"},
        "multipassShaders": {"enabled": "true"},
        "settingsDialog": {"enabled": "true"},
        "shaderVersion": {"value": "2.0"},
        "gfxLevel": {"value": "2"},
        "cloudShadow": {"enabled": "true"},
        "particleLevel": {"value": "2"},
        "snow": {"enabled": "true"},
        "waterSetting": {"value": "2"},
        "windowed": {"enabled": "false"},
    },
    "High": {
        "resolution": {"width": "1920", "height": "1080", "format": "X8R8G8B8", "refreshRate": "60"},
        "multiSamples": {"value": "8"},
        "Ansiotropy": {"value": "8"},
        "drawDistance": {"value": "1.500000"},
        "nPatchLevel": {"value": "1.500000"},
        "levelOfDetail": {"value": "1.500000"},
        "modelDetail": {"value": "3"},
        "textureDetail": {"value": "0"},
        "drawGroundShadows": {"enabled": "true"},
        "bloomEnabled": {"enabled": "true"},
        "drawRealTimeShadows": {"enabled": "true"},
        "drawReflections": {"enabled": "true"},
        "drawArrowTrails": {"enabled": "true"},
        "drawParticles": {"enabled": "true"},
        "drawGrass": {"enabled": "true"},
        "earlyCulling": {"enabled": "true"},
        "enhancedWater": {"enabled": "true"},
        "normalMaps": {"enabled": "true"},
        "multipassShaders": {"enabled": "true"},
        "settingsDialog": {"enabled": "true"},
        "shaderVersion": {"value": "3.0"},
        "gfxLevel": {"value": "3"},
        "cloudShadow": {"enabled": "true"},
        "particleLevel": {"value": "3"},
        "snow": {"enabled": "true"},
        "waterSetting": {"value": "3"},
        "windowed": {"enabled": "false"},
    },
    "Highest": {
        "resolution": {"width": "2560", "height": "1440", "format": "X8R8G8B8", "refreshRate": "60"},
        "multiSamples": {"value": "16"},
        "Ansiotropy": {"value": "16"},
        "drawDistance": {"value": "2.000000"},
        "nPatchLevel": {"value": "2.000000"},
        "levelOfDetail": {"value": "2.000000"},
        "modelDetail": {"value": "4"},
        "textureDetail": {"value": "0"},
        "drawGroundShadows": {"enabled": "true"},
        "bloomEnabled": {"enabled": "true"},
        "drawRealTimeShadows": {"enabled": "true"},
        "drawReflections": {"enabled": "true"},
        "drawArrowTrails": {"enabled": "true"},
        "drawParticles": {"enabled": "true"},
        "drawGrass": {"enabled": "true"},
        "earlyCulling": {"enabled": "true"},
        "enhancedWater": {"enabled": "true"},
        "normalMaps": {"enabled": "true"},
        "multipassShaders": {"enabled": "true"},
        "settingsDialog": {"enabled": "true"},
        "shaderVersion": {"value": "3.0"},
        "gfxLevel": {"value": "4"},
        "cloudShadow": {"enabled": "true"},
        "particleLevel": {"value": "4"},
        "snow": {"enabled": "true"},
        "waterSetting": {"value": "4"},
        "windowed": {"enabled": "false"},
    },
}

# Common resolutions
COMMON_RESOLUTIONS = [
    "1280x720",
    "1366x768",
    "1600x900",
    "1920x1080",
    "2560x1440",
    "3840x2160"
]

# Tooltips for settings
TOOLTIPS = {
    "resolution": "Sets the game's display resolution.",
    "multiSamples": "Controls anti-aliasing for smoother edges.",
    "Ansiotropy": "Improves texture quality at oblique angles.",
    "drawDistance": "Controls how far objects are rendered in the game.",
    "nPatchLevel": "Adjusts the smoothness of curved surfaces.",
    "levelOfDetail": "Controls the level of detail for distant objects.",
    "modelDetail": "Adjusts the complexity of 3D models.",
    "textureDetail": "Adjusts the quality of textures in the game.",
    "drawGroundShadows": "Enables or disables shadows on the ground.",
    "bloomEnabled": "Enables or disables the bloom lighting effect.",
    "drawRealTimeShadows": "Enables or disables real-time shadows.",
    "drawReflections": "Enables or disables reflective surfaces.",
    "drawArrowTrails": "Enables or disables arrow trails.",
    "drawParticles": "Enables or disables particle effects.",
    "drawGrass": "Enables or disables grass rendering.",
    "earlyCulling": "Optimizes rendering by culling unseen objects.",
    "enhancedWater": "Enables or disables enhanced water effects.",
    "normalMaps": "Enables or disables normal mapping for textures.",
    "multipassShaders": "Enables or disables advanced shader effects.",
    "settingsDialog": "Enables or disables the settings dialog in-game.",
    "shaderVersion": "Sets the version of shaders used by the game.",
    "gfxLevel": "Sets the overall graphics quality level.",
    "cloudShadow": "Enables or disables cloud shadows.",
    "particleLevel": "Adjusts the density of particle effects.",
    "snow": "Enables or disables snow effects.",
    "waterSetting": "Adjusts the quality of water rendering.",
    "windowed": "Enables or disables windowed mode.",
}

# Create GUI
class GraphicsSettingsEditor:
    def __init__(self, root, xml_root):
        self.root = root
        self.xml_root = xml_root
        self.entries = {}

        # Calculate the required window height based on the number of settings
        num_settings = len(list(xml_root))
        window_height = 150 + (num_settings * 40)  # Base height + 40px per setting

        # Set up the main window
        self.root.title("Stronghold 2 Graphics Settings Editor")
        self.root.geometry(f"600x{window_height}")  # Dynamic height
        self.root.configure(bg="#f0f0f0")

        # Add a title
        title = ttk.Label(
            self.root,
            text="Graphics Settings",
            font=("Helvetica", 16, "bold"),
            background="#f0f0f0"
        )
        title.pack(pady=10)

        # Create a notebook for tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Create tabs
        self.create_graphics_tab(notebook)

        # Add a label for tooltips that follows the mouse
        self.tooltip_label = ttk.Label(self.root, text="", background="#ffffe0", relief="solid", borderwidth=1)
        self.tooltip_label.place(x=0, y=0)  # Initially place it at (0, 0), but it will be moved dynamically

        # Add action buttons
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)

        confirm_btn = ttk.Button(button_frame, text="Confirm", command=self.save_settings)
        confirm_btn.pack(side="left", padx=5)

        back_btn = ttk.Button(button_frame, text="Back", command=self.root.quit)
        back_btn.pack(side="left", padx=5)

        reset_btn = ttk.Button(button_frame, text="Reset Settings", command=self.reset_settings)
        reset_btn.pack(side="left", padx=5)

    def create_graphics_tab(self, notebook):
        tab = ttk.Frame(notebook)
        notebook.add(tab, text="Graphics & Video")

        # Add preset dropdown
        preset_frame = ttk.Frame(tab)
        preset_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(preset_frame, text="Preset", width=20, anchor="w").pack(side="left", padx=10)
        self.preset_var = tk.StringVar(value="Custom")
        preset_dropdown = ttk.Combobox(
            preset_frame,
            textvariable=self.preset_var,
            values=["Custom", "Lowest", "Low", "Medium", "High", "Highest"],
            state="readonly"
        )
        preset_dropdown.pack(side="right", padx=10)
        preset_dropdown.bind("<<ComboboxSelected>>", self.apply_preset)

        # Add settings from the XML file
        for child in self.xml_root:
            frame = ttk.Frame(tab)
            frame.pack(fill="x", padx=10, pady=5)

            lbl = ttk.Label(frame, text=child.tag, width=20, anchor="w")
            lbl.pack(side="left", padx=10)

            # Bind hover events to show tooltips
            lbl.bind("<Enter>", lambda event, tag=child.tag: self.show_tooltip(event, tag))
            lbl.bind("<Leave>", lambda event: self.hide_tooltip())

            if child.tag == "shaderVersion":
                # Create a dropdown for shaderVersion
                options = ["0.0", "1.1", "1.3", "1.4", "2.0", "3.0"]
                var = tk.StringVar(value=child.attrib["value"])
                dropdown = ttk.Combobox(frame, textvariable=var, values=options, state="readonly")
                dropdown.pack(side="right", padx=10)
                self.entries[child.tag] = var
            elif "enabled" in child.attrib:
                # Create a toggle switch for boolean values
                var = tk.StringVar(value="On" if child.attrib["enabled"].lower() == "true" else "Off")
                switch = ttk.Checkbutton(frame, text=var.get(), variable=var, onvalue="On", offvalue="Off")
                switch.pack(side="right")
                self.entries[child.tag] = var
            elif "value" in child.attrib:
                # Create an entry for numeric/string values
                entry = ttk.Entry(frame)
                entry.insert(0, child.attrib["value"])
                entry.pack(side="right", padx=10)
                self.entries[child.tag] = entry
            elif "width" in child.attrib and "height" in child.attrib:
                # Special case for resolution - dropdown with common resolutions
                resolution_var = tk.StringVar(value=f"{child.attrib['width']}x{child.attrib['height']}")
                resolution_dropdown = ttk.Combobox(frame, textvariable=resolution_var, values=COMMON_RESOLUTIONS, state="readonly")
                resolution_dropdown.pack(side="right", padx=10)
                self.entries["resolution"] = resolution_var

    def show_tooltip(self, event, tag):
        # Update the tooltip text
        self.tooltip_label.config(text=TOOLTIPS.get(tag, "No description available."))
        
        # Calculate the position relative to the window
        x = event.x_root - self.root.winfo_rootx() + 10  # Offset by 10 pixels to the right of the cursor
        y = event.y_root - self.root.winfo_rooty() + 10  # Offset by 10 pixels below the cursor
        
        # Place the tooltip at the calculated position
        self.tooltip_label.place(x=x, y=y)

    def hide_tooltip(self):
        # Hide the tooltip
        self.tooltip_label.place_forget()

    def apply_preset(self, event):
        # This function will be called when a preset is selected
        preset = self.preset_var.get()
        if preset == "Custom":
            return  # Do nothing for "Custom"

        # Apply the selected preset values
        preset_values = PRESETS.get(preset, {})
        for key, value in preset_values.items():
            if key in self.entries:
                if isinstance(value, dict) and "enabled" in value:
                    self.entries[key].set("On" if value["enabled"].lower() == "true" else "Off")
                elif isinstance(value, dict) and "value" in value:
                    if isinstance(self.entries[key], ttk.Entry):
                        self.entries[key].delete(0, tk.END)
                        self.entries[key].insert(0, value["value"])
                    elif isinstance(self.entries[key], tk.StringVar):
                        self.entries[key].set(value["value"])
                elif key == "resolution":
                    resolution_value = f"{value['width']}x{value['height']}"
                    self.entries[key].set(resolution_value)

    def save_settings(self):
        for child in self.xml_root:
            if "enabled" in child.attrib:
                child.attrib["enabled"] = str(self.entries[child.tag].get() == "On").lower()
            elif "value" in child.attrib:
                child.attrib["value"] = self.entries[child.tag].get()
            elif "width" in child.attrib and "height" in child.attrib:
                resolution = self.entries["resolution"].get()
                width, height = resolution.split("x")
                child.attrib["width"] = width
                child.attrib["height"] = height
        save_xml(XML_FILE_PATH, self.xml_root)
        print(f"Settings saved to {XML_FILE_PATH}!")

    def reset_settings(self):
        # Reset settings to default (you can implement this as needed)
        print("Settings reset to default.")

# Main application
if __name__ == "__main__":
    try:
        # Load configuration
        config = load_config()
        xml_folder = config["DEFAULT"].get("xml_folder", "")

        # If no folder is set, prompt the user to select one
        if not xml_folder:
            xml_folder = select_xml_folder()
            if not xml_folder:
                messagebox.showerror("Error", "No folder selected. Exiting.")
                exit()
            config["DEFAULT"]["xml_folder"] = xml_folder
            save_config(config)

        # Get the full path to the XML file
        XML_FILE_PATH = get_xml_file_path(xml_folder)

        # Load XML
        xml_root = load_xml(XML_FILE_PATH)

        # Create Tkinter window
        root = tk.Tk()

        # Apply a modern theme
        style = ttk.Style(root)
        style.theme_use("clam")  # You can try "alt", "default", or "vista" for other themes

        # Create and run the editor
        editor = GraphicsSettingsEditor(root, xml_root)
        root.mainloop()
    except FileNotFoundError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")