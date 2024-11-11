
# Alpine Linux Installation Lab on Docker

## Objective
This lab guides you through installing and configuring Alpine Linux on Docker. It is designed to help you get familiar with the Linux environment and perform initial system configuration tasks.

## Prerequisites
- Docker Desktop installed on your machine.
- Basic understanding of Docker and Linux command-line.

## Steps

### Step 1: Pull the Alpine Linux Image

To begin, download the official Alpine Linux image from Docker Hub:

```bash
docker pull alpine
```

This command downloads the latest version of Alpine Linux.

### Step 2: Run the Alpine Container

Start an interactive container session with Alpine Linux:

```bash
docker run -it alpine
```

This command opens a terminal session inside the Alpine Linux container.

### Step 3: Initial System Setup

1. **Update Package Index**  
   Update the package index to make sure you have the latest package listings:

   ```bash
   apk update
   ```

2. **Install Essential Packages (Optional)**  
   You can install additional packages like `bash`, `curl`, or `nano`:

   ```bash
   apk add bash curl nano
   ```

3. **Switch to Bash (Optional)**  
   If you installed `bash` and want to use it, you can switch to it by typing:

   ```bash
   /bin/bash
   ```

### Step 4: Explore the Alpine Linux Environment

Use basic Linux commands to navigate and familiarize yourself with the system:

- **List files**: `ls`
- **Print working directory**: `pwd`
- **Check disk space**: `df -h`
- **View processes**: `top`

### Step 5: Save Changes (Optional)

If you want to save the current state of the container with installed packages, create a new image:

1. **Identify the container ID**:

   ```bash
   docker ps -a
   ```

2. **Commit the container to a new image**:

   ```bash
   docker commit <container_id> alpine_custom
   ```

### Step 6: Exit the Container

To exit the Alpine Linux session, type:

```bash
exit
```

## Conclusion
In this lab, you learned how to:
- Install and run Alpine Linux on Docker.
- Perform basic configurations and explore the Alpine environment.
- Save a customized container image for future use.

Happy learning!
