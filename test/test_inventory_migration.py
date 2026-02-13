from models import BloodInventory
from data_manager import load_json
from storage import INVENTORY_FILE
import os

def test_inventory_migration():
    print(f"Testing Inventory Migration...")
    
    # 1. Initialize Inventory (Should load existing data, likely list of ints)
    inv = BloodInventory()
    print(f"Loaded Quantities: {inv.quantities}")
    
    # 2. Update Stock (Should trigger save in NEW format)
    inv.update_stock("A+", 5)
    print("Updated Stock A+ by 5")
    
    # 3. Verify File Content
    data = load_json(INVENTORY_FILE)
    print(f"File Content after update: {data}")
    
    if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
        print("SUCCESS: File saved in new structured format.")
    else:
        print("FAILURE: File format incorrect.")

if __name__ == "__main__":
    test_inventory_migration()
