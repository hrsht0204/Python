import os
import stat

def is_hidden(filepath):
    """Check if a file or folder is hidden."""
    name = os.path.basename(filepath)
    # Check for dot-files (common hidden files)
    if name.startswith('.'):
        return True
    # Check for Windows hidden file attribute
    try:
        return bool(os.stat(filepath).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)
    except (AttributeError, FileNotFoundError):
        return False

def list_directory_contents(current_path, show_hidden=False):
    """List files and folders in the specified directory, with an option to show/hide hidden items."""
    try:
        all_items = os.listdir(current_path)
        visible_items = []
        
        print(f"\n--- Contents of '{os.path.basename(current_path) or current_path}' ---")
        if not show_hidden:
            print("(Hidden files are currently hidden. Press 'h' to show them)")
        else:
            print("(Showing all files, including hidden ones)")
        print("-" * 40)
        
        # Filter and display items
        for item in all_items:
            item_path = os.path.join(current_path, item)
            if not show_hidden and is_hidden(item_path):
                continue # Skip hidden files if show_hidden is False
            
            visible_items.append(item)
            
        # Display the filtered items with index numbers
        for index, item in enumerate(visible_items, start=1):
            print(f"[{index}] {item}")
            
        if not visible_items:
            print("  (This folder is empty)")
            
        return visible_items
    except PermissionError:
        print("\nAccess Denied: You don't have permission to view this folder.")
        return []
    except Exception as e:
        print(f"\nError accessing the directory: {e}")
        return []

def search_folder(folder_name, search_path):
    """Search for a folder in the specified directory and return its path if found."""
    folder_name_lower = folder_name.lower()
    for root, dirs, files in os.walk(search_path):
        for dir_name in dirs:
            if dir_name.lower() == folder_name_lower:
                return os.path.join(root, dir_name)
    return None

def search_file(filename, search_path):
    """Search for a file in the specified directory and return its path if found."""
    filename_lower = filename.lower()
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file.lower() == filename_lower:
                return os.path.join(root, file)
    return None

def is_text_file(file_path):
    """Check if a file is a text file by attempting to read a small portion of it."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file.read(512)
        return True
    except:
        return False

def handle_file_open(file_path):
    """Helper function to read and open files."""
    if is_text_file(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                print("\n--- File Content Start ---\n")
                print(content)
                print("\n--- File Content End ---")
            
            open_choice = input("\nDo you want to open this file in its default app? (y/n): ").strip().lower()
            if open_choice in ['yes', 'y']:
                os.startfile(file_path)
        except Exception as e:
            print(f"Error reading/opening text file: {e}")
    else:
        # Non-text files (images, videos, PDFs, etc.)
        open_choice = input(f"'{os.path.basename(file_path)}' is not a text file. Open it anyway? (y/n): ").strip().lower()
        if open_choice in ['yes', 'y']:
            try:
                os.startfile(file_path)
                print(f"Opening '{os.path.basename(file_path)}'...")
            except Exception as e:
                print(f"Error opening file: {e}")
        else:
            print("File opening cancelled.")

def main():
    base_path = r"C:\Users\Hari krishan"  # Change this path as needed
    
    # Fallback just in case the path doesn't exist
    if not os.path.exists(base_path):
        print(f"Warning: The path '{base_path}' does not exist.")
        base_path = os.getcwd() # Uses current working directory instead
        print(f"Defaulting to: {base_path}")

    current_path = base_path
    show_hidden = False  # Keep hidden files hidden by default
    
    # Load items once before starting the loop
    current_items = list_directory_contents(current_path, show_hidden)

    while True:
        # Ask for number, name, or commands
        user_input = input("\nEnter number to select, name to search (or 'b'=back, 'h'=toggle hidden, 'e'=exit): ").strip()
        
        # 1. Check for exit condition
        if user_input.lower() in ['e', 'exit']:
            print("Exiting the program. See ya!")
            break
            
        # 2. Check for back condition
        elif user_input.lower() in ['b', 'back']:
            parent_path = os.path.dirname(current_path)
            if parent_path and parent_path != current_path:
                previous_dir = os.path.basename(current_path)
                current_path = parent_path
                print(f"\nMoved up from '{previous_dir}' to '{os.path.basename(current_path) or current_path}'.")
                current_items = list_directory_contents(current_path, show_hidden)
            else:
                print("\nYou're already at the top-level directory.")
            continue

        # 3. Check for hidden files toggle
        elif user_input.lower() in ['h', 'hidden']:
            show_hidden = not show_hidden
            state = "shown" if show_hidden else "hidden"
            print(f"\n[!] Hidden files are now {state}.")
            current_items = list_directory_contents(current_path, show_hidden)
            continue

        # 4. Check if the user typed a number (Index Navigation)
        if user_input.isdigit():
            index = int(user_input)
            
            # Verify the number is within the valid range
            if 1 <= index <= len(current_items):
                selected_name = current_items[index - 1] # -1 because lists are 0-indexed
                target_path = os.path.join(current_path, selected_name)
                
                # If it's a folder, navigate into it
                if os.path.isdir(target_path):
                    previous_dir = os.path.basename(current_path)
                    current_path = target_path
                    print(f"\nMoved to folder: '{os.path.basename(current_path)}' from '{previous_dir}'.")
                    current_items = list_directory_contents(current_path, show_hidden)
                    continue
                # If it's a file, open it
                elif os.path.isfile(target_path):
                    handle_file_open(target_path)
                    continue
            else:
                print(f"\nInvalid number! Please enter a number between 1 and {len(current_items)}.")
                continue

        # 5. If not a command or number, treat it as a deep search query
        print(f"\nSearching for '{user_input}' in {base_path}... (This might take a moment)")
        
        folder_path = search_folder(user_input, base_path)
        if folder_path:
            previous_dir = os.path.basename(current_path)
            current_path = folder_path
            print(f"\nFound! Moved to folder: '{os.path.basename(current_path)}' from '{previous_dir}'.")
            current_items = list_directory_contents(current_path, show_hidden)
            continue
            
        file_path = search_file(user_input, base_path)
        if file_path:
            print(f"\nFile found: '{os.path.basename(file_path)}'")
            handle_file_open(file_path)
            continue

        # If it wasn't a valid command, number, or search result
        print("\nFile or folder not found. Please check the name or number and try again.")

if __name__ == "__main__":
    main()