def change_configuration(device, configuration):
       device.load_merge_candidate(filename=configuration)
       print(device.compare_config())
       device.commit_config()


