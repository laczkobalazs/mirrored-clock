resource "aws_vpc" "main" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "Main"
  }
}

resource "aws_subnet" "public" {
  count = 2
  Name = element(var.public_subnet_name, count.index)
  vpc_id     = aws_vpc.main.id
  cidr_block = element(var.public_subnet_cidr, count.index)

  tags = {
    Name = "Main"
    type = "public"
  }
}

resource "aws_subnet" "private" {
  count = 2
  Name = element(var.private_subnet_name, count.index)
  vpc_id     = aws_vpc.main.id
  cidr_block = element(var.private_subnet_cidr, count.index)

  tags = {
    Name = "Main"
    type = "private"
  }
}