import sys
from math_lib import projection


def main():
    if len(sys.argv) != 5:
        print("Usage: python3 projection_test.py <fov> <ratio> <near> <far>")
        print("Example: python3 projection_test.py 90 1.77 0.1 100")
        return
    try:
        fov = float(sys.argv[1])
        ratio = float(sys.argv[2])
        near = float(sys.argv[3])
        far = float(sys.argv[4])
        proj_matrix = projection(fov, ratio, near, far)
        # Write to proj file
        with open("proj", "w") as f:
            for row in proj_matrix.data:
                line = ",".join(map(str, row))
                f.write(line + "\n")
        print(f"Successfully generated 'proj' with FOV: {fov}, Ratio: {ratio}")
    except ValueError:
        print("Error: All arguments must be numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()