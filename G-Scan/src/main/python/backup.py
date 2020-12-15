import os
import shutil
from datetime import datetime

def backup_file(master_application, file_name, backup_file_name,
        scan_dir, backup_dir):
    """Creates a backup copy of a file into a specified backup
    directory."""

    if os.path.isdir(backup_dir):
        shutil.copyfile(
            scan_dir + "/" + file_name, backup_dir + "/" + backup_file_name)
        
        master_application.write_log("Backed up " + file_name)

    else:
        master_application.write_log(
            "Backup directory not found. Please check your settings.")

def backup_housekeeping(self, backup_dir):
    """Checks the backup directory for any files over 30 days old and
    deletes them. I have removed this from being used in the code in
    case of issues arising from a user pointing their backup directory
    to the wrong folder, deleting potentially important files on a
    server directory."""
    
    if os.path.isdir(backup_dir):
        backup_folder = os.listdir(backup_dir)
        file_extensions = (".pdf", ".tif", ".tiff", ".jpeg", ".jpg", ".png")

        for item in backup_folder:
            if item.lower().endswith(file_extensions):
                last_modified_time = datetime.fromtimestamp(
                    os.path.getmtime(backup_dir + "/" + item))
                
                current_time = datetime.now()
                difference = current_time - last_modified_time

                if difference.days > 30:
                    os.remove(backup_dir + "/" + item)
    else:
        self.write_log(
            "Backup directory not found. Please check your settings.")