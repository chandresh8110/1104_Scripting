"""
Student Name: Chandreshkumar Patel
Student Id: 100925696

This is a inclass 4 activity  for scripting, perform by Chandreshkumar. 
"""



import json
from typing import Optional

def get_numeric_input(prompt: str, min_value: float = 0) -> Optional[float]:
    """Get numeric input from user with validation."""
    while True:
        value = input(prompt)
        if value.lower() == '':  # Allow empty input for optional maximum values
            return None
        try:
            num = float(value)
            if num < min_value:
                print(f"Value must be greater than {min_value}")
                continue
            return num
        except ValueError:
            print("Please enter a valid number")

def get_cpu_count(vcpu_str: str) -> float:
    """Extract CPU count from vCPU string."""
    try:
        # Handle cases like "2 vCPUs for a 1h 12m burst"
        return float(vcpu_str.split()[0])
    except (ValueError, IndexError):
        return 0

def get_memory_size(memory_str: str) -> float:
    """Extract memory size in GiB from memory string."""
    try:
        return float(memory_str.split()[0])
    except (ValueError, IndexError):
        return 0

def filter_instances(instances: list, min_cpu: float, max_cpu: Optional[float], 
                    min_memory: float, max_memory: Optional[float]) -> list:
    """Filter instances based on CPU and memory requirements."""
    filtered = []
    
    for instance in instances:
        cpu_count = get_cpu_count(instance['vcpu'])
        memory_size = get_memory_size(instance['memory'])
        
        # Check if instance meets minimum requirements
        if cpu_count < min_cpu or memory_size < min_memory:
            continue
            
        # Check maximum requirements if specified
        if (max_cpu and cpu_count > max_cpu) or (max_memory and memory_size > max_memory):
            continue
            
        filtered.append(instance)
    
    return filtered

def display_instances(instances: list):
    """Display filtered instances in a formatted way."""
    if not instances:
        print("\nNo instances found matching your requirements.")
        return
        
    print("\nMatching instances:")
    print("-" * 100)
    print(f"{'Instance Type':<20} {'vCPUs':<15} {'Memory':<15} {'Storage':<25} {'Network':<15}")
    print("-" * 100)
    
    for instance in instances:
        print(f"{instance['name']:<20} {instance['vcpu']:<15} {instance['memory']:<15} "
              f"{instance['storage']:<25} {instance['bandwidth']:<15}")

def main():
    print("AWS EC2 Instance Finder")
    print("=" * 50)
    print("(Press Enter for no maximum limit)")
    
    # Get CPU requirements
    min_cpu = get_numeric_input("Enter minimum CPU cores required: ", 0)
    max_cpu = get_numeric_input("Enter maximum CPU cores (optional): ", min_cpu)
    
    # Get memory requirements
    min_memory = get_numeric_input("Enter minimum memory (GiB) required: ", 0)
    max_memory = get_numeric_input("Enter maximum memory (GiB) (optional): ", min_memory)
    
    # Load instance data
    try:
        with open('D:\Scripting\Inclass 4\ec2_instance_types.json', 'r') as file:
            instances = json.load(file)
    except FileNotFoundError:
        print("Error: Instance data file not found")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON data")
        return
    
    # Filter and display instances
    filtered_instances = filter_instances(instances, min_cpu, max_cpu, min_memory, max_memory)
    display_instances(filtered_instances)

if __name__ == "__main__":
    main()