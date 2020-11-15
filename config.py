##   Primary Author: Mayank Mohindra <github.com/mayankmtg>
##
##   Description: File contains list of configurable parameters to the application
##
import yaml

class Config:
    """
    Class to handle config values.
    The config keys are refreshed every time we hit load
    """

    # Config keys
    DISCORD_TOKEN = None
    DATABASE = None
    
    @staticmethod
    def load():
        """
        Static method to refresh/load the config key values
        """
        with open('config.yaml') as file:
            config_yaml = yaml.safe_load(file)

            # Set individual config keys
            Config.DISCORD_TOKEN = config_yaml['DISCORD_TOKEN']
            Config.DATABASE = config_yaml['DATABASE']

