from locale import currency
import pycountry
def get_currency():
    try:
        country_name = input("Enter the country name: ")
        country = pycountry.countries.lookup(country_name)
        currency = pycountry.currencies.get(numeric=country.numeric).alpha_3
        return f"Currency of {country_name} is {currency}"
    except Exception:
        return "Country not found or currency not available."

print(get_currency())