resource "aws_vpc" "main" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "main"
  }
}

resource "aws_subnet" "main" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "main"
  }
}

resource "aws_instance" "free_tier_example" {
  ami           = "ami-06b21ccaeff8cd686"  # Replace with an Amazon Linux 2 AMI ID for your region
  instance_type = "t2.micro"               # Free tier-eligible instance type

  tags = {
    Name = "Free-Tier-Instance"
  }

  # Optional: Configure security group to allow SSH access
  vpc_security_group_ids = [aws_security_group.allow_ssh.id]

  # Optional: Add a key pair for SSH access
  key_name = "ec2-ssh"          # Replace with your key pair name if you want SSH access
}

# Security Group allowing SSH access (port 22)
resource "aws_security_group" "allow_ssh" {
  name_prefix = "allow_ssh_"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]           # Allows SSH from any IP; restrict this for better security
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}