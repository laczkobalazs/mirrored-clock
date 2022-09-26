variable "aws_profile" {
  type    = string
  default = "laczkobalazs-admin"
}

variable "aws_region" {
  type    = string
  default = "eu-central-1"
}

variable "public_subnet_name" {
  description = "Name of the public subnets"
  type = []
  default = ["public-subnet-001", "public-subnet-002"]
}

variable "public_subnet_cidr" {
  description = "Default CIDR block of the public subnet"
  type = []
  default = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "private_subnet_name" {
  description = "Name of the private subnets"
  type = []
  default = ["private-subnet-001", "private-subnet-002"]
}

variable "private_subnet_cidr" {
  description = "Default CIDR block of the private subnet"
  type = []
  default = ["10.0.101.0/24", "10.0.102.0/24"]
}