class Utils:

    @staticmethod
    def clean_columns(df):

        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
        )

        return df
