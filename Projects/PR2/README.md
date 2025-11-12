## Data

the data for this project are awailable at: https://surfdrive.surf.nl/files/index.php/s/m81MjIPuvHm2lNw

Note: the data of this project are in root format. Python can read this format by using uproot package (pip install uproot). Below a simple macro you can modify adding the proper names:

## Code example
import uproot

### Open the ROOT file
file = uproot.open("your_file.root")

### Access the directory containing the TTrees
directory = file["your_directory_name"]

### List all TTrees in the directory (optional, for confirmation)
print("TTrees in directory:", directory.keys())

### Access each TTree by name
tree1 = directory["TTree1_name"]
tree2 = directory["TTree2_name"]

### List branches in each TTree (optional, for confirmation)
print("Branches in TTree1:", tree1.keys())
print("Branches in TTree2:", tree2.keys())

### Access specific branches and read their data as arrays
branch1_data = tree1["branch_name1"].array()
branch2_data = tree2["branch_name2"].array()

### Example: print the data of a branch
print("Data from branch_name1 in TTree1:", branch1_data)
print("Data from branch_name2 in TTree2:", branch2_data)

### You can also iterate over multiple branches if needed
for branch_name in tree1.keys():
    data = tree1[branch_name].array()
    print(f"Data from {branch_name} in TTree1:", data)


