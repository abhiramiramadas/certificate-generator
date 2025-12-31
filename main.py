import argparse
import uvicorn
import os
import sys
from generator import generate_bulk

def print_header():
    C1 = "\033[96m"
    C2 = "\033[93m"
    B = "\033[1m"
    R = "\033[0m"
    
    print(f"{C1}{B}" + "*"*50)
    print(f"* {' '*46} *")
    print(f"* {C2}   BULK CERTIFICATE GENERATOR    {C1}   *")
    print(f"* {' '*46} *")
    print("*"*50 + f"{R}\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--local", action="store_true")
    parser.add_argument("--api", action="store_true")
    args = parser.parse_args()

    if args.local:
        run_local()
    elif args.api:
        run_api()
    else:
        print_header()
        print("1. Run Local Bulk Generation (Organized by Folder)")
        print("2. Start API Server")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ")
        if choice == "1":
            run_local()
        elif choice == "2":
            run_api()
        else:
            sys.exit()

def run_local():
    G = "\033[92m"
    RE = "\033[91m"
    RS = "\033[0m"
    try:
        results = generate_bulk()
        print(f"{G}✅ Successfully generated {len(results)} individual folders in 'certificates/'.{RS}")
    except Exception as e:
        print(f"{RE}❌ Error: {e}{RS}")

def run_api():
    print("\033[94mStarting API server on http://localhost:8000...\033[0m")
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()