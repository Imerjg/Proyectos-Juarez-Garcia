def main():
    import argparse

    parser = argparse.ArgumentParser(description="Enable Claude Sonnet 3.5 for all clients.")
    parser.add_argument('--enable', action='store_true', help='Enable Claude Sonnet for all clients')
    parser.add_argument('--status', action='store_true', help='Check the status of Claude Sonnet')

    args = parser.parse_args()

    if args.enable:
        enable_claude_sonnet()
    elif args.status:
        check_status()
    else:
        parser.print_help()

def enable_claude_sonnet():
    print("Enabling Claude Sonnet 3.5 for all clients...")

def check_status():
    print("Checking the status of Claude Sonnet...")

if __name__ == "__main__":
    main()