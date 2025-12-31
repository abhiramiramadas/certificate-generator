import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    required_libs = ["pillow", "pandas", "reportlab", "fastapi", "uvicorn"]
    for lib in required_libs:
        try:
            if lib == "pillow":
                __import__("PIL")
            else:
                __import__(lib)
        except ImportError:
            install(lib)

if __name__ == "__main__":
    main()