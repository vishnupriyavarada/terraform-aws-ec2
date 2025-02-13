 ec2-info = [
      + {
          + ami                                  = "ami-09c813fb71547fc4f"
          + arn                                  = "arn:aws:ec2:us-east-1:194722417509:instance/i-0cbf92b9c9b587ae2"
          + associate_public_ip_address          = true
          + availability_zone                    = "us-east-1b"
          + capacity_reservation_specification   = [
              + {
                  + capacity_reservation_preference = "open"
                  + capacity_reservation_target     = []
                },
            ]
          + cpu_core_count                       = 1
          + cpu_options                          = [
              + {
                  + amd_sev_snp      = ""
                  + core_count       = 1
                  + threads_per_core = 2
                },
            ]
          + cpu_threads_per_core                 = 2
          + credit_specification                 = [
              + {
                  + cpu_credits = "unlimited"
                },
            ]
          + disable_api_stop                     = false
          + disable_api_termination              = false
          + ebs_block_device                     = []
          + ebs_optimized                        = false
          + enable_primary_ipv6                  = null
          + enclave_options                      = [
              + {
                  + enabled = false
                },
            ]
          + ephemeral_block_device               = []
          + get_password_data                    = false
          + hibernation                          = false
          + host_id                              = ""
          + host_resource_group_arn              = null
          + iam_instance_profile                 = ""
          + id                                   = "i-0cbf92b9c9b587ae2"
          + instance_initiated_shutdown_behavior = "stop"
          + instance_lifecycle                   = ""
          + instance_market_options              = []
          + instance_state                       = "running"
          + instance_type                        = "t3.micro"
          + ipv6_address_count                   = 0
          + ipv6_addresses                       = []
          + key_name                             = ""
          + launch_template                      = []
          + maintenance_options                  = [
              + {
                  + auto_recovery = "default"
                },
            ]
          + metadata_options                     = [
              + {
                  + http_endpoint               = "enabled"
                  + http_protocol_ipv6          = "disabled"
                  + http_put_response_hop_limit = 1
                  + http_tokens                 = "optional"
                  + instance_metadata_tags      = "disabled"
                },
            ]
          + monitoring                           = false
          + network_interface                    = []
          + outpost_arn                          = ""
          + password_data                        = ""
          + placement_group                      = ""
          + placement_partition_number           = 0
          + primary_network_interface_id         = "eni-0a6e2b6acaf2c959e"
          + private_dns                          = "ip-172-31-47-251.ec2.internal"
          + private_dns_name_options             = [
              + {
                  + enable_resource_name_dns_a_record    = false
                  + enable_resource_name_dns_aaaa_record = false
                  + hostname_type                        = "ip-name"
                },
            ]
          + private_ip                           = "172.31.47.251"
          + public_dns                           = "ec2-34-201-219-127.compute-1.amazonaws.com"
          + public_ip                            = "34.201.219.127"
          + root_block_device                    = [
              + {
                  + delete_on_termination = true
                  + device_name           = "/dev/sda1"
                  + encrypted             = false
                  + iops                  = 3000
                  + kms_key_id            = ""
                  + tags                  = {}
                  + tags_all              = {}
                  + throughput            = 125
                  + volume_id             = "vol-06008f4624933e91b"
                  + volume_size           = 20
                  + volume_type           = "gp3"
                },
            ]
          + secondary_private_ips                = []
          + security_groups                      = [
              + "SG-expense-dev",
            ]
          + source_dest_check                    = true
          + spot_instance_request_id             = ""
          + subnet_id                            = "subnet-00c4747fc5f7495b4"
          + tags                                 = {
              + Name      = "expense-dev-mysql"
              + Project   = "expense"
              + Terraform = "true"
            }
          + tags_all                             = {
              + Name      = "expense-dev-mysql"
              + Project   = "expense"
              + Terraform = "true"
            }
          + tenancy                              = "default"
          + timeouts                             = null
          + user_data                            = null
          + user_data_base64                     = null
          + user_data_replace_on_change          = false
          + volume_tags                          = null
          + vpc_security_group_ids               = [
              + "sg-07973edd1eea8e567",
            ]
        },
      + {
          + ami                                  = "ami-09c813fb71547fc4f"
          + arn                                  = "arn:aws:ec2:us-east-1:194722417509:instance/i-0618eded1f4416601"
          + associate_public_ip_address          = true
          + availability_zone                    = "us-east-1b"
          + capacity_reservation_specification   = [
              + {
                  + capacity_reservation_preference = "open"
                  + capacity_reservation_target     = []
                },
            ]
          + cpu_core_count                       = 1
          + cpu_options                          = [
              + {
                  + amd_sev_snp      = ""
                  + core_count       = 1
                  + threads_per_core = 2
                },
            ]
          + cpu_threads_per_core                 = 2
          + credit_specification                 = [
              + {
                  + cpu_credits = "unlimited"
                },
            ]
          + disable_api_stop                     = false
          + disable_api_termination              = false
          + ebs_block_device                     = []
          + ebs_optimized                        = false
          + enable_primary_ipv6                  = null
          + enclave_options                      = [
              + {
                  + enabled = false
                },
            ]
          + ephemeral_block_device               = []
          + get_password_data                    = false
          + hibernation                          = false
          + host_id                              = ""
          + host_resource_group_arn              = null
          + iam_instance_profile                 = ""
          + id                                   = "i-0618eded1f4416601"
          + instance_initiated_shutdown_behavior = "stop"
          + instance_lifecycle                   = ""
          + instance_market_options              = []
          + instance_state                       = "running"
          + instance_type                        = "t3.micro"
          + ipv6_address_count                   = 0
          + ipv6_addresses                       = []
          + key_name                             = ""
          + launch_template                      = []
          + maintenance_options                  = [
              + {
                  + auto_recovery = "default"
                },
            ]
          + metadata_options                     = [
              + {
                  + http_endpoint               = "enabled"
                  + http_protocol_ipv6          = "disabled"
                  + http_put_response_hop_limit = 1
                  + http_tokens                 = "optional"
                  + instance_metadata_tags      = "disabled"
                },
            ]
          + monitoring                           = false
          + network_interface                    = []
          + outpost_arn                          = ""
          + password_data                        = ""
          + placement_group                      = ""
          + placement_partition_number           = 0
          + primary_network_interface_id         = "eni-0ce848cff524581b6"
          + private_dns                          = "ip-172-31-37-127.ec2.internal"
          + private_dns_name_options             = [
              + {
                  + enable_resource_name_dns_a_record    = false
                  + enable_resource_name_dns_aaaa_record = false
                  + hostname_type                        = "ip-name"
                },
            ]
          + private_ip                           = "172.31.37.127"
          + public_dns                           = "ec2-54-167-87-147.compute-1.amazonaws.com"
          + public_ip                            = "54.167.87.147"
          + root_block_device                    = [
              + {
                  + delete_on_termination = true
                  + device_name           = "/dev/sda1"
                  + encrypted             = false
                  + iops                  = 3000
                  + kms_key_id            = ""
                  + tags                  = {}
                  + tags_all              = {}
                  + throughput            = 125
                  + volume_id             = "vol-09661db646349d394"
                  + volume_size           = 20
                  + volume_type           = "gp3"
                },
            ]
          + secondary_private_ips                = []
          + security_groups                      = [
              + "SG-expense-dev",
            ]
          + source_dest_check                    = true
          + spot_instance_request_id             = ""
          + subnet_id                            = "subnet-00c4747fc5f7495b4"
          + tags                                 = {
              + Name      = "expense-dev-backend"
              + Project   = "expense"
              + Terraform = "true"
            }
          + tags_all                             = {
              + Name      = "expense-dev-backend"
              + Project   = "expense"
              + Terraform = "true"
            }
          + tenancy                              = "default"
          + timeouts                             = null
          + user_data                            = null
          + user_data_base64                     = null
          + user_data_replace_on_change          = false
          + volume_tags                          = null
          + vpc_security_group_ids               = [
              + "sg-07973edd1eea8e567",
            ]
        },
      + {
          + ami                                  = "ami-09c813fb71547fc4f"
          + arn                                  = "arn:aws:ec2:us-east-1:194722417509:instance/i-0126b87ee7ceaf59f"
          + associate_public_ip_address          = true
          + availability_zone                    = "us-east-1b"
          + capacity_reservation_specification   = [
              + {
                  + capacity_reservation_preference = "open"
                  + capacity_reservation_target     = []
                },
            ]
          + cpu_core_count                       = 1
          + cpu_options                          = [
              + {
                  + amd_sev_snp      = ""
                  + core_count       = 1
                  + threads_per_core = 2
                },
            ]
          + cpu_threads_per_core                 = 2
          + credit_specification                 = [
              + {
                  + cpu_credits = "unlimited"
                },
            ]
          + disable_api_stop                     = false
          + disable_api_termination              = false
          + ebs_block_device                     = []
          + ebs_optimized                        = false
          + enable_primary_ipv6                  = null
          + enclave_options                      = [
              + {
                  + enabled = false
                },
            ]
          + ephemeral_block_device               = []
          + get_password_data                    = false
          + hibernation                          = false
          + host_id                              = ""
          + host_resource_group_arn              = null
          + iam_instance_profile                 = ""
          + id                                   = "i-0126b87ee7ceaf59f"
          + instance_initiated_shutdown_behavior = "stop"
          + instance_lifecycle                   = ""
          + instance_market_options              = []
          + instance_state                       = "running"
          + instance_type                        = "t3.micro"
          + ipv6_address_count                   = 0
          + ipv6_addresses                       = []
          + key_name                             = ""
          + launch_template                      = []
          + maintenance_options                  = [
              + {
                  + auto_recovery = "default"
                },
            ]
          + metadata_options                     = [
              + {
                  + http_endpoint               = "enabled"
                  + http_protocol_ipv6          = "disabled"
                  + http_put_response_hop_limit = 1
                  + http_tokens                 = "optional"
                  + instance_metadata_tags      = "disabled"
                },
            ]
          + monitoring                           = false
          + network_interface                    = []
          + outpost_arn                          = ""
          + password_data                        = ""
          + placement_group                      = ""
          + placement_partition_number           = 0
          + primary_network_interface_id         = "eni-05a5699108bd4a7ba"
          + private_dns                          = "ip-172-31-47-132.ec2.internal"
          + private_dns_name_options             = [
              + {
                  + enable_resource_name_dns_a_record    = false
                  + enable_resource_name_dns_aaaa_record = false
                  + hostname_type                        = "ip-name"
                },
            ]
          + private_ip                           = "172.31.47.132"
          + public_dns                           = "ec2-100-24-56-251.compute-1.amazonaws.com"
          + public_ip                            = "100.24.56.251"
          + root_block_device                    = [
              + {
                  + delete_on_termination = true
                  + device_name           = "/dev/sda1"
                  + encrypted             = false
                  + iops                  = 3000
                  + kms_key_id            = ""
                  + tags                  = {}
                  + tags_all              = {}
                  + throughput            = 125
                  + volume_id             = "vol-0fcc732667b14edc4"
                  + volume_size           = 20
                  + volume_type           = "gp3"
                },
            ]
          + secondary_private_ips                = []
          + security_groups                      = [
              + "SG-expense-dev",
            ]
          + source_dest_check                    = true
          + spot_instance_request_id             = ""
          + subnet_id                            = "subnet-00c4747fc5f7495b4"
          + tags                                 = {
              + Name      = "expense-dev-frontend"
              + Project   = "expense"
              + Terraform = "true"
            }
          + tags_all                             = {
              + Name      = "expense-dev-frontend"
              + Project   = "expense"
              + Terraform = "true"
            }
          + tenancy                              = "default"
          + timeouts                             = null
          + user_data                            = null
          + user_data_base64                     = null
          + user_data_replace_on_change          = false
          + volume_tags                          = null
          + vpc_security_group_ids               = [
              + "sg-07973edd1eea8e567",
            ]
        },
    ]
