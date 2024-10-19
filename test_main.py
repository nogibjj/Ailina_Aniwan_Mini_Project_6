"""
Test main.py functions
"""

from main import results


def test_functions():
    result_dict = results()

    assert result_dict["extract"] == "data/women-stem.csv", "Extract function failed"
    print("Extract: Success")

    assert result_dict["transform"] == "women-stem.db", "Transform function failed"
    print("Transform: Success")

    assert result_dict["create"] == "Create Success", "Create query function failed"
    print("Create Query: Success")

    assert result_dict["read"] == "Read Success", "Read query function failed"
    print("Read Query: Success")

    assert result_dict["update"] == "Update Success", "Update query function failed"
    print("Update Query: Success")

    assert result_dict["delete"] == "Delete Success", "Delete query function failed"
    print("Delete Query: Success")


if __name__ == "__main__":
    test_functions()
    print("All tests passed successfully!✨")
