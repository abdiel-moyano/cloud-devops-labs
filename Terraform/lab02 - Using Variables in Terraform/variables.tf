variable "resource_group_name" {
  description = "The name of the Resource Group"
  type        = string
  default     = "my-resource-group"
}

variable "resource_group_location" {
  description = "The Azure region for the Resource Group"
  type        = string
  default     = "East US"
}

variable "storage_account_name" {
  description = "The name of the Storage Account"
  type        = string
}