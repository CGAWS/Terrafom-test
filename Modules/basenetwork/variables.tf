# Let us set the default values t

variable "aws_access_key" {}
variable "aws_secret_key" {}
variable "aws_key_path" {}
variable "aws_key_name" {}

variable "aws_region" {
  default = "us-east-1"
}


variable "aws_vpc_name" {}

variable "vpc_cidr_base" {
  default = "10.20"
}

variable "vpc_instance_tenancy" {
  default = "default"
}


variable "vpc_enable_dns_support" {
  default = "true"
}

variable "vpc_enable_dns_hostnames" {
  default = "true"
}

variable "vpc_enable_classiclink" {
  default = "false"
}

variable "aws_azs" {}

variable "az_count" {}
