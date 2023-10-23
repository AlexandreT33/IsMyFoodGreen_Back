from openfoodfacts import API, APIVersion, Country, Environment, Flavor

class OpenFoodApi:
    
    api : API
    
    def __init__(self) -> None:
        self.connect()

    def connect(self):
        self.api = API(
            username=None,
            password=None,
            country=Country.world,
            flavor=Flavor.off,
            version=APIVersion.v3,
            environment=Environment.org,
    )