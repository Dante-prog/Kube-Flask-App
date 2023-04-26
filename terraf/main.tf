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

