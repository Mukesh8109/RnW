import uuid
import time
def generate_uuid_base_timestamp():
   print("\n--- UUID1 Generator ---\n")

# Timestamp (in 100-ns intervals from UUID epoch: 1582-10-15)
   timestamp = int((time.time() + 12219292800) * 1e7)  # UUID epoch offset

# Optional: manually specify a MAC address
   mac = 0x123456789abc

# Generate UUID1 with specific node and clock sequence
   custom_uuid1 = uuid.uuid1(node=mac)

   print("Custom UUID1:", custom_uuid1)
   print("="*60)

def generate_uuid4():
   print("\n--- UUID4 Generator ---\n")

   custom_uuid4 = uuid.uuid4()
   print(f"Custom UUID4:{custom_uuid4}")
   print("="*60)
