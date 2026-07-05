"""
NexusUB - Plugin System
========================
Dynamic plugin loader that auto-discovers and registers commands.
"""

import os
import importlib
import traceback
from typing import Dict, List, Any

CMD_LIST: Dict[str, List[Dict[str, Any]]] = {}


def register_command(category: str, name: str, help_text: str, aliases: List[str] = None):
    """Add a command to the global registry."""
    if category not in CMD_LIST:
        CMD_LIST[category] = []
    CMD_LIST[category].append({
        "name": name,
        "aliases": aliases or [],
        "help": help_text,
    })


def load_plugins(app):
    """Scan the plugins/ directory and register all commands."""
    plugins_dir = os.path.dirname(os.path.abspath(__file__))
    loaded = 0
    failed = 0

    plugin_files = sorted(
        f for f in os.listdir(plugins_dir)
        if f.endswith(".py") and f != "__init__.py" and not f.startswith("_")
    )

    for filename in plugin_files:
        module_name = f"plugins.{filename[:-3]}"
        try:
            module = importlib.import_module(module_name)
            if hasattr(module, "register"):
                module.register(app)
                loaded += 1
                print(f"[Plugins] Loaded: {module_name}")
            else:
                print(f"[Plugins] Skipped (no register()): {module_name}")
        except Exception as e:
            failed += 1
            print(f"[Plugins] Failed: {module_name} - {e}")
            traceback.print_exc()

    print(f"[Plugins] Loaded {loaded} plugin(s), {failed} failed.")
    total = sum(len(v) for v in CMD_LIST.values())
    print(f"[Plugins] Total commands registered: {total}")
    for cat, cmds in sorted(CMD_LIST.items()):
        print(f"  {cat}: {len(cmds)} commands")
