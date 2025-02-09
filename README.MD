# expense EC2 Module

**INPUTS:**
* ami_id(optional): String Value. Default value is devops-practice AMI ID
* sg_id(mandatory) : User must supply sg_id
* instance_type(Optional): t3.micro is default value. User can provide t3.small or t3.micro or t3.medium
* tags(Optional): Default is empty. User can provide tags in map structure

**OUTPUTS:**
* public_ip : public ip of the instance creatd
* private_ip : private ip of the instance creatd