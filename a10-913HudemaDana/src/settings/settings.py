import configparser


class SettingsConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()

    def read_setting(self):
        self.config.read('settings_prop.ini')
        self.config.sections()
        repo = self.config['settings.properties']['repository']
        activity = self.config['settings.properties']['activity']
        person = self.config['settings.properties']['person']
        return repo, activity, person
