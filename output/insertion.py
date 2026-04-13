# Function to write insertion operation
def write_insertion():
    """
    Demonstrates how to insert an element into a sorted list in-place.

    Time complexity: O(n)
    Space complexity: O(1)

    :return: None
    """

    # Sample sorted list
    sorted_list = [1, 3, 5, 7, 9]

    # Insertion point and value to be inserted
    insert_at = int(input("Enter the index at which you want to insert a new element: "))
    value_to_insert = int(input("Enter the value to be inserted: "))

    # Adjust list length if necessary
    sorted_list.insert(insert_at, value_to_insert)

    print("\nUpdated Sorted List:")
    print(sorted_list)


# Call the function
write_insertion()