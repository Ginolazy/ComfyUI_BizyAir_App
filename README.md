# ComfyUI BizyAir_WebApp

A standalone ComfyUI node for running BizyAir Web Apps.

![](images/01.webp)
## Installation

1. Clone this repository into your `ComfyUI/custom_nodes` folder:
    ```bash
    git clone https://github.com/Ginolazy/ComfyUI_BizyAir_App.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

 **Note:** Before use, please install the official Bizyair plugin (https://github.com/siliconflow/BizyAir). BizyAir_WebApp will automatically sync the API key from the official Bizyair plugin.

## Usage
- Add the `BizyAir WebApp` node to your workflow.

![](images/02.webp)

- **Add App ID**: 
- Go to https://bizyair.cn/community?path=app to get the app ID you want to use (the 6-digit number at the end of the URL).
    - Method 1: Right-click on the node -> Properties Panel -> Edit `webApp_list`, entering IDs separated by commas.
    - Method 2: Create a `default_apps.json` in the plugin directory to pre-load apps.

![](images/03.webp)

## Features
- Incremental App List Sync
- Dynamic Widget Generation
- Support for Image, Video, and Audio inputs/outputs

![](images/04.webp)

