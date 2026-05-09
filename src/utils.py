class Utils:

    @staticmethod
    def get_country_flags():

        return {
            "Ethiopia": "🇪🇹",
            "Kenya": "🇰🇪",
            "Nigeria": "🇳🇬",
            "Sudan": "SD",
            "tanzania": "Tz"
        }

    @staticmethod
    def filter_countries(data, countries):

        return data[
            data["country"].isin(countries)
        ]
