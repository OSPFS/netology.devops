# Configure the AWS Provider
provider "aws" {
  region                  = "us-east-1"
  shared_credentials_file = "~/.aws/credentials"
  profile                 = "default"

}

# terraform {
#   backend "s3" {
#     bucket = "dz27-state-bucket"
#     key    = "./terraform.tfstate"
#     region = "us-east-1"
#   }
# }

locals {
  instance_type_map = {
    stage = "t2.micro"
    prod  = "t2.nano"
  }

  instance_count_map = {
    stage = 1
    prod  = 2
  }
}

resource "aws_instance" "dz28-amazon-linux" {
  ami           = "ami-00514a528eadbc95b" // Amazon Linux
  instance_type = local.instance_type_map[terraform.workspace]
  count         = local.instance_count_map[terraform.workspace]
  lifecycle {
    create_before_destroy = true
  }
}

# locals {
#   instances = {
#     "t3.micro" = data.aws_ami.amazon_linux.id
#     "t3.large" = data.aws_ami.amazon_linux.id
#   }
# }

# resource "aws_instance" "dz28-amazon-linux-second" {
#   ami           = "ami-00514a528eadbc95b" // Amazon Linux
#   instance_type = local.instance_type_map[terraform.workspace]
#   count         = local.instance_count_map[terraform.workspace]
#   lifecycle {
#     create_before_destroy = true
#   }
# }

# locals {
#   ws_id = toset([
#     "stage",
#     "prod",
#   ])
# }

# resource "aws_instance" "dz28-amazon-linux-third" {
#   for_each = local.ws_id

#   ami           = "ami-a1b2c3d4"
#   instance_type = "t3.micro"
#   subnet_id     = each.key # note: each.key and each.value are the same for a set

#   tags = {
#     Name = "Server ${each.key}"
#   }
# }
