# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

# Create a VPC

resource "aws_vpc" "ndevops_net" {
 cidr_block = "10.100.0.0/16"
}

data "aws_caller_identity" "default" {
}

data "aws_region" "default" {
}

data "aws_ami" "ubuntu" {
  most_recent = true

 filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "bubuntu" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t2.micro"
}

