#default - In default you can override values. calling module/child module will pass the value when have to override
variable "ami_id" {
    type = string
    default = "ami-09c813fb71547fc4f"  
}

# mandatory
variable "sg_id" {
  
}

variable "instance_type" {
 type = string
 default = "t3.micro"
 validation {
   condition = contains(["t3.micro","t3.small","t3.medium"], var.instance_type)
   error_message = "Valid values for instance type are : t3.micro, t3.small, t3.medium"
 }
}
#if you don't give default it's mandatory variable. if you give default it becomes optional
#optional
variable "ec2_tags" {
    type= map(string) 
    default = {}
}