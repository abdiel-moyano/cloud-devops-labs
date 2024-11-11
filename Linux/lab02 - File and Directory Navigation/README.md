
# File and Directory Navigation Lab

## Objective
This lab is designed to help you practice basic Linux commands for navigating and managing the filesystem. You will learn how to view, create, and delete directories using commands such as `ls`, `cd`, `pwd`, `mkdir`, and `rmdir`.

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

### Step 2: Practice Basic Navigation Commands

1. **List Files and Directories (`ls`)**  
   Use `ls` to list the contents of the current directory. You can also use `ls -l` for a detailed view with additional information like permissions, owner, and modification date.

   ```bash
   ls
   ls -l
   ```

2. **Print Working Directory (`pwd`)**  
   Display the current directory path.

   ```bash
   pwd
   ```

3. **Change Directory (`cd`)**  
   Navigate to different directories. For example, to switch to the `/tmp` directory:

   ```bash
   cd /tmp
   ```

   Use `cd ..` to move up one directory level.

### Step 3: Create and Remove Directories

1. **Create a Directory (`mkdir`)**  
   Use `mkdir` followed by the directory name to create a new folder. For instance, create a directory called `test_dir`:

   ```bash
   mkdir test_dir
   ```

2. **Navigate into the New Directory**  
   Change to the newly created directory:

   ```bash
   cd test_dir
   ```

3. **Remove a Directory (`rmdir`)**  
   Move up one level and remove the `test_dir` directory:

   ```bash
   cd ..
   rmdir test_dir
   ```

### Step 4: Create Nested Directories

1. **Create Nested Directories with `mkdir -p`**  
   Create a series of nested directories in one command. For example:

   ```bash
   mkdir -p folder1/folder2/folder3
   ```

2. **Remove Nested Directories**  
   Remove the nested directories from the innermost to the outermost, or use:

   ```bash
   rmdir -p folder1/folder2/folder3
   ```

### Step 5: Exit the Container

When you have completed the lab, exit the Alpine Linux session:

```bash
exit
```

## Conclusion
In this lab, you practiced:
- Navigating the filesystem with `ls`, `cd`, and `pwd`.
- Creating and deleting directories with `mkdir` and `rmdir`.
- Building nested directory structures.

These commands are essential for managing the Linux filesystem effectively.
