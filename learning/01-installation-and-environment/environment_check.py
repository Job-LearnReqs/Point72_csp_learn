import importlib
import platform


def check_import(module_name: str) -> str:
    try:
        module = importlib.import_module(module_name)
    except Exception as exc:
        return f"{module_name}: unavailable ({type(exc).__name__}: {exc})"

    version = getattr(module, "__version__", "version unknown")
    return f"{module_name}: available ({version})"


def main() -> None:
    print(f"Python: {platform.python_version()}")
    print(check_import("csp"))
    print(check_import("pandas"))
    print(check_import("pyarrow"))


if __name__ == "__main__":
    main()
