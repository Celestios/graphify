"""Plugin discovery and lifecycle management."""
import importlib.metadata
from pathlib import Path

def discover_plugins(root: Path) -> list:
    """Find all installed graphify plugins via setuptools entry_points.
    Only instantiates a plugin if its activation condition is met
    (e.g., config file exists)."""
    plugins = []
    for ep in importlib.metadata.entry_points(group="graphify.plugins"):
        cls = ep.load()
        instance = cls()
        if hasattr(instance, "should_activate"):
            if not instance.should_activate(root):
                continue
        plugins.append(instance)
    return plugins

def run_hook(plugins, hook_name, *args, **kwargs):
    """Run a named hook across all loaded plugins, chaining the first arg."""
    result = args[0] if args else None
    for plugin in plugins:
        fn = getattr(plugin, hook_name, None)
        if fn:
            out = fn(result, *args[1:], **kwargs)
            if out is not None:
                result = out
    return result
