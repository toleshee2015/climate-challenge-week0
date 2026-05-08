class Utils:

    @staticmethod
    def get_country_flags():

        return {
            "Ethiopia": "🇪🇹",
            "Kenya": "🇰🇪",
            "Nigeria": "🇳🇬",
            "Tanzania": "🇹🇿",
            "Sudan": "🇸🇩",
            "Uganda": "🇺🇬",
        }

    @staticmethod
    def find_country_column(data):

        for col in data.columns:
            if col.lower() == "country":
                return col

        return None
