
# File Management Lab

## Objective
This lab is designed to help you practice basic Linux commands for managing files. You will learn how to create, move, copy, and delete files using commands like `touch`, `cp`, `mv`, and `rm`.

## Prerequisites
- Docker Desktop installed on your machine.
- Basic understanding of Docker and Linux command-line.

## Steps

### Step 1: Start the Alpine Linux Container

To begin, start an Alpine Linux container in interactive mode:

```bash
docker run -it alpine
```

This command opens a terminal session inside the Alpine Linux container.

### Step 2: Create Files with `touch`

1. **Create an empty file**  
   Use `touch` to create a file named `file1.txt`:

   ```bash
   touch file1.txt
   ```

2. **Verify file creation**  
   List files in the current directory:

   ```bash
   ls
   ```

### Step 3: Copy Files with `cp`

1. **Copy the file**  
   Create a copy of `file1.txt` named `file1_copy.txt`:

   ```bash
   cp file1.txt file1_copy.txt
   ```

2. **Verify the copy**  
   Check that both files are present:

   ```bash
   ls
   ```

### Step 4: Move Files with `mv`

1. **Rename a file**  
   Use `mv` to rename `file1_copy.txt` to `renamed_file.txt`:

   ```bash
   mv file1_copy.txt renamed_file.txt
   ```

2. **Move a file to a directory**  
   - Create a directory called `my_folder`:

     ```bash
     mkdir my_folder
     ```

   - Move `renamed_file.txt` into `my_folder`:

     ```bash
     mv renamed_file.txt my_folder/
     ```

3. **Verify the move**  
   Confirm that the file is now in `my_folder`:

   ```bash
   ls my_folder/
   ```

### Step 5: Delete Files with `rm`

1. **Delete a file**  
   Remove `file1.txt`:

   ```bash
   rm file1.txt
   ```

2. **Delete a file in a specific directory**  
   Remove `renamed_file.txt` from `my_folder`:

   ```bash
   rm my_folder/renamed_file.txt
   ```

3. **Remove an empty directory (optional)**  
   If you want to delete `my_folder`, use:

   ```bash
   rmdir my_folder
   ```

### Step 6: Exit the Container

When you have completed the lab, exit the Alpine Linux session:

```bash
exit
```

## Conclusion
In this lab, you practiced:
- Creating files with `touch`.
- Copying files with `cp`.
- Moving and renaming files with `mv`.
- Deleting files with `rm`.

These commands are essential for managing files in a Linux environment.
