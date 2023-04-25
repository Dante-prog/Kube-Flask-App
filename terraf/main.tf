terraform {
  required_providers {
    linode = {
      source  = "linode/linode"
      version = "1.30.0"
    }
  }
}

provider "linode" {
  token = var.linode_token
}

variable "linode_token" {
  description = "Linode API token"
  sensitive   = true
}
resource "linode_instance" "Test" {
  count = 2
  label = "Test-instance-${count.index + 1}"
  image = "linode/alpine3.17"
  region = "us-east"
  type = "g6-nanode-1"
  root_pass = var.root_password
  authorized_keys = [var.ssh_public_key]
}

resource "linode_instance" "example1" {
  label = "example-instance-1"
  image = "linode/ubuntu20.04"
  private_ip = true
  region = "us-east"
  type = "g6-nanode-1"
  root_pass = var.root_password
  authorized_keys = [var.ssh_public_key]
}

resource "linode_instance" "example2" {
  label = "example-instance-2"
  image = "linode/ubuntu20.04"
  region = "us-east"
  private_ip = true
  type = "g6-standard-1"
  root_pass = var.root_password
  authorized_keys = [var.ssh_public_key]
}

resource "linode_nodebalancer" "example" {
  label = "example-nodebalancer"
  region = "us-east"
}

resource "linode_nodebalancer_config" "example" {
  nodebalancer_id = linode_nodebalancer.example.id
  protocol = "http"
  port = 80
  check = "connection"
}

resource "linode_instance" "terraform-db" {
  image = "linode/centos7"
  label = "Terraform-Db-Example"
  group = "Terraform"
  region = "us-south"
  type = "g6-standard-1"
  swap_size = 1024
  authorized_keys = [var.ssh_public_key]
  root_pass = var.root_password
}

resource "linode_database_postgresql" "example_db" {
  label = "mydatabase"
  engine_id = "postgresql/13.8"
  region = "us-southeast"
  type = "g6-nanode-1"
}


variable "root_password" {
  description = "The root password for the Linode instance"
  sensitive   = true
}

variable "ssh_public_key" {
  description = "The public SSH key to be added to the Linode instance"
}

