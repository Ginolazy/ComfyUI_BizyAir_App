from .py.bizyair_webapp import BizyAirWebApp

__version__ = "1.0.0"

NODE_CLASS_MAPPINGS = {
    "BizyAirWebApp": BizyAirWebApp
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BizyAirWebApp": "☁️BizyAir WebApp"
}

WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
