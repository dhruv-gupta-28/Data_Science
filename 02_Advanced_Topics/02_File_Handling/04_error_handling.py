"""
Advanced File Handling: Error Handling and Robustness
======================================================

Topics Covered:
- Exception handling in file operations
- File validation and verification
- Safe file operations
- Context managers and cleanup
- File permissions and attributes
- Atomic operations
"""

import os
import shutil

# ============================================================================
# 1. SAFE FILE OPERATIONS WITH ERROR HANDLING
# ============================================================================

print("--- Safe File Operations ---")

def safe_read_file(filename):
    """Safely read file with error handling"""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'")
        return None
    except IOError as e:
        print(f"Error reading file: {e}")
        return None

# Test safe read
result = safe_read_file("nonexistent.txt")
print(f"Result: {result}")

# ============================================================================
# 2. FILE EXISTENCE AND TYPE CHECKING
# ============================================================================

print("\n--- File Validation ---")

def validate_file(filepath):
    """Check file validity"""
    if not os.path.exists(filepath):
        return "File does not exist"
    
    if not os.path.isfile(filepath):
        return "Path is not a file"
    
    if not os.access(filepath, os.R_OK):
        return "File is not readable"
    
    size = os.path.getsize(filepath)
    return f"Valid file ({size} bytes)"

# Create test file
test_file = "test.txt"
with open(test_file, 'w') as f:
    f.write("Test content")

print(f"File validation: {validate_file(test_file)}")

# ============================================================================
# 3. ATOMIC FILE OPERATIONS
# ============================================================================

print("\n--- Atomic File Operations ---")

def atomic_write(filename, content):
    """Write file atomically (safe from corruption)"""
    # Write to temp file first
    temp_file = filename + '.tmp'
    
    try:
        # Write to temporary file
        with open(temp_file, 'w') as f:
            f.write(content)
        
        # Replace original file
        if os.path.exists(filename):
            os.remove(filename)
        os.rename(temp_file, filename)
        
        print(f"Successfully wrote to {filename}")
    except Exception as e:
        print(f"Error during atomic write: {e}")
        if os.path.exists(temp_file):
            os.remove(temp_file)

atomic_write("atomic_test.txt", "Atomic content")

# ============================================================================
# 4. FILE COPY WITH PROGRESS
# ============================================================================

print("\n--- Safe File Copy ---")

def safe_copy_file(source, destination, chunk_size=1024*1024):
    """Copy file safely with error handling"""
    try:
        if not os.path.exists(source):
            raise FileNotFoundError(f"Source file '{source}' not found")
        
        total_size = os.path.getsize(source)
        copied = 0
        
        with open(source, 'rb') as src:
            with open(destination, 'wb') as dst:
                while True:
                    chunk = src.read(chunk_size)
                    if not chunk:
                        break
                    dst.write(chunk)
                    copied += len(chunk)
                    percent = (copied / total_size) * 100
                    print(f"  Copying: {percent:.1f}%", end='\r')
        
        print(f"\nSuccessfully copied {source} to {destination}")
        return True
    except Exception as e:
        print(f"Error copying file: {e}")
        if os.path.exists(destination):
            os.remove(destination)
        return False

# Test copy
safe_copy_file(test_file, "test_copy.txt")

# ============================================================================
# 5. BACKUP AND RECOVERY
# ============================================================================

print("\n--- Backup and Recovery ---")

def create_backup(filename):
    """Create backup of file"""
    if not os.path.exists(filename):
        return False
    
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{filename}.backup_{timestamp}"
    
    try:
        shutil.copy2(filename, backup_name)
        print(f"Backup created: {backup_name}")
        return backup_name
    except Exception as e:
        print(f"Backup failed: {e}")
        return None

def restore_backup(backup_file, original_file):
    """Restore file from backup"""
    try:
        shutil.copy2(backup_file, original_file)
        print(f"Restored from {backup_file}")
        return True
    except Exception as e:
        print(f"Restore failed: {e}")
        return False

# Create and restore backup
backup = create_backup(test_file)
if backup:
    print(f"File backed up to: {backup}")

# ============================================================================
# 6. FILE LOCKING (SIMULATED)
# ============================================================================

print("\n--- File Operations Lock ---")

class FileLocker:
    """Simple file locking mechanism"""
    def __init__(self, filename):
        self.filename = filename
        self.lock_file = filename + '.lock'
    
    def acquire_lock(self):
        """Acquire lock"""
        if os.path.exists(self.lock_file):
            return False
        with open(self.lock_file, 'w') as f:
            f.write("locked")
        return True
    
    def release_lock(self):
        """Release lock"""
        if os.path.exists(self.lock_file):
            os.remove(self.lock_file)
    
    def __enter__(self):
        self.acquire_lock()
        return self
    
    def __exit__(self, *args):
        self.release_lock()

# Test file locking
with FileLocker(test_file) as locker:
    print("File is locked for exclusive access")

# ============================================================================
# 7. DIRECTORY OPERATIONS WITH ERROR HANDLING
# ============================================================================

print("\n--- Safe Directory Operations ---")

def safe_create_directory(path):
    """Safely create directory"""
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Created directory: {path}")
        return True
    except PermissionError:
        print(f"Permission denied to create {path}")
        return False
    except Exception as e:
        print(f"Error creating directory: {e}")
        return False

def safe_remove_directory(path):
    """Safely remove directory"""
    try:
        shutil.rmtree(path)
        print(f"Removed directory: {path}")
        return True
    except Exception as e:
        print(f"Error removing directory: {e}")
        return False

# Test directory operations
safe_create_directory("test_dir")
safe_remove_directory("test_dir")

# ============================================================================
# 8. FILE CONTENT VALIDATION
# ============================================================================

print("\n--- File Content Validation ---")

def validate_text_file(filename):
    """Validate text file content"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return {
            'size': len(content),
            'lines': content.count('\n') + 1,
            'words': len(content.split()),
            'valid_encoding': True
        }
    except UnicodeDecodeError:
        return {'valid_encoding': False, 'error': 'Invalid encoding'}
    except Exception as e:
        return {'error': str(e)}

validation = validate_text_file(test_file)
print(f"File validation results: {validation}")

# ============================================================================
# 9. SAFE FILE DELETION
# ============================================================================

print("\n--- Safe File Deletion ---")

def safe_delete_file(filename, confirm=True):
    """Safely delete file with confirmation"""
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist")
        return False
    
    if confirm:
        response = input(f"Delete {filename}? (y/n): ")
        if response.lower() != 'y':
            print("Deletion cancelled")
            return False
    
    try:
        os.remove(filename)
        print(f"Deleted {filename}")
        return True
    except PermissionError:
        print(f"Permission denied to delete {filename}")
        return False
    except Exception as e:
        print(f"Error deleting file: {e}")
        return False

# Note: We'll skip actual deletion due to interactive nature

# ============================================================================
# 10. PRACTICE PROBLEMS
# ============================================================================

print("\n--- Practice Problems ---")

# Problem 1: Recursive directory listing
print("\nProblem 1: List All Files Recursively")
def list_all_files(directory):
    """List all files recursively"""
    files = []
    try:
        for root, dirs, filenames in os.walk(directory):
            for filename in filenames:
                files.append(os.path.join(root, filename))
    except PermissionError:
        print(f"Permission denied to access {directory}")
    return files

# List files in current directory
current_files = list_all_files(".")
print(f"Found {len(current_files)} files in current directory")

# Problem 2: Find large files
print("\nProblem 2: Find Large Files")
def find_large_files(directory, min_size_mb=10):
    """Find files larger than specified size"""
    large_files = []
    min_size = min_size_mb * 1024 * 1024
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                if os.path.getsize(filepath) > min_size:
                    large_files.append(filepath)
            except OSError:
                continue
    
    return large_files

# ============================================================================
# 11. CHALLENGES
# ============================================================================

print("\n--- Challenges ---")

# Challenge 1: Safe move operation
print("\nChallenge 1: Safe Move Operation")
# TODO: Implement safe move with rollback on failure

# Challenge 2: File synchronization
print("\nChallenge 2: Directory Sync")
# TODO: Sync two directories efficiently

# Challenge 3: File integrity checker
print("\nChallenge 3: File Integrity")
# TODO: Use checksums to verify file integrity

# ============================================================================
# 12. CLEANUP
# ============================================================================

print("\n--- Cleanup ---")

files_to_remove = [test_file, "test_copy.txt", "atomic_test.txt"]
for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
        print(f"Cleaned up {file}")
